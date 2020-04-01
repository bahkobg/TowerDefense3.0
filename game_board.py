import pygame
import global_variables


class GameBoard:
    """
    Defines the main screen and background.
    """

    def __init__(self):

        # General
        self.screen = pygame.display.set_mode((1280, 780), pygame.SRCALPHA)

        # Main Menu
        self.main_menu_bg = pygame.transform.scale(pygame.image.load('assets/backgrounds/0/bg.png'), (1280, 780))
        self.main_menu_buttons = pygame.sprite.Group()
        self.main_menu_buttons.add(
            Button(global_variables.menu_new_game[1], 525, 370, 200, 107, 'EASY'),
            Button(global_variables.menu_new_game[6], 525, 482, 200, 107, 'NORMAL'),
            Button(global_variables.menu_new_game[2], 525, 599, 200, 107, 'HARD'),
            Button(global_variables.menu_new_game[10], 346, 50, 540, 180, False),
            Button(global_variables.menu_new_game[8], 120, 610, 80, 80, 'SOUND'),
            Button(global_variables.menu_new_game[3], 30, 610, 80, 80, 'MUSIC'),
            Button(global_variables.menu_new_game[5], 525, 200, 200, 200, 'PLAY')
        )

        # In-Game
        self.in_game_bg = pygame.transform.scale(pygame.image.load('assets/backgrounds/1/bg.png'), (1280, 720))
        self.bottom_menu = pygame.transform.scale(pygame.image.load('assets/menus/gui/0.png'), (1340, 70))
        self.tree = pygame.transform.scale(pygame.image.load('assets/backgrounds/1/tree.png'), (67, 105))
        self.text_stats = pygame.font.SysFont('comicsansms', 28)
        self.bottom_menu_buttons = pygame.sprite.Group()
        self.top_menu_buttons = pygame.sprite.Group()
        self.bottom_menu_buttons.add(
            Button(global_variables.menu_bottom[1], 50, 684, 80, 80, 'PAUSE'),
            Button(global_variables.menu_bottom[2], 140, 684, 80, 80, 'QUICK'),
            Button(global_variables.menu_bottom[3], 230, 684, 80, 80, 'PLAY'),
            Button(global_variables.menu_bottom[4], 410, 684, 80, 80, 'EASY'),
            Button(global_variables.menu_bottom[5], 500, 684, 80, 80, 'EASY'),
            Button(global_variables.menu_bottom[6], 590, 684, 80, 80, 'EASY'),
            Button(global_variables.menu_bottom[7], 680, 684, 80, 80, 'EASY'),
            Button(global_variables.menu_bottom[8], 770, 684, 80, 80, 'MAGIC'),
            Button(global_variables.menu_bottom[9], 860, 684, 80, 80, 'STONE'),
            Button(global_variables.menu_bottom[10], 950, 684, 80, 80, 'SUPPORT'),
            Button(global_variables.menu_bottom[11], 1040, 684, 80, 80, 'ARCHER'),
        )
        self.top_menu_buttons.add(
            Button(global_variables.menu_bottom[16], 20, 20, 140, 160, False),
            Button(global_variables.menu_bottom[14], 35, 40, 35, 35, False),
            Button(global_variables.menu_bottom[15], 35, 85, 35, 35, False),
            Button(global_variables.menu_bottom[12], 35, 130, 35, 35, False),
        )

        # Archer Tower
        self.text_h2 = pygame.font.SysFont('comicsansms', bold=True, size=48)
        self.menu_tower_archer_opened = False
        self.menu_tower_archer = pygame.sprite.Group()
        self.menu_tower_archer.add(
            Button(global_variables.towers_archer[0], 330, 100, 670, 400, False),
            Button(global_variables.towers_archer[2], 370, 170, 125, 140, 'EASY'),
            Button(global_variables.towers_archer[7], 525, 170, 125, 140, 'EASY'),
            Button(global_variables.towers_archer[9], 680, 170, 125, 140, 'EASY'),
            Button(global_variables.towers_archer[11], 835, 170, 125, 140, 'EASY')
        )
        # Magic Tower
        self.menu_tower_magic_opened = False
        self.menu_tower_magic = pygame.sprite.Group()
        self.menu_tower_magic.add(
            Button(global_variables.towers_magic[0], 330, 100, 670, 400, False),
            Button(global_variables.towers_magic[2], 370, 170, 125, 140, 'EASY'),
            Button(global_variables.towers_magic[6], 525, 170, 125, 140, 'EASY'),
            Button(global_variables.towers_magic[11], 680, 170, 125, 140, 'EASY'),
            Button(global_variables.towers_magic[16], 835, 170, 125, 140, 'EASY')
        )
        # Stone Tower
        self.menu_tower_stone_opened = False
        self.menu_tower_stone = pygame.sprite.Group()
        self.menu_tower_stone.add(
            Button(global_variables.towers_stone[0], 330, 100, 670, 400, False),
            Button(global_variables.towers_stone[3], 370, 170, 125, 140, 'EASY'),
            Button(global_variables.towers_stone[6], 525, 170, 125, 140, 'EASY'),
            Button(global_variables.towers_stone[12], 680, 170, 125, 140, 'EASY'),
            Button(global_variables.towers_stone[15], 835, 170, 125, 140, 'EASY')
        )
        # Support Tower
        self.menu_tower_support_opened = False
        self.menu_tower_support = pygame.sprite.Group()
        self.menu_tower_support.add(
            Button(global_variables.towers_support[0], 330, 100, 670, 400, False),
            Button(global_variables.towers_support[3], 370, 170, 125, 140, 'EASY'),
            Button(global_variables.towers_support[6], 525, 170, 125, 140, 'EASY'),
            Button(global_variables.towers_support[12], 680, 170, 125, 140, 'EASY'),
            Button(global_variables.towers_support[15], 835, 170, 125, 140, 'EASY')
        )

        # You Lose
        self.you_lose_buttons = pygame.sprite.Group()
        self.text_you_lose = pygame.font.SysFont('comicsansms', 48)
        self.you_lose_buttons.add(
            Button(global_variables.menu_you_lose[2], 440, 120, 400, 460, False),
            Button(global_variables.menu_you_lose[3], 504, 240, 271, 300, False),
            Button(global_variables.menu_you_lose[4], 535, 120, 200, 82, False),
            Button(global_variables.menu_you_lose[0], 520, 520, 80, 80, 'BACK'),
            Button(global_variables.menu_you_lose[1], 680, 520, 80, 80, 'RESTART')
        )

        # You Win
        self.you_win_buttons = pygame.sprite.Group()
        self.text_you_win = pygame.font.SysFont('comicsansms', 32)
        self.you_win_buttons.add(
            Button(global_variables.menu_you_win[8], 440, 120, 400, 460, False),
            Button(global_variables.menu_you_win[9], 504, 240, 271, 300, False),
            Button(global_variables.menu_you_win[3], 535, 120, 200, 82, False),
            Button(global_variables.menu_you_win[7], 515, 270, 250, 106, False),
            Button(global_variables.menu_you_win[0], 650, 474, 36, 48, False),
            Button(global_variables.menu_you_win[1], 520, 520, 80, 80, 'OPTIONS'),
            Button(global_variables.menu_you_win[2], 680, 520, 80, 80, 'NEXT')
        )

    def draw(self, game_state):
        """
        Draws the main screen.
        :param:game_state -> 1: Main menu,
                             2: Game- Started,
                             3: You lose,
                             4: You win
        :return: None
        """
        if game_state == 1:
            self.screen.blit(self.main_menu_bg, (0, 0))
            self.main_menu_buttons.draw(self.screen)

        elif game_state == 2:
            self.screen.blit(self.in_game_bg, (0, 0))
            self.screen.blit(self.bottom_menu, (-30, 720))
            self.bottom_menu_buttons.draw(self.screen)
            self.top_menu_buttons.draw(self.screen)
            self.screen.blit(self.text_stats.render(str(global_variables.stats_money), True, (247, 187, 31)), (75, 38))
            self.screen.blit(self.text_stats.render(str(global_variables.stats_player_mana), True, (247, 187, 31)),
                             (75, 83))
            self.screen.blit(self.text_stats.render(str(global_variables.stats_player_health), True, (247, 187, 31)),
                             (75, 128))

        elif game_state == 3:
            self.screen.blit(self.main_menu_bg, (0, 0))
            self.you_lose_buttons.draw(self.screen)
            self.screen.blit(self.text_you_lose.render('SORRY :(', True, (247, 187, 31)), (540, 390))
            self.screen.blit(self.text_you_lose.render('You lose', True, (247, 187, 31)), (540, 450))

        elif game_state == 4:
            self.screen.blit(self.main_menu_bg, (0, 0))
            self.you_win_buttons.draw(self.screen)
            self.screen.blit(self.text_you_win.render('Congratulations!', True, (247, 187, 31)), (520, 380))
            self.screen.blit(self.text_you_win.render('Level Complete', True, (247, 187, 31)), (520, 420))
            self.screen.blit(self.text_you_win.render('+' + str(global_variables.stats_money), True, (255, 180, 0)),
                             (570, 470))

    def draw_tower_menus(self, game_state):
        # Draw the menus
        if game_state == 2:
            if self.menu_tower_archer_opened:
                self.menu_tower_archer.draw(self.screen)
                self.screen.blit(self.text_h2.render('Archer Towers:', True, (247, 187, 31)), (470, 100))
            elif self.menu_tower_stone_opened:
                self.menu_tower_stone.draw(self.screen)
                self.screen.blit(self.text_h2.render('Stone Towers:', True, (247, 187, 31)), (470, 100))
            elif self.menu_tower_magic_opened:
                self.menu_tower_magic.draw(self.screen)
                self.screen.blit(self.text_h2.render('Magic Towers:', True, (247, 187, 31)), (470, 100))
            elif self.menu_tower_support_opened:
                self.menu_tower_support.draw(self.screen)
                self.screen.blit(self.text_h2.render('Support Towers:', True, (247, 187, 31)), (470, 100))

    @property
    def get_screen(self):
        """
        Returns the main surface object.
        :return:Surface obj
        """
        return self.screen

    def click(self, x, y, game_state):
        if game_state == 1:
            for sprite in self.main_menu_buttons:
                if sprite.click(x, y):
                    return sprite.button_id
        elif game_state == 2:
            for sprite in self.bottom_menu_buttons:
                if sprite.click(x, y):
                    if sprite.click(x, y) == 'ARCHER':
                        self.close_open_menus()
                        self.menu_tower_archer_opened = True
                        return True
                    elif sprite.click(x, y) == 'MAGIC':
                        self.close_open_menus()
                        self.menu_tower_magic_opened = True
                        return True
                    elif sprite.click(x, y) == 'STONE':
                        self.close_open_menus()
                        self.menu_tower_stone_opened = True
                        return True
                    elif sprite.click(x, y) == 'SUPPORT':
                        self.close_open_menus()
                        self.menu_tower_support_opened = True
                        return True
        elif game_state == 3:
            for sprite in self.you_lose_buttons:
                if sprite.click(x, y):
                    return sprite.button_id
        elif game_state == 4:
            for sprite in self.you_win_buttons:
                if sprite.click(x, y):
                    return sprite.button_id

    def close_open_menus(self):
        self.menu_tower_archer_opened = False
        self.menu_tower_support_opened = False
        self.menu_tower_magic_opened = False
        self.menu_tower_stone_opened = False


class Button(pygame.sprite.Sprite):
    def __init__(self, img, x, y, width, height, button_id):
        pygame.sprite.Sprite.__init__(self)
        self.sound_click = pygame.mixer.Sound('assets/sounds/click.wav')
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.button_id = button_id
        self.image = pygame.transform.scale(img, (self.width, self.height))
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def click(self, x, y):
        if self.rect.collidepoint(x, y):
            if self.button_id:
                pygame.mixer.Sound.play(self.sound_click)
                return self.button_id
            else:
                return False
