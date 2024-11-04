import pygame
import sys
import space_invaders
from button import Button

def get_font(size):
    return pygame.font.Font(None, size)  # Utilise une police par défaut avec la taille spécifiée

def menu():
    menu_on = True
    print("Début Ok")
    
    while menu_on:
        ecran.blit(background, (0,0))
        
        position_souris=pygame.mouse.get_pos()
        
        font = pygame.font.Font("font.ttf", 70)
        
        texte_menu=font.render("Battle War", True, (254, 153, 0))
        positon_texte_menu=texte_menu.get_rect(center=(400,90))
        
        boutton_jouer=Button(image=pygame.image.load("Play Rect.png"), pos=(400,190),
                             text_input="Jouer", font=get_font(60), base_color="#d7fcd4",hovering_color="White")
        boutton_quitter=Button(image=pygame.image.load("Quit Rect.png"), pos=(400,290),
                             text_input="Quitter", font=get_font(60), base_color="#d7fcd4",hovering_color="White")
        
        ecran.blit(texte_menu, positon_texte_menu)
        
        for boutton in [boutton_jouer, boutton_quitter]:
            boutton.changeColor(position_souris)
            boutton.update(ecran)
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if boutton_jouer.checkForInput(position_souris):
                    menu_on = False
                    space_invaders.jeu()
                if boutton_quitter.checkForInput(position_souris):
                    menu_on = False
                    pygame.quit()
                    sys.exit()
        
        pygame.display.update()
            
        pygame.mixer.music.load("Dancing In The Flames Instrumental.mp3")
        pygame.mixer.music.play(loops=3, start=0)
        pygame.mixer.music.set_volume(0.5)
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.mixer.music.stop()
        

pygame.init()
ecran=pygame.display.set_mode((800,600))
pygame.display.set_caption("Menu")
background=pygame.image.load("fondecranm.png")
menu()
        