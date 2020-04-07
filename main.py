import pygame
import game_board
import global_variables
import enemy
import tower
import time
import random
import effect


class Runtime:
    """
    Main game logic goes here.
    """

    def __init__(self):
        pygame.init()
        pygame.mixer.init()

        # General
        self.clock = pygame.time.Clock()
        self.game_board = None
        self.screen = None
        self.paused = False
        self.difficulty = None
        self.game_state = None
        self.wave = None
        self.timer = None
        self.wave_number = None
        self.wave_level = None
        self.game_settings = None
        self.game_map = None
        self.sound_you_lose = None

        # Enemies
        self.enemy_paths = None
        self.spawn_timer = None
        self.enemy_queue = None
        self.enemy_list = None
        self.enemy_spawn_position_x = None
        self.enemy_spawn_position_y = None

        # Towers
        self.towers_list = None
        self.moving_objects = None
        self.object_being_dragged = None
        self.tower_available_positions = None

        # Player
        self.player_health = None
        self.positions = None
        self.effects_list = None

        self.pos = []

    def setup(self, game_map):
        """
        All variables held here, so the game can be restarted in runtime.
        :param map: int
        :return: None
        """
        self.game_settings = global_variables.game_settings
        self.game_board = game_board.GameBoard(self.game_settings[game_map][0])
        self.screen = self.game_board.get_screen
        pygame.mixer.music.load('assets/sounds/music1.wav')
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.3)
        self.sound_you_lose = pygame.mixer.Sound('assets/sounds/youlose.wav')
        self.difficulty = 1
        self.game_state = 1  # 1 - Main Menu, 2 - Game started, 3 - You lose, 4 - You win
        self.wave = 2 * self.difficulty
        self.wave_number = 0
        self.wave_level = 1
        self.timer = time.time()
        self.game_map = game_map

        # Enemies
        pygame.time.set_timer(25, 1000)
        self.enemy_queue = []
        self.enemy_list = pygame.sprite.Group()
        self.enemy_spawn_position_x = global_variables.game_settings[game_map][2][0][0]
        self.enemy_spawn_position_y = global_variables.game_settings[game_map][2][0][1]

        # Towers
        self.towers_list = pygame.sprite.Group()
        self.moving_objects = pygame.sprite.Group()
        self.tower_available_positions = global_variables.game_settings[game_map][1]

        # Player
        self.player_health = global_variables.stats_player_health = 10 * self.difficulty

        # Effects
        pygame.time.set_timer(26, 2000)
        self.effects_list = pygame.sprite.Group()
        self.effects_list.add(
            effect.Effect(600, 400, 'FIRE')
        )

        self.positions = []

    def spawn_enemy(self):
        """
        Spawn new enemy and add it to the list.
        :return: None
        """
        self.enemy_list.add(enemy.Enemy(self.enemy_spawn_position_x, self.enemy_spawn_position_y, (random.randint(5, 20)) * self.wave_level, self.game_map))
        if self.wave_number >= self.wave:
            self.wave_number = 0
            self.wave_level += 1
            self.wave *= 1.5
        self.wave_number += 1

    def spawn_effect(self):
        """
        Spawn new effect and add it to the list.
        :return:
        """
        for effct in self.moving_objects:
            effct.set_in_position()
        self.effects_list.add(
            self.moving_objects
        )
        self.object_being_dragged = False
        self.moving_objects.empty()


    def spawn_tower(self):
        """
        Spawn new tower.
        :return: None
        """
        for twr in self.moving_objects:
            twr.set_in_position()
        self.towers_list.add(
            self.moving_objects
        )
        self.object_being_dragged = False
        self.moving_objects.empty()

    def drag_tower(self, name):
        """
        Spawn a tower from the buy menu
        :return: None
        """
        x, y = pygame.mouse.get_pos()
        obj = self.buy_tower(x, y, name)
        if obj:
            self.moving_objects.add(obj)
            self.object_being_dragged = True
            self.game_board.close_open_menus()

    def setup_wave(self):
        pass

    def you_lose(self):
        # empty towers
        self.enemy_list.empty()
        self.game_state = 3
        pygame.mixer.Sound(self.sound_you_lose)

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

                    if event.button == 1:
                        # First check if any tower is currently being drag on the screen
                        if self.object_being_dragged:
                            for obj in self.moving_objects:

                                # Check the tower dragged position against the map specific tower points/
                                for point in self.tower_available_positions:

                                    # If the point is not already taken by another tower.
                                    if obj.rect.collidepoint(point) and not pygame.sprite.spritecollide(obj, self.towers_list, False):
                                        self.spawn_tower()

                        else:
                            mouse_pos = pygame.mouse.get_pos()


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
                                self.pos.append(mouse_pos)
                                print(self.pos)

                                button_clicked = self.game_board.click(mouse_pos[0], mouse_pos[1], self.game_state)
                                print(button_clicked)
                                for twr in self.towers_list:
                                    twr.click(mouse_pos[0], mouse_pos[1])

                                if button_clicked is None:
                                    self.game_board.close_open_menus()
                                elif button_clicked:
                                    self.drag_tower(button_clicked)

                            # Game state - You lose
                            elif self.game_state == 3:
                                button_clicked = self.game_board.click(mouse_pos[0], mouse_pos[1], self.game_state)
                                if button_clicked == 'BACK':
                                    self.setup(random.randint(0, 4))
                                elif button_clicked == 'RESTART':
                                    self.setup(random.randint(0, 4))
                                    self.game_state = 2

                            # Game state - You win
                            elif self.game_state == 4:
                                button_clicked = self.game_board.click(mouse_pos[0], mouse_pos[1], self.game_state)

                    else:  # If mouse right button is pressed
                        # Close all opened menus
                        self.game_board.close_open_menus()
                        # Stop dragging sprites
                        self.object_being_dragged = False

                # Spawn events
                if event.type == 25 and len(self.enemy_list) <= self.wave and self.game_state == 2:
                    self.spawn_enemy()

            if global_variables.stats_player_health <= 0:
                self.you_lose()

            # Enemy in range of tower
            for twr in self.towers_list:
                enemies = pygame.sprite.spritecollide(twr, self.enemy_list, False, pygame.sprite.collide_circle)
                if enemies:
                    for enmy in enemies:
                        twr.set_enemy_in_range(True)
                        enmy.take_damage(twr.damage, twr.rate)
                        if twr.rect.x > enmy.rect.x:
                            twr.set_archer_flipped(True)
                        else:
                            twr.set_archer_flipped(False)
                else:
                    twr.set_enemy_in_range(False)

            self.draw()
        pygame.quit()

    def draw(self):
        """
        All drawing logic goes here.
        :return:
        """
        # Draw the background
        self.game_board.draw(self.game_state)

        # Draw the enemies
        for en in self.enemy_list:
            en.draw(self.screen, self.game_state)

        # Draw the effects
        for effct in self.effects_list:
            effct.draw(self.screen, self.game_state)

        # Draws the towers
        for twr in self.towers_list:
            twr.draw(self.screen, self.game_state)

        # Logic when a tower is being dragged with the mouse
        if self.object_being_dragged:
            for obj in self.moving_objects:
                for point in self.tower_available_positions:
                    if obj.rect.collidepoint(point) and not pygame.sprite.spritecollide(obj, self.towers_list, False):
                        circle_surface_green = pygame.Surface((64 * 2, 64 * 2), pygame.SRCALPHA, 32)
                        pygame.draw.circle(circle_surface_green, (0, 128, 0, 128), (64, 64), 64, 0)
                        self.screen.blit(circle_surface_green, (pygame.mouse.get_pos()[0] - 68, pygame.mouse.get_pos()[1] - 64))
                obj.drag(pygame.mouse.get_pos())
                obj.draw(self.screen, self.game_state)

        # Draw the tower's buy menu
        self.game_board.draw_tower_menus(self.game_state)

        # Update game display
        pygame.display.update()

    def buy_tower(self, x, y, name):
        if name == 'BUY_ARCHER_TOWER_1':
            return tower.TowerArcher1(x, y, self.game_map)
        elif name == 'BUY_ARCHER_TOWER_2':
            return tower.TowerArcher2(x, y, self.game_map)
        elif name == 'BUY_ARCHER_TOWER_3':
            return tower.TowerArcher3(x, y, self.game_map)
        elif name == 'BUY_ARCHER_TOWER_4':
            return tower.TowerArcher4(x, y, self.game_map)
        elif name == 'BUY_MAGIC_TOWER_1':
            return tower.TowerMagic1(x, y, self.game_map)
        elif name == 'BUY_MAGIC_TOWER_2':
            return tower.TowerMagic2(x, y, self.game_map)
        elif name == 'BUY_MAGIC_TOWER_3':
            return tower.TowerMagic3(x, y, self.game_map)
        elif name == 'BUY_MAGIC_TOWER_4':
            return tower.TowerMagic4(x, y, self.game_map)
        elif name == 'BUY_STONE_TOWER_1':
            return tower.TowerStone1(x, y, self.game_map)
        elif name == 'BUY_STONE_TOWER_2':
            return tower.TowerStone2(x, y, self.game_map)
        elif name == 'BUY_STONE_TOWER_3':
            return tower.TowerStone3(x, y, self.game_map)
        elif name == 'BUY_STONE_TOWER_4':
            return tower.TowerStone4(x, y, self.game_map)
        elif name == 'BUY_SUPPORT_TOWER_1':
            return tower.TowerSupport1(x, y, self.game_map)
        elif name == 'BUY_SUPPORT_TOWER_2':
            return tower.TowerSupport2(x, y, self.game_map)
        elif name == 'BUY_SUPPORT_TOWER_3':
            return tower.TowerSupport3(x, y, self.game_map)
        elif name == 'BUY_SUPPORT_TOWER_4':
            return tower.TowerSupport4(x, y, self.game_map)
        elif name == 'BUY_FREEZE':
            return effect.Effect(x, y, 'FREEZE')
        elif name == 'BUY_FIRE':
            return effect.Effect(x, y, 'FIRE')
        elif name == 'BUY_RAIN':
            return effect.Effect(x, y, 'RAIN')
        elif name == 'BUY_STONES':
            return effect.Effect(x, y, 'STONES')
        else:
            return False


if __name__ == '__main__':
    g = Runtime()
    g.setup(0)
    g.run()

"""
TO DO 
- DONE -> Archers shoot animation
- Moneys
- DONE -> Tower's placement availability
- DONE -> Tower's descriptions
- Auto level up
- Effects
"""
