import pygame
import game_board
import global_variables
import enemy


class Runtime:

    def __init__(self):
        pygame.init()
        #test
        # General
        self.clock = pygame.time.Clock()
        self.game_board = game_board.GameBoard()
        self.screen = self.game_board.get_screen
        self.paused = False
        self.difficulty = None
        self.game_state = None
        self.wave = None

        # Enemies
        self.spawn_timer = None
        self.enemy_queue = None
        self.enemy_list = None

        # Player
        self.player_health = None
        self.positions = None

    def setup(self):
        self.difficulty = 1
        self.game_state = 1  # 1 - Main Menu, 2 - Game started, 3 - You lose, 4 - You win
        self.wave = 2 * self.difficulty

        # Enemies
        self.spawn_timer = pygame.time.set_timer(25, 1000)
        self.enemy_queue = []
        self.enemy_list = pygame.sprite.Group()

        # Player
        self.player_health = global_variables.stats_player_health = 10 * self.difficulty

        self.positions = []

    def spawn_enemy(self):
        self.enemy_list.add(enemy.Enemy(1290, 110))

    def setup_wave(self):
        pass

    def you_lose(self):
        # empty towers
        self.enemy_list.empty()
        self.game_state = 3
        # play sound

    def you_win(self):
        pass

    def run(self):
        running = True
        while running:

            # Set the game to 60 FPS
            self.clock.tick(30)

            # Event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    self.positions.append(mouse_pos)
                    print(self.positions)

                    # Game state - Main Menu
                    if self.game_state == 1:
                        button_clicked = self.game_board.click(mouse_pos[0], mouse_pos[1], self.game_state)
                        if button_clicked == 'EASY':
                            self.difficulty = 1
                            self.game_state = 2
                        elif button_clicked == 'NORMAL':
                            self.difficulty = 2
                            self.game_state = 2
                        elif button_clicked == 'HARD':
                            self.difficulty = 3
                            self.game_state = 2

                    # Game state - In game
                    elif self.game_state == 2:
                        button_clicked = self.game_board.click(mouse_pos[0], mouse_pos[1], self.game_state)

                    # Game state - You lose
                    elif self.game_state == 3:
                        button_clicked = self.game_board.click(mouse_pos[0], mouse_pos[1], self.game_state)
                        if button_clicked == 'BACK':
                            self.setup()
                        elif button_clicked == 'RESTART':
                            self.setup()
                            self.game_state = 2

                    # Game state - You win
                    elif self.game_state == 4:
                        button_clicked = self.game_board.click(mouse_pos[0], mouse_pos[1], self.game_state)

                if event.type == pygame.MOUSEMOTION:
                    pass

                if event.type == 25 and len(self.enemy_list) <= self.wave and self.game_state == 2:
                    self.spawn_enemy()

            # Draw the background
            self.game_board.draw(self.game_state)

            # Draw the enemies
            self.enemy_list.update()
            for en in self.enemy_list:
                en.draw(self.screen)

            # Draw the overlay tails

            if global_variables.stats_player_health <= 0:
                self.you_lose()

            # Update game display
            pygame.display.update()
        pygame.quit()


if __name__ == '__main__':
    g = Runtime()
    g.setup()
    g.run()
