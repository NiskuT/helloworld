from random import randrange
from itertools import permutations


def generer_PI(n, cmax):
	array = []
	if n <= cmax ** 2:
		while len(array) < n:
			xy = [randrange(0,cmax), randrange(0,cmax)]
			if not (xy in array):
				array.append(xy)
	return array

def distance(XaYa, XbYb):
	return (((XaYa[0]-XbYb[0])**2)+((XaYa[1]-XbYb[1])**2))**(1/2)



def listeChemin(nbElts):
	chemin = []
	a = permutations(range(nbElts))
	for k in a:
		chemin.append(k)
	return chemin




def forceBrute(listeDeCoordonnees,xyRobot):
	ddpcc = 1000000  # Distance du plus court chemin
	bestChemin = 0
	
	chemin = listeChemin(len(listeDeCoordonnees))

	for k in chemin:
		dist = 0
		dist += distance(xyRobot, listeDeCoordonnees[k[0]])
		for i in range(len(k)-1):
			dist += distance(listeDeCoordonnees[k[i]], listeDeCoordonnees[k[i+1]])
		if dist < ddpcc:
			ddpcc = dist
			bestChemin = k

	return ddpcc, bestChemin

a = generer_PI(9,10000)
# Génération de 9 point aléatoiredont les coordonnées sont dans l'interval [0,10000]
# Les points sont assimilés à une liste de couple de coordonnées

#print(a)
dist, chemin = forceBrute(a, (9000,100))
# La méthode force brute nous revoie la distance minimale et le chemin correspondant

print("Le chemin le plus court est:", chemin)
print("Cela correspond dans l'ordre aux points:")
for k in chemin:
    print(a[k])
print("La distance minimale est", int(dist),".")

import matplotlib.pyplot as plt

lstX = [a[k][0] for k in range(len(a))]
lstY = [a[k][1] for k in range(len(a))]

plt.title("Mars Exploration Rover")
plt.plot(lstX, lstY, 'ro')
plt.xlabel('x')
plt.ylabel('y')
plt.axis([0, 10000, 0, 10000])
#plt.show()

# Trace le chemin
listeX = [a[i][0] for i in chemin]
listeY = [a[i][1] for i in chemin]

plt.plot(listeX, listeY)
#plt.show()





