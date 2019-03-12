import pygame, Paddle, Block, Ball
pygame.init()


window = pygame.display.set_mode((1048,629))

pygame.display.set_caption("MyTennisGame")

menu = pygame.image.load('Menu.png')
background = pygame.image.load('Background.png')
paddle_1 = pygame.image.load('Paddle.png')
paddle_2 = pygame.image.load('Paddle.png')
rectangle_1 = pygame.image.load('Block.png')
rectangle_2 = pygame.image.load('Block.png')
circle = pygame.image.load('Ball.png')

font = pygame.font.SysFont("comicsans", 20, True)

def redrawGameWindow(player_1, player_2, block_1, block_2, ball, score_1, score_2):
    window.blit(background, (0, 0))
    window.blit(paddle_1, (player_1.x, player_1.y))
    window.blit(paddle_2, (player_2.x, player_2.y))
    window.blit(rectangle_1, (block_1.x, block_1.y))
    window.blit(rectangle_2, (block_2.x, block_2.y))
    window.blit(circle, (ball.x, ball.y))
    window.blit(score_1, (10, 609))
    window.blit(score_2, (10, 7))
    pygame.display.update()


def main():
    run = True
    while (run):
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        window.blit(menu, (0, 0))
        pygame.display.update()

        keys = pygame.key.get_pressed()

        if keys[pygame.K_2] or keys[pygame.K_KP2]:
            run = False
        if keys[pygame.K_1] or keys[pygame.K_KP1]:
            player_1 = Paddle.Paddle(455, 610, 138, 19)
            player_2 = Paddle.Paddle(455, 0, 138, 19)
            block_1 = Block.Block(242, 269, 160, 91)
            block_2 = Block.Block(646, 269, 160, 91)
            ball = Ball.Ball(509, 300, 30)

            game = True
            while (game):
                score_1 = font.render("PLAYER 1 Score: " + str(player_1.score), 1, (0, 0, 255))
                score_2 = font.render("PLAYER 2 Score: " + str(player_2.score), 1, (0, 0, 255))

                if player_1.score == 10 or player_2.score == 10:
                    finishFont = pygame.font.SysFont("arial", 100, True)
                    if player_1.score > player_2.score:
                        finish = finishFont.render("PLAYER 1 WIN !!!", 1, (237, 156, 5))
                    else:
                        finish = finishFont.render("PLAYER 2 WIN !!!", 1, (237, 156, 5))
                    text_rect = finish.get_rect(center=(1048 / 2, 629 / 2))
                    window.blit(background, (0, 0))
                    window.blit(score_1, (10, 609))
                    window.blit(score_2, (10, 7))
                    window.blit(finish, text_rect)
                    pygame.display.update()
                    pygame.time.wait(5000)
                    break

                pygame.time.delay(1)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False
                        game = False

                keys_1 = pygame.key.get_pressed()
                keys_2 = pygame.key.get_pressed()

                if keys_1[pygame.K_LEFT] and player_1.x > 5:
                    player_1.x -= player_1.speed
                elif keys_1[pygame.K_RIGHT] and player_1.x < 1048 - 10 - player_1.width:
                    player_1.x += player_1.speed

                if keys_2[pygame.K_a] and player_2.x > 5:
                    player_2.x -= player_2.speed
                elif keys_2[pygame.K_d] and player_2.x < 1048 - 10 - player_2.width:
                    player_2.x += player_2.speed

                # the ball hits the left wall
                if ball.x < 0:
                    ball.x_speed = -ball.x_speed

                # the ball hits the right wall
                if ball.x + ball.size > 1048:
                    ball.x_speed = -ball.x_speed

                # the ball hits the obstacle No. 1 from above
                if ball.y + ball.size >= block_1.y and ball.y + ball.size < block_1.y + block_1.height \
                        and ball.x + ball.size > block_1.x and ball.x < block_1.x + block_1.width:
                    ball.y_speed = -ball.y_speed

                # the ball hits the obstacle No. 2 from above
                if ball.y + ball.size >= block_2.y and ball.y + ball.size < block_2.y + block_2.height \
                        and ball.x + ball.size > block_2.x and ball.x < block_2.x + block_2.width:
                    ball.y_speed = -ball.y_speed

                # The ball hits the obstacle No. 1 from the bottom
                if ball.y <= block_1.y + block_1.height and ball.y > block_1.y \
                        and ball.x + ball.size > block_1.x and ball.x < block_1.x + block_1.width:
                    ball.y_speed = -ball.y_speed

                # The ball hits the obstacle No. 2 from the bottom
                if ball.y <= block_2.y + block_2.height and ball.y > block_2.y \
                        and ball.x + ball.size > block_2.x and ball.x < block_2.x + block_2.width:
                    ball.y_speed = -ball.y_speed

                # The ball hits the right side of obstacle No. 1
                if ball.x <= block_1.x + block_1.width and ball.x > block_1.x \
                        and ball.y + ball.size >= block_1.y and ball.y <= block_1.y + block_1.height:
                    ball.x_speed = -ball.x_speed

                # The ball hits the right side of obstacle No. 2
                if ball.x <= block_2.x + block_2.width and ball.x > block_2.x \
                        and ball.y + ball.size >= block_2.y and ball.y <= block_2.y + block_2.height:
                    ball.x_speed = -ball.x_speed

                # The ball hits the left side of obstacle No. 1
                if ball.x + ball.size >= block_1.x and ball.x + ball.size < block_1.x + block_1.width \
                        and ball.y + ball.size >= block_1.y and ball.y <= block_1.y + block_1.height:
                    ball.x_speed = -ball.x_speed

                # The ball hits the left side of obstacle No. 2
                if ball.x + ball.size >= block_2.x and ball.x + ball.size < block_2.x + block_2.width \
                        and ball.y + ball.size >= block_2.y and ball.y <= block_2.y + block_2.height:
                    ball.x_speed = -ball.x_speed

                # The ball hits the paddle No. 1 from the top
                if ball.y + ball.size >= player_1.y and ball.y + ball.size < player_1.y + player_1.height \
                        and ball.x + ball.size > player_1.x and ball.x < player_1.x + player_1.width:
                    ball.y_speed = -ball.y_speed

                # The ball hits the left side of the paddle No. 1
                if ball.x + ball.size >= player_1.x and ball.x + ball.size < player_1.x + player_1.width \
                        and ball.y + ball.size >= player_1.y and ball.y < player_1.y + player_1.height:
                    ball.x_speed = -ball.x_speed

                # The ball hits the right side of the paddle No. 1
                if ball.x <= player_1.x + player_1.width and ball.x > player_1.x \
                        and ball.y + ball.size >= player_1.y and ball.y < player_1.y + player_1.height:
                    ball.x_speed = -ball.x_speed

                # The ball hits the paddle No. 2 from the bottom
                if ball.y <= player_2.y + player_2.height and ball.y > player_2.y \
                        and ball.x + ball.size > player_2.x and ball.x < player_2.x + player_2.width:
                    ball.y_speed = -ball.y_speed

                # The ball hits the left side of the paddle No. 2
                if ball.x + ball.size >= player_2.x and ball.x + ball.size < player_2.x + player_2.width \
                        and ball.y > player_2.y and ball.y + ball.size <= player_2.y + player_2.height:
                    ball.x_speed = -ball.x_speed

                # The ball hits the right side of the paddle No. 2
                if ball.x <= player_2.x + player_2.width and ball.x > player_2.x \
                        and ball.y > player_2.y and ball.y + ball.size <= player_2.y + player_2.height:
                    ball.x_speed = -ball.x_speed

                # player_2 scores a point
                if ball.y + ball.size > 629:
                    player_2.score += 1
                    ball.x = 509
                    ball.y = 300
                    ball.x_speed = abs(ball.x_speed)
                    ball.y_speed = -abs(ball.y_speed)
                    player_1.x = 455
                    player_2.x = 455
                    pygame.time.delay(500)

                # player_1 scores a point
                if ball.y < 0:
                    player_1.score += 1
                    ball.x = 509
                    ball.y = 300
                    ball.x_speed = abs(ball.x_speed)
                    ball.y_speed = abs(ball.y_speed)
                    player_1.x = 455
                    player_2.x = 455
                    pygame.time.wait(500)

                ball.x += ball.x_speed
                ball.y += ball.y_speed

                redrawGameWindow(player_1, player_2, block_1, block_2, ball, score_1, score_2)

    pygame.quit()


if __name__ == "__main__":
    main()
