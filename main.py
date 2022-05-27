#Module permettant de créer un jeu avec interface graphique notamment
import pygame
#Module permettant d'utiliser des variables et des fonctions en lien avec l'exécution du programme (interactions avec l'interpréteur python)
import sys
#Module permettant de travailler avec des valeurs aléatoires
import random
#Module permettant de manipuler le temps dans un programme
import time
#Module re (Regular Expression) qui permet d'utiliser des expressions régulières et ainsi les utiliser. Cela spécifie un ensemble de chaînes (donc: modèle) qui lui correspond. 
import re
#Module permettant d'accéder aux fonctions mathématiques 
import math
#pygame.locals aide à appeler des fonctions et constantes utilisées souvent 
from pygame.locals import *
#Importe la liste avec les mots à trouver, choisis par la suite aléatoirement
from mots import liste_mots

#code RGB couleurs (noir, blanc, marron)
BLACK = (0,0,0)
WHITE = (255,255,255)
MARRON = (153,102,51)


#Initialisation du module pygame
pygame.init()

#Pour generer la fenetre du jeu
pygame.display.set_caption("Jeu du Pendu")

#Pour gérer les dimensions de la fenetre de jeu
screen = pygame.display.set_mode((1600,900))

#Pour importer puis charger l'arrière-plan
background = pygame.image.load('TEMPLATES/background_canyon.jpg')
background = pygame.transform.scale(background, (1600, 900))

#Pour importer puis charger la bannière
banner = pygame.image.load('TEMPLATES/banner.png')
banner = pygame.transform.scale(banner, (750, 550))
banner_rect = banner.get_rect()#Associe la surface de l'image à un rectangle (important)
banner_rect.x = math.ceil(screen.get_width() / 4)

#Pour importer puis charger notre bouton pour lancer la partie
play_button = pygame.image.load('TEMPLATES/button_jouer.png')
play_button = pygame.transform.scale(play_button, (275, 100))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 2.5)
play_button_rect.y = math.ceil(screen.get_height() / 1.68)

#Pour importer puis charger le boutton pour rejouer (à la fin de la partie)
rejouer = pygame.image.load('TEMPLATES/rejouer_button.png')
rejouer = pygame.transform.scale(rejouer, (75, 75))
rejouer_rect = rejouer.get_rect()
rejouer_rect.x = 10
rejouer_rect.y = 50


#———————————————————PENDU ERREUR 1—————————————————————————#
pendu1 = pygame.image.load('TEMPLATES/10.png')
pendu1 = pygame.transform.scale(pendu1, (550, 570))
pendu1_rect = pendu1.get_rect()
pendu1_rect.x = 200
pendu1_rect.y = 300

#———————————————————PENDU ERREUR 2—————————————————————————#
pendu2 = pygame.image.load('TEMPLATES/9.png')
pendu2 = pygame.transform.scale(pendu2, (550, 570))
pendu2_rect = pendu2.get_rect()
pendu2_rect.x = 200
pendu2_rect.y = 300

#———————————————————PENDU ERREUR 3—————————————————————————#
pendu3 = pygame.image.load('TEMPLATES/8.png')
pendu3 = pygame.transform.scale(pendu3, (550, 570))
pendu3_rect = pendu3.get_rect()
pendu3_rect.x = 200
pendu3_rect.y = 300

#———————————————————PENDU ERREUR 4—————————————————————————#
pendu4 = pygame.image.load('TEMPLATES/7.png')
pendu4 = pygame.transform.scale(pendu4, (550, 570))
pendu4_rect = pendu4.get_rect()
pendu4_rect.x = 200
pendu4_rect.y = 300

#———————————————————PENDU ERREUR 5—————————————————————————#
pendu5 = pygame.image.load('TEMPLATES/6.png')
pendu5 = pygame.transform.scale(pendu5, (550, 570))
pendu5_rect = pendu5.get_rect()
pendu5_rect.x = 200
pendu5_rect.y = 300

#———————————————————PENDU ERREUR 6—————————————————————————#
pendu6 = pygame.image.load('TEMPLATES/5.png')
pendu6 = pygame.transform.scale(pendu6, (550, 570))
pendu6_rect = pendu6.get_rect()
pendu6_rect.x = 200
pendu6_rect.y = 300

#———————————————————PENDU ERREUR 7—————————————————————————#
pendu7 = pygame.image.load('TEMPLATES/4.png')
pendu7 = pygame.transform.scale(pendu7, (550, 570))
pendu7_rect = pendu7.get_rect()
pendu7_rect.x = 200
pendu7_rect.y = 300

#———————————————————PENDU ERREUR 8—————————————————————————#
pendu8 = pygame.image.load('TEMPLATES/3.png')
pendu8 = pygame.transform.scale(pendu8, (550, 570))
pendu8_rect = pendu8.get_rect()
pendu8_rect.x = 200
pendu8_rect.y = 300

#———————————————————PENDU ERREUR 9—————————————————————————#
pendu9 = pygame.image.load('TEMPLATES/2.png')
pendu9 = pygame.transform.scale(pendu9, (550, 570))
pendu9_rect = pendu9.get_rect()
pendu9_rect.x = 200
pendu9_rect.y = 300

#———————————————————PENDU ERREUR 10—————————————————————————#
pendu10 = pygame.image.load('TEMPLATES/1.png')
pendu10 = pygame.transform.scale(pendu10, (550, 570))
pendu10_rect = pendu10.get_rect()
pendu10_rect.x = 200
pendu10_rect.y = 300

#———————————————————PENDU ERREUR 11—————————————————————————#
pendu11 = pygame.image.load('TEMPLATES/0.png')
pendu11 = pygame.transform.scale(pendu11, (550, 570))
pendu11_rect = pendu11.get_rect()
pendu11_rect.x = 200
pendu11_rect.y = 300



#Gérer les polices d'écriture
Font = pygame.font.Font("freesansbold.ttf",70)
Font2 = pygame.font.Font("freesansbold.ttf",40)

#Générer le fond d'écran du jeu
screen.blit(background, (0,0))



#Fonction qui permet d'obtenir la valeur du rang du mot choisi au hasard lorsque le joueur 'joue'
def motHasard(jouer):
    motHasard = 0
    if jouer == 1:
        #Permet de créer une variable ayant pour valeur le rang du mot à trouver, choisi au hasard grace a random.randint
        motHasard = random.randint(0,len(liste_mots)-1) # 0 et -1 pour la 'plage' d'indice (rangs) des mots de la liste
    #print(motHasard) -> ne pas afficher (utile pour vérifier la fonctionnalité)
    return motHasard


#Fonction qui permet de récupérer la valeur 'string' du mot choisi au hasard lorsque le joueur 'joue'
def List(nombre,jouer):
    if jouer == 1:
        Mot = liste_mots[nombre]   
    #print(Mot) -> ne pas afficher (utile pour vérifier la fonctionnalité)
    return Mot 



#Fonction qui permet d'associer le nb d'erreur à sa représentation graphique du pendu correspondant
def Pendu(erreur):
    if (erreur == 0):
        print("Pas d'erreur")

    elif (erreur == 1):
        screen.blit(pendu1, pendu1_rect)

    elif (erreur == 2):
        screen.blit(pendu2, pendu2_rect)

    elif (erreur == 3):
        screen.blit(pendu3, pendu3_rect)

    elif (erreur == 4):
        screen.blit(pendu4, pendu4_rect)

    elif (erreur == 5):
        screen.blit(pendu5, pendu5_rect)

    elif (erreur == 6):
        screen.blit(pendu6, pendu6_rect)

    elif (erreur == 7):
        screen.blit(pendu7, pendu7_rect)

    elif (erreur == 8):
        screen.blit(pendu8, pendu8_rect)

    elif (erreur == 9):
        screen.blit(pendu9, pendu9_rect)

    elif (erreur == 10):
        screen.blit(pendu10, pendu10_rect)

    #PERDUUUUUUUUUUUUUUUUUUU!!!!!!!!!!!
    elif (erreur == 11):
        screen.blit(pendu11, pendu11_rect)

        


#Fonction qui définit l'élément sheriff (utlile pour afficher l'image du sheriff par la suite)
#Aucun impact sur l'aspect technique du jeu
#--- EFFET VISUEL ---#
def sheriff():
    sheriff = pygame.image.load('TEMPLATES/sheriff.png')
    sheriff = pygame.transform.scale(sheriff, (500, 500))
    sheriff_rect = sheriff.get_rect()
    sheriff_rect.x = 1100
    sheriff_rect.y = 350
    screen.blit(sheriff, sheriff_rect)

#Fonction qui définit l'élément bulle (utlile pour afficher l'image de la bulle par la suite, qui sert à donner des indications au joueur)
#Aucun impact sur l'aspect technique du jeu
#--- EFFET VISUEL ---#
def bulle():
    bulle = pygame.image.load('TEMPLATES/bulle.png')
    bulle = pygame.transform.scale(bulle, (500, 275))
    bulle_rect = bulle.get_rect()
    bulle_rect.x = 950
    bulle_rect.y = 150
    screen.blit(bulle, bulle_rect)


#Fonction qui définit l'élément bagcoin (utlile pour afficher l'image du sac de pièces par la suite)
#Aucun impact sur l'aspect technique du jeu
#--- EFFET VISUEL ---#
def bagcoin():
    bagcoin = pygame.image.load('TEMPLATES/bagcoin.png')
    bagcoin = pygame.transform.scale(bagcoin, (500, 450))
    bagcoin_rect = bagcoin.get_rect()
    bagcoin_rect.x = 100
    bagcoin_rect.y = 500
    screen.blit(bagcoin, bagcoin_rect)


#Fonction qui définit l'élément cercueil (utlile pour afficher l'image du cercueil par la suite)
#Aucun impact sur l'aspect technique du jeu
#--- EFFET VISUEL ---#
def cercueil():
    cercueil = pygame.image.load('TEMPLATES/cercueil.png')
    cercueil = pygame.transform.scale(cercueil, (600, 250))
    cercueil_rect = cercueil.get_rect()
    cercueil_rect.x = 100
    cercueil_rect.y = 650
    screen.blit(cercueil, cercueil_rect)



#Fonction qui définit l'élément cercueil (utlile pour afficher l'image du boutton rejouer par la suite à la fin de la partie)
#--- EFFET VISUEL ---#
def rejouer():
    rejouer = pygame.image.load('TEMPLATES/rejouer_button.png')
    rejouer = pygame.transform.scale(rejouer, (75, 75))
    rejouer_rect = rejouer.get_rect()
    rejouer_rect.x = 10
    rejouer_rect.y = 50
    screen.blit(rejouer, rejouer_rect)



#Fonction qui déninit le menu du jeu (avant que le joueur cliquer sur 'jouer')
#Affche la bannière du jeu + le 'boutton' jouer
def Menu():
    screen.blit(play_button, play_button_rect)
    screen.blit(banner, banner_rect)


#————————————FONCTION PRINCIPALE DU JEU————————————#
def main():
    BLACK = (0,0,0)
    WHITE = (255,255,255)
    MARRON = (153,102,51)

    #Etat initial avant que je joueur ne clique sur le 'boutton' jouer
    PlayGame = 0
	
    #Appelle la fonction 'Menu' définie au dessus
    Menu()
		
    
    Running = True
    while Running:

        #Pour tous les evenements 
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == MOUSEBUTTONDOWN:
                #Detecte si le joueur clique sur le 'boutton' jouer
                if play_button_rect.collidepoint(event.pos):
                    #Alors la variable PlayGame prend la valeur de 1
                    PlayGame = 1
                    Running = False
                    break


        if PlayGame == 1:
            screen.blit(background, (0,0))
            
        pygame.display.update()
        

    Numéro = motHasard(PlayGame)                      
    MotCache = List(Numéro, PlayGame)

    #Crée une liste vide 
    ListeVide = []
    #Crée une liste vide (pour les lettres déja utilisées)
    Letter_Used = []

    for i in range(len(MotCache)):
        ListeVide.append('-') #Pour faire correspondre le nombre de lettre au nombre de trait grace a 'len' 

    
    pygame.draw.rect(screen,MARRON,(300,150,400,110)) #Pour afficher le rectangle marron
    Trait = Font.render("".join(ListeVide),True,WHITE) #Pour afficher le trait correspondant à chaque lettre (connaitre la longueur du mot)
    TraitRect = Trait.get_rect()
    TraitRect.center = (500,215)
    screen.blit(Trait,TraitRect)

    Erreur = 0 #Au début du jeu le nb d'erreur est de 0
    FinDuJeu = 0 #Etat du jeu -> pas fini 



    while True:

        #Cela permet que la difficulté soit la meme quelque soit la longueur du mot (nombre d'erreurs max -> équilibré en fonction de la longueur du mot)
        if len(MotCache) <= 4 :
          total_erreur = 7
        elif len(MotCache) > 4 and len(MotCache) <= 7 :
          total_erreur = 10
        else :
          total_erreur = math.ceil(len(MotCache) * 1.2)
        etat_pendu = round(Erreur / total_erreur * 10)
        if etat_pendu == 10 and Erreur != 0:
          etat_pendu = etat_pendu - 1
        
        Pendu(etat_pendu)
        sheriff()
        bulle()
        
        for event in pygame.event.get():

            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            elif event.type == KEYDOWN:
 

                #Permet rechercher les touches pressées allant de A à Z
                if re.search("[a-z]",chr(event.key)):
                    pygame.draw.rect(screen,MARRON,(300,150,400,110)) #Pour cacher la couche de mot 
                    
                    screen.blit(pygame.font.Font("freesansbold.ttf",30).render("Lettres déjà utilisées:",True,BLACK),(30,40))

                    #Permet d'afficher les lettres déja utilisées
                    if chr(event.key) not in Letter_Used :
                      Letter_Used.append(chr(event.key))
                    Word1 = Font2.render(" ".join(Letter_Used),True,BLACK)
                    Word1Rect = Word1.get_rect()
                    Word1Rect.x = 440
                    Word1Rect.y = 30
                    screen.blit(Word1,Word1Rect)
                    
                  
                    #chr (char) permet de convertir un entier en son code unicode associé (donc renvoyer le caractère)
                    #event.key pour savoir quelle touche du clavier est enfoncé
                    if ((chr(event.key).upper() in MotCache) or (chr(event.key).lower() in MotCache)):
                        for i in range(len(MotCache)):
                            if ((MotCache[i] == (chr(event.key)).upper()) or (MotCache[i] == (chr(event.key)).lower())):
                                ListeVide[i] = MotCache[i]


                    elif chr(event.key).upper not in Letter_Used or chr(event.key).lower not in Letter_Used :
                        Erreur = Erreur + 1
                      
                      
                    
                    #Pour afficher le trait correspondant à chaque lettre (connaitre la longueur du mot)
                    Trait = Font.render("".join(ListeVide),True,WHITE)
                    TraitRect = Trait.get_rect()
                    TraitRect.center = (500,215)
                    screen.blit(Trait,TraitRect)

                    
            
        #Si la partie est perdue 
        if (Erreur/total_erreur == 1):
            screen.blit(background, (0,0))

            sheriff()
            cercueil()
            rejouer()
            

            

            screen.blit(pygame.font.Font("freesansbold.ttf",30).render("Appuyez pour revenir au menu",True,BLACK),(90,70))

            bulle_perdu = pygame.image.load('TEMPLATES/bulle_lost.png')
            bulle_perdu = pygame.transform.scale(bulle_perdu, (500, 275))
            bulle_perdu_rect = bulle_perdu.get_rect()
            bulle_perdu_rect.x = 950
            bulle_perdu_rect.y = 150
            screen.blit(bulle_perdu, bulle_perdu_rect)

            Word = Font2.render("Le mot était:",True,BLACK)
            WordRect = Word.get_rect()
            WordRect.center = (650,250)
            screen.blit(Word,WordRect)

            Word2 = Font.render(MotCache,True,BLACK)
            Word2Rect = Word2.get_rect()
            Word2Rect.center = (650,315)
            screen.blit(Word2,Word2Rect)

            FinDuJeu = 1


        elif (MotCache == "".join(ListeVide)): #Remplace les traits par le mot complet 
            screen.blit(background, (0,0))
            
            sheriff()
            bagcoin()
            rejouer()
            
            screen.blit(pygame.font.Font("freesansbold.ttf",30).render("Appuyez pour revenir au menu",True,BLACK),(90,70))
         
            bulle_gagne = pygame.image.load('TEMPLATES/bulle_win.png')
            bulle_gagne = pygame.transform.scale(bulle_gagne, (500, 275))
            bulle_gagne_rect = bulle_gagne.get_rect()
            bulle_gagne_rect.x = 950
            bulle_gagne_rect.y = 150
            screen.blit(bulle_gagne, bulle_gagne_rect)
            
            
            Word = Font2.render("Le mot est:",True,BLACK)
            WordRect = Word.get_rect()
            WordRect.center = (650,250)
            screen.blit(Word,WordRect)

            Word2 = Font.render(MotCache,True,BLACK)
            Word2Rect = Word2.get_rect()
            Word2Rect.center = (650,315)
            screen.blit(Word2,Word2Rect)
            
            
            FinDuJeu = 1



        pygame.display.update()


        if (FinDuJeu == 1):

            
          
             #Rajouter une partie rejouer ou quitter
            for event in pygame.event.get():
              if event.type == QUIT:
                pygame.quit()
                sys.exit()

              elif event.type == MOUSEBUTTONDOWN:
                #Detecte si le joueur clique sur le 'boutton' rejouer
                if rejouer_rect.collidepoint(event.pos):
                    
                    screen.blit(background, (0,0))
                    main()

                  
main()


