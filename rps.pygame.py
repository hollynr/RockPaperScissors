#Holly Reidy, Rock Paper Scissors game, Feb 15 2023


import pygame
import random
#import time
pygame.init()


#variables:
BGCOLOR = "light blue"
player_1 = ""
mode = ""
tie = 0
win = 0
loss = 0



#loading assets:
rock_image = pygame.image.load("assets/Rock.png")
rock_image = pygame.transform.scale(rock_image, (100, 100))
paper_image = pygame.image.load("assets/Paper.png")
paper_image = pygame.transform.scale(paper_image, (100, 100))
scissors_image = pygame.image.load("assets/Scissors.png")
scissors_image = pygame.transform.scale(scissors_image, (100, 100))
lizard_image = pygame.image.load("assets/Lizard.png")
lizard_image = pygame.transform.scale(lizard_image, (100, 100))
spock_image = pygame.image.load("assets/Spock.png")
spock_image = pygame.transform.scale(spock_image, (100, 100))





#functions:
def printing_text(text, x, y, p):
        set_my_text = pygame.font.SysFont("arial", p)
        textSurface = set_my_text.render(text, True, "black")
        screen.blit(textSurface, (x, y))



#initialize screen
screen = pygame.display.set_mode([1000, 1000])


running = True
while running:

        # check for events / get input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = event.pos
                    if rock.collidepoint(mouse_x, mouse_y):
                            player_1 = 'Rock'
                    if paper.collidepoint(mouse_x, mouse_y):
                            player_1 = 'Paper'
                    if scissors.collidepoint(mouse_x, mouse_y):
                            player_1 = 'Scissors'
                    if mode == "rpsls":
                            if lizard.collidepoint(mouse_x, mouse_y):
                                    player_1 = 'Lizard'
                            if spock.collidepoint(mouse_x, mouse_y):
                                    player_1 = 'Spock'
            if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                            mode = "Classic rps"
                    if event.key == pygame.K_2:
                            mode = "rpsls"
            
        # do stuff / proccess input
        screen.fill(BGCOLOR)
        printing_text("Type 1 for Classic Rock, Paper, Scissors", 50, 200, 50)
        printing_text("Type 2 for Lizard, Spock", 200, 250, 50)
        choices = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']




        if mode == "Classic rps":
                screen.fill(BGCOLOR)
                printing_text("type 1 or 2 to toggle modes", 350, 20, 25)
                player_2 = choices[random.randint(0,2)]
                rock = screen.blit(rock_image, (250,200))
                paper = screen.blit(paper_image, (450, 200))
                scissors = screen.blit(scissors_image, (650, 200))
        if mode == "rpsls":
                screen.fill(BGCOLOR)
                printing_text("type 1 or 2 to toggle modes", 350, 20, 25)
                rock = screen.blit(rock_image, (250,200))
                paper = screen.blit(paper_image, (450, 200))
                scissors = screen.blit(scissors_image, (650, 200))
                player_2 = choices[random.randint(0,4)]
                lizard = screen.blit(lizard_image, (50, 200))
                spock = screen.blit(spock_image, (850, 200))


        
        printing_text(f"ties: {tie} losses: {loss} wins: {win}", 200, 800, 50)
        
        if player_1 != "":

                printing_text(f"You chose {player_1}", 300, 500, 50)
                printing_text(f"Your opponent chose {player_2}", 175, 600, 50)
                if player_1 == player_2:
                       printing_text("You tied", 400, 700, 50)
                       tie += 1
        
                elif player_1 == 'Rock':
                        if player_2 == 'Scissors' or player_2 == 'Lizard':
                                printing_text("You won!", 420, 700, 50)
                                win += 1
                        elif player_2 == "Paper" or player_2 == 'Spock':
                                printing_text("You lost!", 420, 700, 50)
                                loss += 1
                elif player_1 == 'Paper':
                        if player_2 == 'Rock' or player_2 == 'Spock':
                                printing_text('You won!', 420, 700, 50)
                                win += 1
                        elif player_2 == 'Scissors' or player_2 == 'Lizard':
                                printing_text('You lost!', 420, 700, 50)
                                loss += 1
                elif player_1 == 'Scissors':
                        if player_2 == 'Paper' or player_2 == 'Lizard':
                                printing_text("You won!", 420, 700, 50)
                                win += 1
                        elif player_2 == 'Rock' or player_2 == 'Spock':
                                printing_text("You lost!", 420, 700, 50)
                                loss += 1
                elif player_1 == "Lizard":
                        if player_2 == "Paper" or player_2 == 'Spock':
                                printing_text("You won!", 420, 700, 50)
                                win += 1
                        elif player_2 == 'Rock' or player_2 == 'Scissors':
                                printing_text("You lost!", 420, 700, 50)
                                loss += 1
                elif player_1 == "Spock":
                        if player_2 == "Scissors" or player_2 == 'Rock':
                                printing_text("You won!", 420, 700, 50)
                                win += 1
                        elif player_2 == 'Lizard' or player_2 == 'Paper':
                                printing_text("You lost!", 420, 700, 50)
                                loss += 1

                


                pygame.display.update()
                pygame.time.wait(1500)
                player_1 = ""




            

        
        #pygame.draw.circle(screen, "red", (400,300), 100)
    
        # draw screen

        pygame.display.flip()

pygame.quit()
