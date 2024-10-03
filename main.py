
import os
import time
import copy
import numpy as np


class JeuDeLaVie:
    def __init__(self, tableau):
        
        self.tableau = copy.deepcopy(tableau)
        self._tableau_a_ne_pas_toucher = copy.deepcopy(tableau)
        print(self.tableau)


    def run(self, nombre_tours, delai):
        """
        Méthode principale du jeu.

        Fait tourner le jeu de la vie pendant nombre_tours.
        Elle rafraichit l'affichage à chaque tour
        et attend delai entre chaque tour.

        :param nombre_tours: nombre de tours à effectuer
        :param delai: temps d'attente en secondes entre chaque tour
        """

        for cpt in range(nombre_tours) :
            self.tour()
            time.sleep(delai)
            os.system("cls")
            #self.affichage()
            print(self.tableau)


    """
        def affichage(self) :
            tab = str(self.tableau)
            lines, length = self.tableau.shape
            for cpt_1 in range(lines):
                for cpt_2 in range(length):

                    if self.tableau[cpt_1,cpt_2] == 0 :
                        tab[cpt_1, cpt_2] = "."
            print(tab)

    """

    def tour(self):
        """
        Met à jour toute les cellules du tableau en respectant les règles
        du jeu de la vie.
        """
        lignes, colonnes = self.tableau.shape
        for cpt_1 in range(lignes) :
            for cpt_2 in range(colonnes) :
                self.tableau[cpt_1,cpt_2] = self.resultat(self._tableau_a_ne_pas_toucher[cpt_1,cpt_2], self.total_voisins(cpt_1, cpt_2))
                # l'element du tableau reçoit le retour de la méthode résultat qui prend en paramètre la valeur de l'élément du tableau et le total des voi
                #  ATTENTION : on n'utilise pas self.tableau mais plûtôt self._tableau_a_ne_pas_toucher car le self._tableau est modifé lors du début de cette méthode 

        self._tableau_a_ne_pas_toucher = copy.deepcopy(self.tableau)




    def valeur_case(self, i, j):
        """ Renvoie la valeur de la case [i][j] ou 0 si la case n�existe pas. """
        lignes, colonnes = self.tableau.shape
        
        if lignes < i and colonnes < j :
            return 0 
        else :
            return self.tableau[i][j]


    def total_voisins(self, i, j):
        """Renvoie la somme des valeurs des voisins de la case [i][j]."""
        lignes, colonnes = self._tableau_a_ne_pas_toucher.shape
        som = 0
        if i not in range(lignes) or j not in range(colonnes) :
            return 0
        
        else :
            if  i > 0 and i < lignes-1 and j > 0 and j < colonnes-1 :  # cas o� la case ne se situe pas au bord du tableau
                for cpt1 in range(i-1, i+2): 
                    for cpt2 in range(j-1, j+2) :
                        som += self._tableau_a_ne_pas_toucher[cpt1,cpt2]
            
                som -= self._tableau_a_ne_pas_toucher[i, j]
                return som
        
            elif i == 0 and j == 0 :    # cas de la premiere case du tableau
                for cpt1 in range(2):
                    for cpt2 in range(2):
                        som += self._tableau_a_ne_pas_toucher[cpt1, cpt2]

                som -= self._tableau_a_ne_pas_toucher[i, j]
                return som        


            elif i == lignes - 1  and j == 0 :    # cas de la case en fin de la premiere colonne
                for cpt1 in range(lignes-2 , lignes):
                    for cpt2 in range(2):
                        som += self._tableau_a_ne_pas_toucher[cpt1, cpt2]

                som -= self._tableau_a_ne_pas_toucher[i, j]
                return som


            elif j == 0 and i in range(1,colonnes-1) :     #cas des cases qui se situent entre la premiere et la derniere dans la premiere colonne
                for cpt1 in range(i-1, i+2) :
                    for cpt2 in range(2) :
                        som += self._tableau_a_ne_pas_toucher[cpt1, cpt2]

                som -= self._tableau_a_ne_pas_toucher[i, j]
                return som
                    
            
            elif i == 0 and  j > 0 and j < colonnes -1 :   # cas de toutes les cases situ�es entre le premier et le dernier sur la premiere ligne
                for cpt1 in range(2):
                    for cpt2 in range(j-1, j+2) :
                        som += self._tableau_a_ne_pas_toucher[cpt1, cpt2]

                som -= self._tableau_a_ne_pas_toucher[i, j]
                return som



            elif i == lignes-1 and j == colonnes-1 :     #cas de la derniere case dans le tableau soit celle qui se trouve a la fin dans la derniere colonne
                for cpt1 in range(lignes-2, lignes) :
                    for cpt2 in range(colonnes-2, colonnes) :
                        som += self._tableau_a_ne_pas_toucher[cpt1, cpt2]

                som -= self._tableau_a_ne_pas_toucher[i, j]
                return som
        

            elif i == lignes-1 and  j in range(1,colonnes-1) :     #cas des cases qui se situent entre la premiere case et la derniere dans la derniere ligne
                for cpt1 in range(lignes-2, lignes) :
                    for cpt2 in range(j-1, j+2) :
                        som += self._tableau_a_ne_pas_toucher[cpt1, cpt2]

                som -= self._tableau_a_ne_pas_toucher[i, j]
                return som
            

            elif j == colonnes-1 and i in range(1,lignes -1) :     #cas des cases qui se situent en dessous de la premiere case sauf le dernier dans la derniere colonne
                for cpt1 in range(i-1, i+2) :
                    for cpt2 in range(colonnes-2, colonnes) :
                        som += self._tableau_a_ne_pas_toucher[cpt1, cpt2]

                som -= self._tableau_a_ne_pas_toucher[i, j]
                return som


            elif i == 0 and j == colonnes-1 :     #cas de la derniere case sur la premiere ligne
                for cpt1 in range(lignes-2, lignes) :
                    for cpt2 in range(colonnes-2,colonnes) :
                        som += self._tableau_a_ne_pas_toucher[cpt1, cpt2]

                som -= self._tableau_a_ne_pas_toucher[i, j]
                return som



    def resultat(self, valeur_case, total_voisins):
        """
        Renvoie la valeur suivante d�une la cellule.

        :param valeur_case: la valeur de la cellule (0 ou 1)
        :param total_voisins: la somme des valeurs des voisins
        :return: la valeur de la cellule au tour suivant

        >>> a = JeuDeLaVie([])
        >>> a.resultat(0, 3)
        1
        >>> a = JeuDeLaVie([])
        >>> a.resultat(0, 1)
        0
        >>> a = JeuDeLaVie([])
        >>> a.resultat(0, 4)
        0
        >>> a = JeuDeLaVie([])
        >>> a.resultat(1, 2)
        1
        >>> a = JeuDeLaVie([])
        >>> a.resultat(1, 3)
        1
        >>> a = JeuDeLaVie([])
        >>> a.resultat(1, 1)
        0
        >>> a = JeuDeLaVie([])
        >>> a.resultat(1, 4)
        0
        """
        if valeur_case == 0 :
            if total_voisins == 3 :
                return 1 
            else :
                return 0 
        elif valeur_case == 1 :
            if total_voisins == 2 or total_voisins == 3 :
                return 1
            else :
                return 0   


tableau = np.zeros((15,15))
for cpt in range(8) :
    tableau[1,cpt+3] = 1
    tableau[3,cpt] = 1
    tableau[0,cpt+5] = 1
    tableau[5,cpt] = 1
    tableau[4,cpt+3] = 1
    tableau[6,cpt] = 1
    tableau[7,cpt+4] = 1
    tableau[8,cpt+5] = 1
    tableau[9,cpt+2] = 1
    tableau[11,cpt+1] = 1
    tableau[12,cpt] = 1
    tableau[13,cpt+3] = 1
    tableau[14,cpt+5] = 1
ma_classe = JeuDeLaVie(tableau)
ma_classe.run(5,2)

#ma_classe.tableau[0,1] = ma_classe.resultat(ma_classe._tableau_a_ne_pas_toucher[0,1], ma_classe.total_voisins(0,1))




"""
lignes, colonnes = ma_classe.tableau.shape
for cpt_1 in range(lignes) :
    for cpt_2 in range(colonnes) :
        ma_classe.tableau[cpt_1,cpt_2] = ma_classe.resultat(ma_classe._tableau_a_ne_pas_toucher[cpt_1,cpt_2], ma_classe.total_voisins(cpt_1, cpt_2))

#print(ma_classe._tableau_a_ne_pas_toucher)  
#print(ma_classe.tableau)
"""
