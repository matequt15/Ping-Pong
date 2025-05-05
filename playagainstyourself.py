def playagainstyour_self():

    import pygame
    import random
    import time

    pygame.init()
    pygame.mouse.set_visible(False)

    win_width = 1100
    win_height = 1000
    screen = pygame.display.set_mode((win_width, win_height))

    bg_image = pygame.transform.scale(pygame.image.load("foldedtable.png"), (win_width, win_height))
    bg_color = (0, 0, 0)
    sound = pygame.mixer.Sound("pingpong.wav")

    table_top_left_x, table_top_left_y = 192, 125
    table_top_mid_x, table_top_mid_y = 558, 125
    table_top_right_x, table_top_right_y = 919, 125

    table_bottom_left_x, table_bottom_mid_y = 59, 533
    table_bottom_mid_x, table_bottom_mid_y = 554, 533
    table_bottom_right_x, table_bottom_right_y = 1054, 533
    #(198, 393), (918, 393) y = 279



    text_font = pygame.font.Font(None, 60)

    def get_x_bounds(y):
        top_y = table_top_left_y
        bottom_y = table_bottom_mid_y

        top_left_x = table_top_mid_x - 120
        top_right_x = table_top_mid_x + 120

        bottom_left_x = table_bottom_left_x
        bottom_right_x = table_bottom_right_x

        percent = (y - top_y) / (bottom_y - top_y)

        left_x = top_left_x + percent * (bottom_left_x - top_left_x)
        right_x = top_right_x + percent * (bottom_right_x - top_right_x)

        return int(left_x), int(right_x)

    class Sprite:
        def __init__(self, x, y, width, height, image):
            self.racket = pygame.Rect(x, y, width, height)
            self.racket_image = pygame.transform.scale(pygame.image.load(image), (width, height))

        def collide(self, other):
            return self.racket.colliderect(other.racket)

    class Player(Sprite):
        def __init__(self, x, y, width, height, speed, image):
            super().__init__(x, y, width, height, image)
            self.speed = speed

        def draw(self):
            screen.blit(self.racket_image, (self.racket.x, self.racket.y))

        def upd_mouse_pos(self):
            mouse_position = pygame.mouse.get_pos()

            if mouse_position[0] < table_top_left_x:
                self.racket.x = table_top_left_x
            elif mouse_position[0] > table_bottom_right_x - self.racket.width:
                self.racket.x = table_bottom_right_x - self.racket.width
            else:
                self.racket.x = mouse_position[0]

            if mouse_position[1] < table_top_left_y:
                self.racket.y = table_top_left_y
            elif mouse_position[1] > table_bottom_right_y - self.racket.height:
                self.racket.y = table_bottom_right_y - self.racket.height
            else:
                self.racket.y = mouse_position[1]

    class Ball(Sprite):
        def __init__(self, x, y, width, height, speed, image):
            super().__init__(x, y, width, height, image)
            self.dx, self.dy = speed, speed

        def appear_on_screen(self):
            screen.blit(self.racket_image, (self.racket.x, self.racket.y))

        def move(self):
            self.racket.x += self.dx
            self.racket.y += self.dy

            left_bound, right_bound = get_x_bounds(self.racket.y)

            if self.racket.x <= left_bound:
                self.racket.x = left_bound
                self.dx = -self.dx

            elif self.racket.x >= right_bound - self.racket.width:
                self.racket.x = right_bound - self.racket.width
                self.dx = -self.dx

    class Rackets(Player):
        def __init__(self, x, y, width, height, speed, image):  
            super().__init__(x, y, width, height, speed, image)

        def random_loc(self):
            self.racket.x = random.randint(395, 765 - self.racket.width)
            min_y = table_top_left_y
            max_y = table_top_left_y + 55

            if self.racket.height >= (max_y - min_y):
                self.racket.y = min_y
            else:
                self.racket.y = random.randint(min_y, max_y - self.racket.height)





    def print_info():
        score_txt = text_font.render(f"Score: {score}", True, (0, 0, 0))
        screen.blit(score_txt, (50, 30))


    ball_image = Ball((table_top_left_x + table_bottom_right_x) // 2,
                        (table_top_left_y + table_bottom_right_y) // 2,
                        30, 30, 10, "ball.png")

    player = Player(550, 550, 100, 100, 10, "racket.png")



    score = 0



    game_running = True
    while game_running:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                game_running = False

        screen.fill(bg_color)
        screen.blit(bg_image, (0, 0))

        ball_image.appear_on_screen()
        ball_image.move()


        player.upd_mouse_pos()
        player.draw()

        if ball_image.racket.y <= random.randint(128, 279):
            ball_image.dy = abs(ball_image.dy)  
            score += 1



        if player.collide(ball_image):
            ball_image.dy = -abs(ball_image.dy)
            sound.play()

        if ball_image.racket.y >= 581:
            ball_image.dy = -abs(ball_image.dy)
            score -= score

        



    
        key = pygame.key.get_pressed()
        if key[pygame.K_ESCAPE]:
            game_running = False


        print_info()
        pygame.display.update()
        pygame.time.Clock().tick(60)
