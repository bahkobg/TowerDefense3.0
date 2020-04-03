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

# Menus
menu_new_game = [pygame.image.load('assets/menus/main_menu/' + str(x) + '.png') for x in range(11)]
menu_you_win = [pygame.image.load('assets/menus/win/' + str(x) + '.png') for x in range(10)]
menu_you_lose = [pygame.image.load('assets/menus/lose/' + str(x) + '.png') for x in range(5)]
menu_bottom = [pygame.image.load('assets/menus/gui/' + str(x) + '.png') for x in range(17)]

# Effects
rain = [pygame.image.load('assets/effects/rain/' + str(x) + '.png') for x in range(39)]

# Map specific
# Map 1
map_1_bg = pygame.transform.scale(pygame.image.load('assets/backgrounds/1/bg.png'), (1280, 720))
map_1_tower_positions = [(1122, 262), (856, 264), (585, 262), (502, 468), (794, 481), (1078, 480), (366, 642)]
map_1_path_1 = [(1100, 100), (470, 100), (384, 240), (631, 359), (702, 528), (1194, 541), (1242, 541)]
map_1_path_2 = [(1100, 100), (470, 100), (384, 240), (639, 444), (603, 509), (469, 562), (479, 690), (475, 699)]

# Map 2
map_2_bg = pygame.transform.scale(pygame.image.load('assets/backgrounds/2/bg.png'), (1280, 720))
map_2_tower_positions = [(1159, 317), (945, 263), (700, 295), (802, 470), (548, 443), (374, 662), (101, 663), (877, 664), (1142, 661)]
map_2_path_1 = [(1261, 212), (1183, 180), (1089, 143), (881, 149), (792, 245), (765, 345), (636, 361), (518, 311), (409, 399), (388, 508), (217, 539),
                (11, 537), (2, 546)]
map_2_path_2 = [(1259, 203), (1112, 151), (899, 151), (798, 229), (741, 367), (618, 380), (717, 522), (887, 541), (1050, 541), (1264, 550), (1274, 556)]

# Map 3
map_3_bg = pygame.transform.scale(pygame.image.load('assets/backgrounds/3/bg.png'), (1280, 720))
map_3_tower_positions = [(1089, 425), (961, 631), (836, 423), (836, 201), (521, 234), (188, 265), (238, 473), (196, 679)]
map_3_path_1 = [(1269, 512), (1027, 504), (929, 459), (931, 263), (932, 14), (932, 6)]
map_3_path_2 = [(1270, 499), (788, 499), (698, 446), (703, 164), (605, 106), (406, 111), (313, 185), (241, 336), (133, 355), (69, 483), (317, 601), (343, 664),
                (359, 711)]
# Map 4
map_4_bg = pygame.transform.scale(pygame.image.load('assets/backgrounds/4/bg.png'), (1280, 720))
map_4_tower_positions = [(978, 202), (784, 203), (588, 209), (963, 434), (678, 434), (477, 442), (582, 655), (106, 570)]
map_4_path_1 = [(1264, 72), (533, 68), (403, 205), (516, 294), (756, 301), (857, 446), (730, 522), (473, 520), (241, 510), (163, 464), (22, 462), (7, 462)]
map_4_path_2 = [(1264, 72), (533, 68), (403, 205), (516, 294), (756, 301), (857, 446), (730, 522), (473, 520), (241, 510), (163, 464), (22, 462), (7, 462)]

# Map 5
map_5_bg = pygame.transform.scale(pygame.image.load('assets/backgrounds/5/bg.png'), (1280, 720))
map_5_tower_positions = [(978, 202), (784, 203), (588, 209), (963, 434), (678, 434), (477, 442), (582, 655), (106, 570)]
map_5_path_1 = [(1271, 278), (1149, 124), (1013, 38), (943, 55), (818, 182), (777, 202), (492, 202), (398, 292), (407, 410), (239, 588), (144, 621), (75, 677),
                (38, 707)]
map_5_path_2 = [(1264, 250), (1082, 65), (979, 44), (813, 191), (778, 257), (780, 381), (689, 415), (407, 404), (225, 600), (150, 616), (58, 683), (29, 712)]

game_settings = [
    [map_1_bg, map_1_tower_positions, map_1_path_1, map_1_path_2],
    [map_2_bg, map_2_tower_positions, map_2_path_1, map_2_path_2],
    [map_3_bg, map_3_tower_positions, map_3_path_1, map_3_path_2],
    [map_4_bg, map_4_tower_positions, map_4_path_1, map_4_path_2],
    [map_5_bg, map_5_tower_positions, map_5_path_1, map_5_path_2]
]
