import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import sys
import numpy as np
#np.set_printoptions(threshold=sys.maxsize)

#matrice P
matrice_p = [
    #1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19 20 21 21 23 24 25 26 27 28 29 30 31 32 33 34 35 36
    [0, 0.25, 0, 0, 0, 0, 0, 0.25, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.25, 0.25], #1 x
    [0.25, 0, 0.25, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.25, 0, 0, 0, 0, 0, 0.25, 0, 0], #2 x
    [0, 0.25, 0, 0.25, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.25, 0, 0, 0, 0, 0, 0.25, 0, 0, 0], #3 x 
    [0, 0, 0.25, 0, 0.25, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.25, 0, 0, 0, 0, 0, 0.25, 0, 0, 0, 0], #4 x
    [0, 0, 0, 0.25, 0, 0.25, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.25, 0, 0, 0, 0, 0, 0.25, 0, 0, 0, 0, 0], #5 x
    [0, 0, 0, 0, 0.25, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.25, 0, 0, 0, 0, 0.25, 0.25, 0, 0, 0, 0, 0, 0], #6 x
    [0, 0, 0, 0, 0, 0, 0, 0.25, 0, 0, 0, 0, 0, 0, 0.25, 0.25, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.25], #7 x
    [0.25, 0, 0, 0, 0, 0, 0.25, 0, 0.25, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.25, 0, 0, 0, 0, 0, 0, 0, 0], #8 x
    [0, 0, 0, 0, 0, 0, 0, 0.25, 0, 0.25, 0, 0, 0, 0, 0, 0.25, 0.25, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #9 x
    [0, 0, 0, 0, 0, 0, 0, 0, 0.25, 0, 0.25, 0, 0, 0, 0, 0, 0, 0.25, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.25, 0, 0, 0, 0, 0, 0, 0, 0], #10 x
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0.25, 0, 0.25, 0, 0, 0, 0, 0, 0, 0.25, 0, 0, 0, 0, 0, 0, 0, 0.25, 0, 0, 0, 0, 0, 0, 0, 0, 0], #11 x
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.25, 0, 0.25, 0, 0, 0, 0, 0, 0, 0.25, 0, 0, 0, 0, 0, 0.25, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #12 x
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.25, 0, 0.25, 0, 0, 0, 0, 0, 0, 0.25, 0, 0, 0, 0.25, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #13 x
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.25, 0, 0, 0, 0, 0, 0, 0, 0, 0.25, 0.25, 0.25, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #14 x
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #15
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #16
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #17
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #18
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #19
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #20
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #21
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #22
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #23
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #24
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #25
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #26
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], #27
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], #28
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0], #29
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0], #30
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], #31
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], #32
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], #33
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], #34
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0], #35
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]  #36
    #1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19 20 21 21 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37
             ]


#potentiel électique aux noeuds absobrants
pot_for_point = [[-300, -300, -300, -300, -300, -300, -300, -300, 0, 0, 0, 0, 0, 0, 0, -300, -300, -300, -300, -300, -300, -300]]


steps = 10 ** 4

Pn = matrice_p

#multiplie la matrice P avec elle meme 10000 fois pour trouver une approximatiom très précise des probabilités qu’un état initial i soit absorbé par le noeud j
i=0
while i < steps:
    Pn = np.matmul(Pn, matrice_p)
    i += 1

#print ('Pn = ', Pn)

#for n in range (36):
#    print (np.sum(Pn[n]))


#garde seuleemnt l'information importante de la matrice Pn

mopdif1 = np.delete(Pn, range(14,36), 0)
mopdif2 = np.delete(mopdif1, range(14), 1)

#print('mopdif2 =', mopdif2)

#print('potentiel finale =', np.matmul(mopdif2, np.transpose(pot_for_point))) (à print pour remplir la matrice contenu_matrice)


# Charger l'image depuis l'ordinateur
image = mpimg.imread("C:/Users/louxc/OneDrive/Desktop/projet-num-elmg/travaile-num-elg/Q3bg.JPG")

# Créer une matrice pour contenir les valeurs affichées aux intersections des lignes, les données sont entré manuellement depuis un print fait plus haut (ligne 77)
contenu_matrice = [
    ['', '', '-300', '-300', '-300', '-300', '-300', '-300', ''],
    ['', '-300', '-240.60', '-174.08', '-155.74', '-148.86', '-139.70', '-109.92', '0'],
    ['-300', '-272.08', '-188.32', '0', '0', '0', '0', '0', ''],
    ['', '-300', '-240.60', '-174.08', '-155.74', '-148.86', '-139.70', '-109.92', '0'],
    ['', '', '-300', '-300', '-300', '-300', '-300', '-300', '']
]



# Dimensions de l'image
largeur_image = 115

# Calculer la hauteur de l'image proportionnellement à la largeur
hauteur_image = largeur_image * image.shape[0] / image.shape[1]

# Créer une grille de points pour les lignes verticales
x = np.linspace(0, largeur_image, 10)

# Créer une grille de points pour les lignes horizontales
y = np.linspace(0, hauteur_image, 6)

plt.figure()

# Afficher l'image en arrière-plan avec les dimensions spécifiées
plt.imshow(image, extent=[0, largeur_image, 0, hauteur_image])

# Dessiner les lignes verticales grises
for i in range(len(x)):
    plt.plot([x[i], x[i]], [0, hauteur_image], color='gray')

# Dessiner les lignes horizontales grises
for j in range(len(y)):
    plt.plot([0, largeur_image], [y[j], y[j]], color='gray')


# Taille de police
taille_police_1 = min(largeur_image, hauteur_image) * 0.15

# Afficher le contenu de la matrice dans les carrées
for i in range(len(x) - 1):
    for j in range(len(y) - 1):
        plt.text((x[i] + x[i+1]) / 2, (y[j] + y[j+1]) / 2, contenu_matrice[j][i],
                 horizontalalignment='center', verticalalignment='center', color = 'gray', fontsize=taille_police_1)


plt.xlim(0, largeur_image)
plt.ylim(0, hauteur_image)
plt.axis('off')

#afficher le graphique de potentiel
plt.show()


noeud_matrice = [
    ['', '', '17', '18', '19', '20', '21', '22', ''],
    ['', '16', '9', '10', '11', '12', '13', '14', '23'],
    ['15', '7', '8', '28', '27', '26', '25', '24', ''],
    ['', '36', '1', '2', '3', '4', '5', '6', '29'],
    ['', '', '35', '34', '33', '32', '31', '30', '']
]

# Dimensions de l'image
largeur_image = 115

# Calculer la hauteur de l'image proportionnellement à la largeur
hauteur_image = largeur_image * image.shape[0] / image.shape[1]

# Créer une grille de points pour les lignes verticales
x = np.linspace(0, largeur_image, 10)

# Créer une grille de points pour les lignes horizontales
y = np.linspace(0, hauteur_image, 6)

plt.figure()

# Afficher l'image en arrière-plan avec les dimensions spécifiées
plt.imshow(image, extent=[0, largeur_image, 0, hauteur_image])

# Dessiner les lignes verticales grises
for i in range(len(x)):
    plt.plot([x[i], x[i]], [0, hauteur_image], color='gray')

# Dessiner les lignes horizontales grises
for j in range(len(y)):
    plt.plot([0, largeur_image], [y[j], y[j]], color='gray')

# Taille de police
taille_police_2 = min(largeur_image, hauteur_image) * 0.4

# Afficher le contenu de la matrice dans les carrées
for i in range(len(x) - 1):
    for j in range(len(y) - 1):
        plt.text((x[i] + x[i+1]) / 2, (y[j] + y[j+1]) / 2, noeud_matrice[j][i],
                 horizontalalignment='center', verticalalignment='center', color = 'gray', fontsize=taille_police_2)

plt.xlim(0, largeur_image)
plt.ylim(0, hauteur_image)
plt.axis('off')

#afficher le graphique des numéro de case
plt.show()