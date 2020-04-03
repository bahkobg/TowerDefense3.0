import pygame

# General
stats_kills = 0
stats_money = 0
stats_player_mana = 0
stats_player_health = 0

# Enemies
enemy_1 = [pygame.image.load('assets/enemies/1/' + str(x) + '.png') for x in range(20)]
enemy_2 = [pygame.image.load('assets/enemies/2/' + str(x) + '.png') for x in range(20)]
enemy_3 = [pygame.image.load('assets/enemies/3/' + str(x) + '.png') for x in range(20)]
enemy_4 = [pygame.image.load('assets/enemies/4/' + str(x) + '.png') for x in range(20)]
enemy_5 = [pygame.image.load('assets/enemies/5/' + str(x) + '.png') for x in range(20)]

# Towers
towers_archer = [pygame.image.load('assets/towers/archer/' + str(x) + '.png') for x in range(82)]
towers_magic = [pygame.image.load('assets/towers/magic/' + str(x) + '.png') for x in range(32)]
towers_stone = [pygame.image.load('assets/towers/stone/' + str(x) + '.png') for x in range(62)]
towers_support = [pygame.image.load('assets/towers/support/' + str(x) + '.png') for x in range(18)]


# Map specific
map_1_tower_positions = [(1122, 262), (856, 264), (585, 262), (502, 468), (794, 481), (1078, 480), (366, 642)]
map_1_path_1 = [(1100, 100), (470, 100), (384, 240), (631, 359), (702, 528), (1194, 541), (1242, 541)]
map_1_path_2 = [(1100, 100), (470, 100), (384, 240), (639, 444), (603, 509), (469, 562), (479, 690), (475, 699)]

# Menus
menu_new_game = [pygame.image.load('assets/menus/main_menu/' + str(x) + '.png') for x in range(11)]
menu_you_win = [pygame.image.load('assets/menus/win/' + str(x) + '.png') for x in range(10)]
menu_you_lose = [pygame.image.load('assets/menus/lose/' + str(x) + '.png') for x in range(5)]
menu_bottom = [pygame.image.load('assets/menus/gui/' + str(x) + '.png') for x in range(17)]

# Effects
rain = [pygame.image.load('assets/effects/rain/' + str(x) + '.png') for x in range(39)]

