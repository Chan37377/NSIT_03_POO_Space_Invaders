import pygame  # necessaire pour charger les images et les sons


class Joueur() : # classe pour créer le vaisseau du joueur
    def __init__(self) :
        self.sens = "O"
        self.image = "vaisseau.png"
        self.position = 400-64
        
    def deplacer(self):
        if self.sens == "gauche":
            slef.position -= 0.5
            if self.position < 0:
                self.position = 0
        if self.sens == "droite":
            slef.position += 0.5
            if self.position > 800-64:
                self.position = 800-64
                
class Balle():
    def __init__(self)
        self.tireur = Joueur
        self.depart = Joueur.position  # 400-16
        self.hauteur =
        self.image = "balle.png"
        self.etat = 