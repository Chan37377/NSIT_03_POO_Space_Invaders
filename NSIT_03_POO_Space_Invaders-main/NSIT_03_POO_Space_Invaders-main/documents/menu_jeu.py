import pygame
import sys
import space_invaders_5
from button import Button

pygame.init()

ecran=pygame.display.set_mode((800,600))
pygame.display.set_caption("Menu")

background=pygame.image.load("fondecranm.png")

def menu():
    pygame.display.set_caption("Menu")
    
    while True:
        ecran.blit(background, (0,0))
        
        position_souris=pygame.mouse.get_pos()
        
        texte_menu=get_font(100).render("Battle War", True, "#b68f40")
        positon_texte_menu=texte_menu.get_rect(center=(400,90))
        
        boutton_jouer=Button(image=pygame.image.load("assets/Play Rect.png"), pos=(400,190),
                             text_input="Jouer", font=get_font(75), base_color="d7fcd4",hovering_color="White")
        boutton_quitter=Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(400,290),
                             text_input="Quitter", font=get_font(75), base_color="d7fcd4",hovering_color="White")
        
        ecran.blit(texte_menu, positon_texte_menu)
        
        for boutton in [boutton_jouer, boutton_quitter]:
            boutton.changeColor(position_souris)
            bouton.update(ecran)
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if boutton_jouer.checkForInput(position_souris):
                    space_invaders_5
                if boutton_quitter.checkForInput(position_souris):
                    pygame.quit()
                    sys.exit()
        
        pygame.display.update()
            
            
        
        