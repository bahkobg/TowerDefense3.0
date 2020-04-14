import pygame
import global_variables


class GameBoard:
    """
    Defines the main screen and background.
    """

    def __init__(self, settings):

        # General
        self.screen = pygame.display.set_mode((1280, 780), pygame.SRCALPHA)
        self.icon = pygame.image.load('assets/icon.png')

        pygame.display.set_icon(self.icon)
        self.color_red = (255,0,0)
        self.color_green = (0,255,0)

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
        self.in_game_bg = settings
        self.bottom_menu = pygame.transform.scale(pygame.image.load('assets/menus/gui/0.png'), (1340, 70))
        self.tree = pygame.transform.scale(pygame.image.load('assets/backgrounds/1/tree.png'), (67, 105))
        self.text_stats = pygame.font.Font('assets/fonts/custom_font.ttf', 28)
        self.bottom_menu_buttons = pygame.sprite.Group()
        self.top_menu_buttons = pygame.sprite.Group()
        self.bottom_menu_buttons.add(
            Button(global_variables.menu_bottom[1], 50, 684, 80, 80, 'PAUSE'),
            Button(global_variables.menu_bottom[2], 140, 684, 80, 80, 'QUICK'),
            Button(global_variables.menu_bottom[3], 230, 684, 80, 80, 'PLAY'),
            Button(global_variables.menu_bottom[4], 410, 684, 80, 80, 'FREEZE'),
            Button(global_variables.menu_bottom[5], 500, 684, 80, 80, 'FIRE'),
            Button(global_variables.menu_bottom[6], 590, 684, 80, 80, 'STONES'),
            Button(global_variables.menu_bottom[7], 680, 684, 80, 80, 'RAIN'),
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
        self.text_h2 = pygame.font.Font('assets/fonts/custom_font.ttf', 56)
        self.text_p = pygame.font.Font('assets/fonts/custom_font.ttf', 28)
        self.menu_tower_archer_opened = False
        self.menu_tower_archer = pygame.sprite.Group()
        self.menu_tower_archer.add(
            Button(global_variables.towers_archer[0], 330, 100, 670, 400, False),
            Button(global_variables.towers_archer[2], 370, 170, 125, 140, 'BUY_ARCHER_TOWER_1', price=12),
            Button(global_variables.towers_archer[7], 525, 170, 125, 140, 'BUY_ARCHER_TOWER_2', price=24),
            Button(global_variables.towers_archer[9], 680, 170, 125, 140, 'BUY_ARCHER_TOWER_3', price=36),
            Button(global_variables.towers_archer[11], 835, 170, 125, 140, 'BUY_ARCHER_TOWER_4', price=48)
        )
        # Magic Tower
        self.menu_tower_magic_opened = False
        self.menu_tower_magic = pygame.sprite.Group()
        self.menu_tower_magic.add(
            Button(global_variables.towers_magic[0], 330, 100, 670, 400, False),
            Button(global_variables.towers_magic[2], 370, 170, 125, 140, 'BUY_MAGIC_TOWER_1', 48),
            Button(global_variables.towers_magic[6], 525, 170, 125, 140, 'BUY_MAGIC_TOWER_2', 64),
            Button(global_variables.towers_magic[11], 680, 170, 125, 140, 'BUY_MAGIC_TOWER_3', 80),
            Button(global_variables.towers_magic[16], 835, 170, 125, 140, 'BUY_MAGIC_TOWER_4', 96)
        )
        # Stone Tower
        self.menu_tower_stone_opened = False
        self.menu_tower_stone = pygame.sprite.Group()
        self.menu_tower_stone.add(
            Button(global_variables.towers_stone[0], 330, 100, 670, 400, False),
            Button(global_variables.towers_stone[3], 370, 170, 125, 140, 'BUY_STONE_TOWER_1', 44),
            Button(global_variables.towers_stone[6], 525, 170, 125, 140, 'BUY_STONE_TOWER_2', 64),
            Button(global_variables.towers_stone[12], 680, 170, 125, 140, 'BUY_STONE_TOWER_3', 84),
            Button(global_variables.towers_stone[15], 835, 170, 125, 140, 'BUY_STONE_TOWER_4', 104)
        )
        # Support Tower
        self.menu_tower_support_opened = False
        self.menu_tower_support = pygame.sprite.Group()
        self.menu_tower_support.add(
            Button(global_variables.towers_support[0], 330, 100, 670, 400, False),
            Button(global_variables.towers_support[1], 370, 170, 125, 140, 'BUY_SUPPORT_TOWER_1', price=28),
            Button(global_variables.towers_support[4], 525, 170, 125, 140, 'BUY_SUPPORT_TOWER_2', price=38),
            Button(global_variables.towers_support[7], 680, 170, 125, 140, 'BUY_SUPPORT_TOWER_3', price=48),
            Button(global_variables.towers_support[10], 835, 170, 125, 140, 'BUY_SUPPORT_TOWER_4', price=68)
        )
        # Freeze Effect
        self.menu_freeze_effect_opened = False
        self.menu_freeze_effect = pygame.sprite.Group()
        self.menu_freeze_effect.add(
            Button(global_variables.towers_support[0], 330, 100, 670, 400, False),
            Button(global_variables.effect_icons[2], 370, 220, 140, 140, False)
        )
        # Fire Effect
        self.menu_fire_effect_opened = False
        self.menu_fire_effect = pygame.sprite.Group()
        self.menu_fire_effect.add(
            Button(global_variables.towers_support[0], 330, 100, 670, 400, False),
            Button(global_variables.effect_icons[1], 370, 220, 140, 140, False)
        )
        # Stones Effect
        self.menu_stones_effect_opened = False
        self.menu_stones_effect = pygame.sprite.Group()
        self.menu_stones_effect.add(
            Button(global_variables.towers_support[0], 330, 100, 670, 400, False),
            Button(global_variables.effect_icons[7], 370, 220, 140, 140, False)
        )
        # Rain Effect
        self.menu_rain_effect_opened = False
        self.menu_rain_effect = pygame.sprite.Group()
        self.menu_rain_effect.add(
            Button(global_variables.towers_support[0], 330, 100, 670, 400, False),
            Button(global_variables.effect_icons[4], 370, 220, 140, 140, False)
        )

        # You Lose
        self.you_lose_buttons = pygame.sprite.Group()
        self.text_you_lose = pygame.font.Font('assets/fonts/custom_font.ttf', 48)
        self.you_lose_buttons.add(
            Button(global_variables.menu_you_lose[2], 440, 120, 400, 460, False),
            Button(global_variables.menu_you_lose[3], 504, 240, 271, 300, False),
            Button(global_variables.menu_you_lose[4], 535, 120, 200, 82, False),
            Button(global_variables.menu_you_lose[0], 520, 520, 80, 80, 'BACK'),
            Button(global_variables.menu_you_lose[1], 680, 520, 80, 80, 'RESTART')
        )

        # You Win
        self.you_win_buttons = pygame.sprite.Group()
        self.text_you_win = pygame.font.Font('assets/fonts/custom_font.ttf', 32)
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
            self.screen.blit(self.text_stats.render(str(global_variables.stats_kills), True, (247, 187, 31)),
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
        """
        Draws the tower's shop menus.
        :param:game_state -> 1: Main menu,
                             2: Game- Started,
                             3: You lose,
                             4: You win
        :return: None
        """
        # Draw the menus
        if game_state == 2:
            if self.menu_tower_archer_opened:
                self.menu_tower_archer.draw(self.screen)
                self.screen.blit(self.text_h2.render('Archer Towers:', True, (247, 187, 31)), (470, 110))
                self.screen.blit(self.text_p.render('Damage: 1', True, (247, 187, 31)), (370, 300))
                self.screen.blit(self.text_p.render('Range: 120', True, (247, 187, 31)), (370, 330))
                self.screen.blit(self.text_p.render('Attack: 0.8', True, (247, 187, 31)), (370, 360))
                if global_variables.stats_money >= 12:
                    self.screen.blit(self.text_p.render('Price: 12', True, self.color_green), (370, 390))
                else:
                    self.screen.blit(self.text_p.render('Price: 12', True, self.color_red), (370, 390))
                self.screen.blit(self.text_p.render('Damage: 3', True, (247, 187, 31)), (525, 300))
                self.screen.blit(self.text_p.render('Range: 130', True, (247, 187, 31)), (525, 330))
                self.screen.blit(self.text_p.render('Attack: 0.7', True, (247, 187, 31)), (525, 360))
                if global_variables.stats_money >= 24:
                    self.screen.blit(self.text_p.render('Price: 24', True, self.color_green), (525, 390))
                else:
                    self.screen.blit(self.text_p.render('Price: 24', True, self.color_red), (525, 390))
                self.screen.blit(self.text_p.render('Damage: 5', True, (247, 187, 31)), (680, 300))
                self.screen.blit(self.text_p.render('Range: 120', True, (247, 187, 31)), (680, 330))
                self.screen.blit(self.text_p.render('Attack: 0.6', True, (247, 187, 31)), (680, 360))
                if global_variables.stats_money >= 36:
                    self.screen.blit(self.text_p.render('Price: 36', True, self.color_green), (680, 390))
                else:
                    self.screen.blit(self.text_p.render('Price: 36', True, self.color_red), (680, 390))
                self.screen.blit(self.text_p.render('Damage: 7', True, (247, 187, 31)), (835, 300))
                self.screen.blit(self.text_p.render('Range: 150', True, (247, 187, 31)), (835, 330))
                self.screen.blit(self.text_p.render('Attack: 0.5', True, (247, 187, 31)), (835, 360))
                if global_variables.stats_money >= 48:
                    self.screen.blit(self.text_p.render('Price: 48', True, self.color_green), (835, 390))
                else:
                    self.screen.blit(self.text_p.render('Price: 48', True, self.color_red), (835, 390))
            elif self.menu_tower_stone_opened:
                self.menu_tower_stone.draw(self.screen)
                self.screen.blit(self.text_h2.render('Stone Towers:', True, (247, 187, 31)), (470, 110))
                self.screen.blit(self.text_p.render('Damage: 5', True, (247, 187, 31)), (370, 300))
                self.screen.blit(self.text_p.render('Range: 120', True, (247, 187, 31)), (370, 330))
                self.screen.blit(self.text_p.render('Attack: 0.8', True, (247, 187, 31)), (370, 360))
                if global_variables.stats_money >= 44:
                    self.screen.blit(self.text_p.render('Price: 44', True, self.color_green), (370, 390))
                else:
                    self.screen.blit(self.text_p.render('Price: 44', True, self.color_red), (370, 390))
                self.screen.blit(self.text_p.render('Damage: 12', True, (247, 187, 31)), (525, 300))
                self.screen.blit(self.text_p.render('Range: 130', True, (247, 187, 31)), (525, 330))
                self.screen.blit(self.text_p.render('Attack: 0.7', True, (247, 187, 31)), (525, 360))
                if global_variables.stats_money >= 64:
                    self.screen.blit(self.text_p.render('Price: 64', True, self.color_green), (525, 390))
                else:
                    self.screen.blit(self.text_p.render('Price: 64', True, self.color_red), (525, 390))
                self.screen.blit(self.text_p.render('Damage: 18', True, (247, 187, 31)), (680, 300))
                self.screen.blit(self.text_p.render('Range: 120', True, (247, 187, 31)), (680, 330))
                self.screen.blit(self.text_p.render('Attack: 0.6', True, (247, 187, 31)), (680, 360))
                if global_variables.stats_money >= 84:
                    self.screen.blit(self.text_p.render('Price: 84', True, self.color_green), (680, 390))
                else:
                    self.screen.blit(self.text_p.render('Price: 84', True, self.color_red), (680, 390))
                self.screen.blit(self.text_p.render('Damage: 24', True, (247, 187, 31)), (835, 300))
                self.screen.blit(self.text_p.render('Range: 150', True, (247, 187, 31)), (835, 330))
                self.screen.blit(self.text_p.render('Attack: 0.5', True, (247, 187, 31)), (835, 360))
                if global_variables.stats_money >= 104:
                    self.screen.blit(self.text_p.render('Price: 104', True, self.color_green), (835, 390))
                else:
                    self.screen.blit(self.text_p.render('Price: 104', True, self.color_red), (835, 390))
            elif self.menu_tower_magic_opened:
                self.menu_tower_magic.draw(self.screen)
                self.screen.blit(self.text_h2.render('Magic Towers:', True, (247, 187, 31)), (470, 110))
                self.screen.blit(self.text_p.render('Damage: 8', True, (247, 187, 31)), (370, 300))
                self.screen.blit(self.text_p.render('Range: 120', True, (247, 187, 31)), (370, 330))
                self.screen.blit(self.text_p.render('Attack: 0.8', True, (247, 187, 31)), (370, 360))
                if global_variables.stats_money >= 48:
                    self.screen.blit(self.text_p.render('Price: 48', True, self.color_green), (370, 390))
                else:
                    self.screen.blit(self.text_p.render('Price: 48', True, self.color_red), (370, 390))
                self.screen.blit(self.text_p.render('Damage: 12', True, (247, 187, 31)), (525, 300))
                self.screen.blit(self.text_p.render('Range: 130', True, (247, 187, 31)), (525, 330))
                self.screen.blit(self.text_p.render('Attack: 0.7', True, (247, 187, 31)), (525, 360))
                if global_variables.stats_money >= 64:
                    self.screen.blit(self.text_p.render('Price: 64', True, self.color_green), (525, 390))
                else:
                    self.screen.blit(self.text_p.render('Price: 64', True, self.color_red), (525, 390))
                self.screen.blit(self.text_p.render('Damage: 16', True, (247, 187, 31)), (680, 300))
                self.screen.blit(self.text_p.render('Range: 140', True, (247, 187, 31)), (680, 330))
                self.screen.blit(self.text_p.render('Attack: 0.6', True, (247, 187, 31)), (680, 360))
                if global_variables.stats_money >= 80:
                    self.screen.blit(self.text_p.render('Price: 80', True, self.color_green), (680, 390))
                else:
                    self.screen.blit(self.text_p.render('Price: 80', True, self.color_red), (680, 390))
                self.screen.blit(self.text_p.render('Damage: 30', True, (247, 187, 31)), (835, 300))
                self.screen.blit(self.text_p.render('Range: 150', True, (247, 187, 31)), (835, 330))
                self.screen.blit(self.text_p.render('Attack: 0.5', True, (247, 187, 31)), (835, 360))
                if global_variables.stats_money >= 96:
                    self.screen.blit(self.text_p.render('Price: 50', True, self.color_green), (835, 390))
                else:
                    self.screen.blit(self.text_p.render('Price: 50', True, self.color_red), (835, 390))
            elif self.menu_tower_support_opened:
                self.menu_tower_support.draw(self.screen)
                self.screen.blit(self.text_h2.render('Support Towers:', True, (247, 187, 31)), (470, 110))
                self.screen.blit(self.text_p.render('Damage: 4', True, (247, 187, 31)), (370, 300))
                self.screen.blit(self.text_p.render('Range: 120', True, (247, 187, 31)), (370, 330))
                self.screen.blit(self.text_p.render('Attack: 0.8', True, (247, 187, 31)), (370, 360))
                if global_variables.stats_money >= 28:
                    self.screen.blit(self.text_p.render('Price: 28', True, self.color_green), (370, 390))
                else:
                    self.screen.blit(self.text_p.render('Price: 28', True, self.color_red), (370, 390))
                self.screen.blit(self.text_p.render('Damage: 6', True, (247, 187, 31)), (525, 300))
                self.screen.blit(self.text_p.render('Range: 130', True, (247, 187, 31)), (525, 330))
                self.screen.blit(self.text_p.render('Attack: 0.7', True, (247, 187, 31)), (525, 360))
                if global_variables.stats_money >= 38:
                    self.screen.blit(self.text_p.render('Price: 38', True, self.color_green), (525, 390))
                else:
                    self.screen.blit(self.text_p.render('Price: 38', True, self.color_red), (525, 390))
                self.screen.blit(self.text_p.render('Damage: 8', True, (247, 187, 31)), (680, 300))
                self.screen.blit(self.text_p.render('Range: 120', True, (247, 187, 31)), (680, 330))
                self.screen.blit(self.text_p.render('Attack: 0.6', True, (247, 187, 31)), (680, 360))
                if global_variables.stats_money >= 48:
                    self.screen.blit(self.text_p.render('Price: 48', True, self.color_green), (680, 390))
                else:
                    self.screen.blit(self.text_p.render('Price: 48', True, self.color_red), (680, 390))
                self.screen.blit(self.text_p.render('Damage: 10', True, (247, 187, 31)), (835, 300))
                self.screen.blit(self.text_p.render('Range: 150', True, (247, 187, 31)), (835, 330))
                self.screen.blit(self.text_p.render('Attack: 0.5', True, (247, 187, 31)), (835, 360))
                if global_variables.stats_money >= 68:
                    self.screen.blit(self.text_p.render('Price: 68', True, self.color_green), (835, 390))
                else:
                    self.screen.blit(self.text_p.render('Price: 68', True, self.color_red), (835, 390))
            elif self.menu_freeze_effect_opened:
                self.menu_freeze_effect.draw(self.screen)
                self.screen.blit(self.text_h2.render('Freeze Effect', True, (247, 187, 31)), (470, 110))
                self.screen.blit(self.text_p.render('Damage: 20 *', True, (247, 187, 31)), (530, 210))
                self.screen.blit(self.text_p.render('Range: 25', True, (247, 187, 31)), (530, 240))
                self.screen.blit(self.text_p.render('Attack: 10', True, (247, 187, 31)), (530, 270))
                self.screen.blit(self.text_p.render('Price: 35', True, (247, 187, 31)), (530, 300))
                self.screen.blit(self.text_p.render('* Some creatures have freeze resistance!', True, (247, 187, 31)), (470, 370))
            elif self.menu_stones_effect_opened:
                self.menu_stones_effect.draw(self.screen)
                self.screen.blit(self.text_h2.render('Falling Stones Effect', True, (247, 187, 31)), (470, 100))
                self.screen.blit(self.text_p.render('Damage: 30 *', True, (247, 187, 31)), (530, 210))
                self.screen.blit(self.text_p.render('Range: 25', True, (247, 187, 31)), (530, 240))
                self.screen.blit(self.text_p.render('Attack: 10', True, (247, 187, 31)), (530, 270))
                self.screen.blit(self.text_p.render('Price: 35', True, (247, 187, 31)), (530, 300))
                self.screen.blit(self.text_p.render('* Some creatures have stones resistance!', True, (247, 187, 31)), (470, 370))
            elif self.menu_fire_effect_opened:
                self.menu_fire_effect.draw(self.screen)
                self.screen.blit(self.text_h2.render('Fire Effect', True, (247, 187, 31)), (470, 100))
                self.screen.blit(self.text_p.render('Damage: 25 *', True, (247, 187, 31)), (530, 210))
                self.screen.blit(self.text_p.render('Range: 25', True, (247, 187, 31)), (530, 240))
                self.screen.blit(self.text_p.render('Attack: 10', True, (247, 187, 31)), (530, 270))
                self.screen.blit(self.text_p.render('Price: 55', True, (247, 187, 31)), (530, 300))
                self.screen.blit(self.text_p.render('* Some creatures have fire resistance!', True, (247, 187, 31)), (470, 370))
            elif self.menu_rain_effect_opened:
                self.menu_rain_effect.draw(self.screen)
                self.screen.blit(self.text_h2.render('Poison rain Effect:', True, (247, 187, 31)), (470, 100))
                self.screen.blit(self.text_p.render('Damage: 30 *', True, (247, 187, 31)), (530, 210))
                self.screen.blit(self.text_p.render('Range: 20', True, (247, 187, 31)), (530, 240))
                self.screen.blit(self.text_p.render('Attack: 10', True, (247, 187, 31)), (530, 270))
                self.screen.blit(self.text_p.render('Price: 50', True, (247, 187, 31)), (530, 300))
                self.screen.blit(self.text_p.render('* Some creatures have poison rain resistance!', True, (247, 187, 31)), (470, 370))

    @property
    def get_screen(self):
        """
        Returns the main surface object.
        :return:Surface obj
        """
        return self.screen

    def click(self, x, y, game_state):
        """
        Check the mouse coordinates against all menu buttons
        :param x: int
        :param y: int
        :param:game_state: int -> 1: Main menu,
                                  2: Game- Started,
                                  3: You lose,
                                  4: You win
        :return:
        """
        if game_state == 1:
            for sprite in self.main_menu_buttons:
                if sprite.click(x, y):
                    return sprite.button_id
        elif game_state == 2:
            # Bottom menus
            for sprite in self.bottom_menu_buttons:
                if sprite.click(x, y):
                    if sprite.click(x, y) == 'ARCHER':
                        self.close_open_menus()
                        self.menu_tower_archer_opened = True
                        return 'ARCHER'
                    elif sprite.click(x, y) == 'MAGIC':
                        self.close_open_menus()
                        self.menu_tower_magic_opened = True
                        return 'MAGIC'
                    elif sprite.click(x, y) == 'STONE':
                        self.close_open_menus()
                        self.menu_tower_stone_opened = True
                        return 'STONE'
                    elif sprite.click(x, y) == 'SUPPORT':
                        self.close_open_menus()
                        self.menu_tower_support_opened = True
                        return 'SUPPORT'
                    elif sprite.click(x, y) == 'FREEZE':
                        self.close_open_menus()
                        self.menu_freeze_effect_opened = True
                        return 'FREEZE'
                    elif sprite.click(x, y) == 'FIRE':
                        self.close_open_menus()
                        self.menu_fire_effect_opened = True
                        return 'FIRE'
                    elif sprite.click(x, y) == 'RAIN':
                        self.close_open_menus()
                        self.menu_rain_effect_opened = True
                        return 'RAIN'
                    elif sprite.click(x, y) == 'STONES':
                        self.close_open_menus()
                        self.menu_stones_effect_opened = True
                        return 'STONES'

            # Buy menus
            if self.menu_tower_archer_opened:
                for sprite in self.menu_tower_archer:
                    if sprite.click(x, y):
                        return sprite.button_id
            elif self.menu_tower_stone_opened:
                for sprite in self.menu_tower_stone:
                    if sprite.click(x, y):
                        return sprite.button_id
            elif self.menu_tower_magic_opened:
                for sprite in self.menu_tower_magic:
                    if sprite.click(x, y):
                        return sprite.button_id
            elif self.menu_tower_support_opened:
                for sprite in self.menu_tower_support:
                    if sprite.click(x, y):
                        return sprite.button_id
            elif self.menu_freeze_effect_opened:
                for sprite in self.menu_freeze_effect:
                    if sprite.click(x, y):
                        return sprite.button_id
            elif self.menu_stones_effect_opened:
                for sprite in self.menu_stones_effect:
                    if sprite.click(x, y):
                        return sprite.button_id
            elif self.menu_fire_effect_opened:
                for sprite in self.menu_fire_effect:
                    if sprite.click(x, y):
                        return sprite.button_id
            elif self.menu_rain_effect_opened:
                for sprite in self.menu_rain_effect:
                    if sprite.click(x, y):
                        return sprite.button_id


        elif game_state == 3:
            for sprite in self.you_lose_buttons:
                if sprite.click(x, y):
                    return sprite.button_id
        elif game_state == 4:
            for sprite in self.you_win_buttons:
                if sprite.click(x, y):
                    return sprite.button_id

    def close_open_menus(self):
        """
        Closes all open tower's shop menus
        :return:
        """
        self.menu_tower_archer_opened = False
        self.menu_tower_support_opened = False
        self.menu_tower_magic_opened = False
        self.menu_tower_stone_opened = False
        self.menu_rain_effect_opened = False
        self.menu_fire_effect_opened = False
        self.menu_stones_effect_opened = False
        self.menu_freeze_effect_opened = False


class Button(pygame.sprite.Sprite):
    """
    Defines the main button class
    """

    def __init__(self, img, x, y, width, height, button_id, price=0):
        pygame.sprite.Sprite.__init__(self)
        self.sound_click = pygame.mixer.Sound('assets/sounds/click.wav')
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.button_id = button_id
        self.image = pygame.transform.scale(img, (self.width, self.height))
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.price = price

    def click(self, x, y):
        """
        Check the mouse coordinates against all menu buttons
        :param x: int
        :param y: int
        :return:
        """
        if self.rect.collidepoint(x, y):
            if self.button_id:
                pygame.mixer.Sound.play(self.sound_click)
                if self.price == 0:
                    return self.button_id
                elif self.price != 0 and global_variables.stats_money >= self.price:
                    global_variables.stats_money -= self.price
                    return self.button_id
                else:
                    return False
            else:
                return False
