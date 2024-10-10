import pygame  # necessaire pour charger les images et les sons
import random
import math

class Joueur() : # classe pour créer le vaisseau du joueur
    def __init__(self) :
        self.sens = "O"
        self.image = pygame.image.load("vaisseau.png")
        self.position = 400-64
        self.score = 0
        
    def deplacer(self):
        if self.sens == "gauche":
            self.position -= 0.5
            if self.position < 0:
                self.position = 0
        if self.sens == "droite":
            self.position += 0.5
            if self.position > 800-64:
                self.position = 800-64
                
    def tirer(self):
        self.sens = "O"
        
    def marquer(self):
        self.score += 1
        
        
                
class Balle():
    def __init__(self, player):
        self.tireur = player
        self.depart = player.position + 16  
        self.hauteur =495
        self.image = pygame.image.load("balle.png")
        self.etat = "chargee"
        
    def bouger(self):
        if self.etat == "chargee":
            self.depart = self.tireur.position + 16  
        else:
            # Cas où self.etat == "tiree"
            self.hauteur -= 1
            if self.hauteur < 0:
                self.etat = "chargee"
                self.hauteur = 495
                
    def toucher(self, vaisseau):
        if (math.fabs(self.hauteur - vaisseau.hauteur) < 40) and (math.fabs(self.depart - vaisseau.depart) < 40):
            self.etat = "chargee"
            self.hauteur = 495
            return True
        
                
                
                
class Ennemi():
    
    NbEnnemis = 7
    
    def __init__(self):
        self.depart = random.randint(0, 800-64)
        self.hauteur = random.randint(0, 75)
        self.type = random.randint(1, 2)
        self.image = pygame.image.load("invader1.png") or pygame.image.load("invader2.png") 
        self.vitesse = 0.1
        
        
    def avancer(self):
        self.hauteur += self.vitesse
        if self.hauteur > 600:
            self.hauteur = 0
            
    def disparaitre(self):
        self.depart = random.randint(1,800-64)
        self.hauteur = random.randint(0, 100)
        self.type = random.randint(1,2)
        if  (self.type == 1):
            self.image = pygame.image.load("invader1.png")
            self.vitesse = 0.2
        elif (self.type ==2):
            self.image = pygame.image.load("invader2.png")
            self.vitesse = 0.1
        
        
        

        