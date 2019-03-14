import pygame
import Ball
import Block
import Paddle

pygame.init()


class Gameplay(object):
    def __init__(self, window, menu, background, paddle_1, paddle_2, rectangle_1, rectangle_2, circle, font,
                 point_sound, winner_sound, game_music):
        self.__window = window
        self.__menu = menu
        self.__background = background
        self.__paddle_1 = paddle_1
        self.__player_1 = None
        self.__paddle_2 = paddle_2
        self.__player_2 = None
        self.__rectangle_1 = rectangle_1
        self.__block_1 = None
        self.__rectangle_2 = rectangle_2
        self.__block_2 = None
        self.__circle = circle
        self.__ball = None
        self.__font = font
        self.__point_sound = point_sound
        self.__winner_sound = winner_sound
        self.__game_music = game_music
        self.__score_1 = None
        self.__score_2 = None

    def redraw_game_window(self):
        self.__window.blit(self.__background, (0, 0))
        self.__window.blit(self.__paddle_1, (self.__player_1.x, self.__player_1.y))
        self.__window.blit(self.__paddle_2, (self.__player_2.x, self.__player_2.y))
        self.__window.blit(self.__rectangle_1, (self.__block_1.x, self.__block_1.y))
        self.__window.blit(self.__rectangle_2, (self.__block_2.x, self.__block_2.y))
        self.__window.blit(self.__circle, (self.__ball.x, self.__ball.y))
        self.__window.blit(self.__score_1, (10, 609))
        self.__window.blit(self.__score_2, (10, 7))
        pygame.display.update()

    def is_hit(self):
        player_hits = False
        # the ball hits the left wall
        if self.__ball.x < 0:
            self.__ball.x_speed = -self.__ball.x_speed

        # the ball hits the right wall
        if self.__ball.x + self.__ball.size > 1048:
            self.__ball.x_speed = -self.__ball.x_speed

        # the ball hits the obstacle No. 1 from above
        if self.__block_1.y <= self.__ball.y + self.__ball.size < self.__block_1.y + self.__block_1.height \
                and self.__ball.x + self.__ball.size > self.__block_1.x and self.__ball.x < self.__block_1.x + \
                self.__block_1.width:
            self.__ball.y_speed = -self.__ball.y_speed

        # the ball hits the obstacle No. 2 from above
        if self.__block_2.y <= self.__ball.y + self.__ball.size < self.__block_2.y + self.__block_2.height \
                and self.__ball.x + self.__ball.size > self.__block_2.x and self.__ball.x < self.__block_2.x + \
                self.__block_2.width:
            self.__ball.y_speed = -self.__ball.y_speed

        # The ball hits the obstacle No. 1 from the bottom
        if self.__block_1.y + self.__block_1.height >= self.__ball.y > self.__block_1.y \
                and self.__ball.x + self.__ball.size > self.__block_1.x and self.__ball.x < self.__block_1.x + \
                self.__block_1.width:
            self.__ball.y_speed = -self.__ball.y_speed

        # The ball hits the obstacle No. 2 from the bottom
        if self.__block_2.y + self.__block_2.height >= self.__ball.y > self.__block_2.y \
                and self.__ball.x + self.__ball.size > self.__block_2.x and self.__ball.x < self.__block_2.x + \
                self.__block_2.width:
            self.__ball.y_speed = -self.__ball.y_speed

        # The ball hits the right side of obstacle No. 1
        if self.__block_1.x + self.__block_1.width >= self.__ball.x > self.__block_1.x \
                and self.__ball.y + self.__ball.size >= self.__block_1.y and self.__ball.y <= self.__block_1.y + \
                self.__block_1.height:
            self.__ball.x_speed = -self.__ball.x_speed

        # The ball hits the right side of obstacle No. 2
        if self.__block_2.x + self.__block_2.width >= self.__ball.x > self.__block_2.x \
                and self.__ball.y + self.__ball.size >= self.__block_2.y and self.__ball.y <= self.__block_2.y + \
                self.__block_2.height:
            self.__ball.x_speed = -self.__ball.x_speed

        # The ball hits the left side of obstacle No. 1
        if self.__block_1.x <= self.__ball.x + self.__ball.size < self.__block_1.x + self.__block_1.width \
                and self.__ball.y + self.__ball.size >= self.__block_1.y and self.__ball.y <= self.__block_1.y + \
                self.__block_1.height:
            self.__ball.x_speed = -self.__ball.x_speed

        # The ball hits the left side of obstacle No. 2
        if self.__block_2.x <= self.__ball.x + self.__ball.size < self.__block_2.x + self.__block_2.width \
                and self.__ball.y + self.__ball.size >= self.__block_2.y and self.__ball.y <= self.__block_2.y + \
                self.__block_2.height:
            self.__ball.x_speed = -self.__ball.x_speed

        # The ball hits the paddle No. 1 from the top
        if self.__player_1.y <= self.__ball.y + self.__ball.size < self.__player_1.y + self.__player_1.height \
                and self.__ball.x + self.__ball.size > self.__player_1.x and self.__ball.x < self.__player_1.x + \
                self.__player_1.width:
            self.__ball.y_speed = -self.__ball.y_speed
            player_hits = True

        # The ball hits the left side of the paddle No. 1
        if self.__player_1.x <= self.__ball.x + self.__ball.size < self.__player_1.x + self.__player_1.width \
                and self.__ball.y + self.__ball.size >= self.__player_1.y and self.__ball.y < self.__player_1.y + \
                self.__player_1.height:
            self.__ball.x_speed = -self.__ball.x_speed
            player_hits = True

        # The ball hits the right side of the paddle No. 1
        if self.__player_1.x + self.__player_1.width >= self.__ball.x > self.__player_1.x \
                and self.__ball.y + self.__ball.size >= self.__player_1.y and self.__ball.y < self.__player_1.y + \
                self.__player_1.height:
            self.__ball.x_speed = -self.__ball.x_speed
            player_hits = True

        # The ball hits the paddle No. 2 from the bottom
        if self.__player_2.y + self.__player_2.height >= self.__ball.y > self.__player_2.y \
                and self.__ball.x + self.__ball.size > self.__player_2.x and self.__ball.x < self.__player_2.x + \
                self.__player_2.width:
            self.__ball.y_speed = -self.__ball.y_speed
            player_hits = True

        # The ball hits the left side of the paddle No. 2
        if self.__player_2.x <= self.__ball.x + self.__ball.size < self.__player_2.x + self.__player_2.width \
                and self.__ball.y > self.__player_2.y and self.__ball.y + self.__ball.size <= self.__player_2.y + \
                self.__player_2.height:
            self.__ball.x_speed = -self.__ball.x_speed
            player_hits = True

        # The ball hits the right side of the paddle No. 2
        if self.__player_2.x + self.__player_2.width >= self.__ball.x > self.__player_2.x \
                and self.__ball.y > self.__player_2.y and self.__ball.y + self.__ball.size <= self.__player_2.y + \
                self.__player_2.height:
            self.__ball.x_speed = -self.__ball.x_speed
            player_hits = True

        if player_hits:
            self.faster()

    def faster(self):
        if abs(self.__ball.x_speed) < 8:
            if self.__ball.x_speed > 0:
                self.__ball.x_speed += 1
            else:
                self.__ball.x_speed -= 1

            if self.__ball.y_speed > 0:
                self.__ball.y_speed += 1
            else:
                self.__ball.y_speed -= 1

    def play_game(self):
        pygame.mixer.music.play(-1)
        run = True
        while run:
            pygame.time.delay(100)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            self.__window.blit(self.__menu, (0, 0))
            pygame.display.update()

            keys = pygame.key.get_pressed()

            if keys[pygame.K_2] or keys[pygame.K_KP2]:
                run = False
            if keys[pygame.K_1] or keys[pygame.K_KP1]:
                self.__player_1 = Paddle.Paddle(455, 610, 138, 19)
                self.__player_2 = Paddle.Paddle(455, 0, 138, 19)
                self.__block_1 = Block.Block(242, 269, 160, 91)
                self.__block_2 = Block.Block(646, 269, 160, 91)
                self.__ball = Ball.Ball(509, 300, 30)

                game = True
                while game:
                    self.__score_1 = self.__font.render("PLAYER 1 Score: " + str(self.__player_1.score), 1, (0, 0, 255))
                    self.__score_2 = self.__font.render("PLAYER 2 Score: " + str(self.__player_2.score), 1, (0, 0, 255))

                    if self.__player_1.score == 10 or self.__player_2.score == 10:
                        pygame.mixer.music.stop()
                        self.__winner_sound.play()
                        finish_font = pygame.font.SysFont("arial", 100, True)
                        if self.__player_1.score > self.__player_2.score:
                            finish = finish_font.render("PLAYER 1 WIN !!!", 1, (237, 156, 5))
                        else:
                            finish = finish_font.render("PLAYER 2 WIN !!!", 1, (237, 156, 5))
                        text_rect = finish.get_rect(center=(1048 / 2, 629 / 2))
                        self.__window.blit(self.__background, (0, 0))
                        self.__window.blit(self.__score_1, (10, 609))
                        self.__window.blit(self.__score_2, (10, 7))
                        self.__window.blit(finish, text_rect)
                        pygame.display.update()
                        pygame.time.wait(13000)
                        self.play_game()

                    pygame.time.delay(1)
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            run = False
                            game = False

                    keys_1 = pygame.key.get_pressed()
                    keys_2 = pygame.key.get_pressed()

                    if keys_1[pygame.K_LEFT] and self.__player_1.x > 5:
                        self.__player_1.x -= self.__player_1.speed
                    elif keys_1[pygame.K_RIGHT] and self.__player_1.x < 1048 - 10 - self.__player_1.width:
                        self.__player_1.x += self.__player_1.speed

                    if keys_2[pygame.K_a] and self.__player_2.x > 5:
                        self.__player_2.x -= self.__player_2.speed
                    elif keys_2[pygame.K_d] and self.__player_2.x < 1048 - 10 - self.__player_2.width:
                        self.__player_2.x += self.__player_2.speed

                    self.is_hit()

                    # player_2 scores a point
                    if self.__ball.y + self.__ball.size > 629:
                        self.__point_sound.play()
                        self.__player_2.score += 1
                        self.__ball.x = 509
                        self.__ball.y = 300
                        self.__ball.x_speed = 2
                        self.__ball.y_speed = -2
                        self.__player_1.x = 455
                        self.__player_2.x = 455
                        pygame.time.delay(500)

                    # player_1 scores a point
                    if self.__ball.y < 0:
                        self.__point_sound.play()
                        self.__player_1.score += 1
                        self.__ball.x = 509
                        self.__ball.y = 300
                        self.__ball.x_speed = 2
                        self.__ball.y_speed = 2
                        self.__player_1.x = 455
                        self.__player_2.x = 455
                        pygame.time.wait(500)

                    self.__ball.x += self.__ball.x_speed
                    self.__ball.y += self.__ball.y_speed

                    self.redraw_game_window()

        exit()
