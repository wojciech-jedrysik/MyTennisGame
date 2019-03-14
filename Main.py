import pygame
import Gameplay

pygame.init()


window = pygame.display.set_mode((1048, 629))
pygame.display.set_caption("MyTennisGame")
menu = pygame.image.load('Menu.png')
background = pygame.image.load('Background.png')
paddle_1 = pygame.image.load('Paddle.png')
paddle_2 = pygame.image.load('Paddle.png')
rectangle_1 = pygame.image.load('Block.png')
rectangle_2 = pygame.image.load('Block.png')
circle = pygame.image.load('Ball.png')
font = pygame.font.SysFont("comicsans", 20, True)
point_sound = pygame.mixer.Sound('PointSound.ogg')
winner_sound = pygame.mixer.Sound('WinnerSound.flac')
game_music = pygame.mixer.music.load('GameMusic.mp3')


def main():
    game = Gameplay.Gameplay(window, menu, background, paddle_1, paddle_2, rectangle_1, rectangle_2, circle, font,
                             point_sound, winner_sound, game_music)
    game.play_game()


if __name__ == "__main__":
    main()
