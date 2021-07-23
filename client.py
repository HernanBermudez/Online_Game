import pygame
from network import Network
from player import Player

width = 500
height = 500
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")

def redraw_window(win, player, player2):
    win.fill('white')
    player.draw(win)
    player2.draw(win)
    pygame.display.update()

def main():
    run = True
    n = Network()
    player = n.get_p()

    clock = pygame.time.Clock()
    while run:
        clock.tick(60)
        player2 = n.send(player)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.QUIT()

        player.move()
        redraw_window(win, player, player2)

main()