import pygame
import sys


pygame.init()

WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Game")


clock = pygame.time.Clock()


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
paddle_speed = 10

player1 = pygame.Rect(10, (HEIGHT - PADDLE_HEIGHT) // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
player2 = pygame.Rect(WIDTH - 20, (HEIGHT - PADDLE_HEIGHT) // 2, PADDLE_WIDTH, PADDLE_HEIGHT)

BALL_SIZE = 20
ball_speed_x, ball_speed_y = 7, 7
ball = pygame.Rect(WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)


player1_score = 0
player2_score = 0
font = pygame.font.Font(None, 74)

def handle_input(keys):
    if keys[pygame.K_w] and player1.top > 0:
        player1.y -= paddle_speed
    if keys[pygame.K_s] and player1.bottom < HEIGHT:
        player1.y += paddle_speed
    if keys[pygame.K_UP] and player2.top > 0:
        player2.y -= paddle_speed
    if keys[pygame.K_DOWN] and player2.bottom < HEIGHT:
        player2.y += paddle_speed

def update_ball():
    global ball_speed_x, ball_speed_y, player1_score, player2_score

    ball.x += ball_speed_x
    ball.y += ball_speed_y

   
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed_y *= -1

 
    if ball.colliderect(player1) or ball.colliderect(player2):
        ball_speed_x *= -1

  
    if ball.left <= 0:
        player2_score += 1
        reset_ball()
    elif ball.right >= WIDTH:
        player1_score += 1
        reset_ball()

def reset_ball():
    global ball_speed_x, ball_speed_y
    ball.x = WIDTH // 2 - BALL_SIZE // 2
    ball.y = HEIGHT // 2 - BALL_SIZE // 2
    ball_speed_x *= -1
    ball_speed_y *= -1

def draw():
    win.fill(BLACK)
    pygame.draw.rect(win, WHITE, player1)
    pygame.draw.rect(win, WHITE, player2)
    pygame.draw.ellipse(win, WHITE, ball)
    pygame.draw.aaline(win, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))

    player1_text = font.render(str(player1_score), True, WHITE)
    win.blit(player1_text, (WIDTH // 4, 20))

    player2_text = font.render(str(player2_score), True, WHITE)
    win.blit(player2_text, (WIDTH * 3 // 4, 20))

    pygame.display.flip()

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        handle_input(keys)
        update_ball()
        draw()
        clock.tick(60)

if __name__ == "__main__":
    main()
