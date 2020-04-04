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
enemy_6 = [pygame.image.load('assets/enemies/6/' + str(x) + '.png') for x in range(10)]
enemy_7 = [pygame.image.load('assets/enemies/6/' + str(x) + '.png') for x in range(10)]
enemy_8 = [pygame.image.load('assets/enemies/8/' + str(x) + '.png') for x in range(10)]
enemy_9 = [pygame.image.load('assets/enemies/9/' + str(x) + '.png') for x in range(10)]
enemy_10 = [pygame.image.load('assets/enemies/10/' + str(x) + '.png') for x in range(10)]

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
rain = [pygame.image.load('assets/effects/rain/' + str(x) + '.png') for x in range(19)]
fire = [pygame.image.load('assets/effects/fire/' + str(x) + '.png') for x in range(19)]
freeze = [pygame.image.load('assets/effects/freeze/' + str(x) + '.png') for x in range(16)]
stone = [pygame.image.load('assets/effects/stone/' + str(x) + '.png') for x in range(18)]
time = [pygame.image.load('assets/effects/time/' + str(x) + '.png') for x in range(14)]
zip = [pygame.image.load('assets/effects/zip/' + str(x) + '.png') for x in range(14)]
damage = [pygame.image.load('assets/effects/damage/' + str(x) + '.png') for x in range(10)]
defense = [pygame.image.load('assets/effects/def/' + str(x) + '.png') for x in range(10)]
effect_icons = [pygame.image.load('assets/effects/icons/' + str(x) + '.png') for x in range(1,9)]

# Map specific
# Map 1
map_1_bg = pygame.transform.scale(pygame.image.load('assets/backgrounds/1/bg.png'), (1280, 720))
map_1_tower_positions = [(1122, 262), (856, 264), (585, 262), (502, 468), (794, 481), (1078, 480), (366, 642)]
map_1_path_1 = [(1280, 100), (1100, 100), (470, 100), (384, 240), (631, 359), (702, 528), (1194, 541), (1242, 541)]
map_1_path_2 = [(1280, 100), (1100, 100), (470, 100), (384, 240), (639, 444), (603, 509), (469, 562), (479, 690), (475, 699)]

# Map 2
map_2_bg = pygame.transform.scale(pygame.image.load('assets/backgrounds/2/bg.png'), (1280, 720))
map_2_tower_positions = [(1159, 317), (945, 263), (700, 295), (802, 470), (548, 443), (374, 662), (101, 663), (877, 664), (1142, 661)]
map_2_path_1 = [(1280, 210), (1261, 212), (1183, 180), (1089, 143), (881, 149), (792, 245), (765, 345), (636, 361), (518, 311), (409, 399), (388, 508),
                (217, 539),
                (11, 537), (2, 546)]
map_2_path_2 = [(1280, 205), (1259, 203), (1112, 151), (899, 151), (798, 229), (741, 367), (618, 380), (717, 522), (887, 541), (1050, 541), (1264, 550),
                (1274, 556)]

# Map 3
map_3_bg = pygame.transform.scale(pygame.image.load('assets/backgrounds/3/bg.png'), (1280, 720))
map_3_tower_positions = [(1089, 425), (961, 631), (836, 423), (836, 201), (521, 234), (188, 265), (238, 473), (196, 679)]
map_3_path_1 = [(1280, 512), (1269, 500), (1027, 504), (929, 459), (931, 263), (932, 14), (932, 6)]
map_3_path_2 = [(1280, 512), (1270, 499), (788, 499), (698, 446), (703, 164), (605, 106), (406, 111), (313, 185), (241, 336), (133, 355), (69, 483), (317, 601),
                (343, 664),
                (359, 711)]
# Map 4
map_4_bg = pygame.transform.scale(pygame.image.load('assets/backgrounds/4/bg.png'), (1280, 720))
map_4_tower_positions = [(978, 202), (784, 203), (588, 209), (963, 434), (678, 434), (477, 442), (582, 655), (106, 570)]
map_4_path_1 = [(1290, 110), (1264, 72), (533, 68), (403, 205), (516, 294), (756, 301), (857, 446), (730, 522), (473, 520), (241, 510), (163, 464), (22, 462),
                (7, 462)]
map_4_path_2 = [(1290, 110), (1264, 72), (533, 68), (403, 205), (516, 294), (756, 301), (857, 446), (730, 522), (473, 520), (241, 510), (163, 464), (22, 462),
                (7, 462)]

# Map 5
map_5_bg = pygame.transform.scale(pygame.image.load('assets/backgrounds/5/bg.png'), (1280, 720))
map_5_tower_positions = [(1018, 203), (749, 111), (876, 495), (507, 542), (337, 177), (299, 403), (368, 664), (155, 537)]
map_5_path_1 = [(1280, 278), (1271, 278), (1149, 124), (1013, 38), (943, 55), (818, 182), (777, 202), (492, 202), (398, 292), (407, 410), (239, 588),
                (144, 621), (75, 677),
                (38, 707)]
map_5_path_2 = [(1280, 250), (1264, 250), (1082, 65), (979, 44), (813, 191), (778, 257), (780, 381), (689, 415), (407, 404), (225, 600), (150, 616), (58, 683),
                (29, 712)]

# Map 6
map_6_bg = pygame.transform.scale(pygame.image.load('assets/backgrounds/6/bg.png'), (1280, 720))
map_6_tower_positions = [(1018, 203), (749, 111), (876, 495), (507, 542), (337, 177), (299, 403), (368, 664), (155, 537)]
map_6_path_1 = [(0, 80), (2, 70), (100, 80), (192, 53), (270, 87), (902, 72), (1006, 213), (850, 302), (640, 311), (541, 483), (559, 544), (402, 546),
                (341, 656), (338, 699)]
map_6_path_2 = [(0, 80), (2, 70), (100, 80), (192, 53), (270, 87), (902, 72), (1006, 213), (850, 302), (640, 311), (541, 483), (566, 529), (763, 554),
                (824, 660), (827, 689)]

# Map 7
map_7_bg = pygame.transform.scale(pygame.image.load('assets/backgrounds/7/bg.png'), (1280, 720))
map_7_tower_positions = [(511, 190), (777, 167), (1011, 187), (975, 403), (843, 604), (452, 657), (223, 467), (630, 650), (372, 181)]
map_7_path_1 = [(0, 200), (5, 202), (178, 203), (269, 261), (561, 257), (632, 201), (689, 64), (840, 43), (935, 230), (1119, 312), (1131, 457), (1007, 485),
                (783, 496), (691, 546), (313, 549), (159, 538), (75, 356), (14, 316), (2, 316)]
map_7_path_2 = [(0, 200), (5, 202), (178, 203), (269, 261), (561, 257), (632, 201), (689, 64), (840, 43), (935, 230), (1119, 312), (1131, 457), (1007, 485),
                (783, 496), (691, 546), (312, 536), (320, 690), (320, 710)]

# Map 8
map_8_bg = pygame.transform.scale(pygame.image.load('assets/backgrounds/8/bg.png'), (1280, 720))
map_8_tower_positions = [(87, 448), (353, 427), (580, 196), (1048, 205), (823, 392), (1095, 427), (1042, 647)]
map_8_path_1 = [(0, 510), (30, 519), (143, 509), (195, 435), (240, 325), (398, 265), (469, 97), (549, 57), (791, 62), (877, 32), (963, 66), (1116, 67),
                (1208, 241), (1086, 283), (944, 369), (968, 492), (1162, 552), (1184, 691), (1188, 711)]
map_8_path_2 = [(0, 510), (30, 519), (143, 509), (195, 435), (240, 325), (398, 265), (469, 97), (549, 57), (791, 62), (877, 32), (963, 66), (1116, 67),
                (1208, 241), (1086, 283), (944, 369), (968, 492), (1162, 552), (1184, 691), (1188, 711)]

# Map 9
map_9_bg = pygame.transform.scale(pygame.image.load('assets/backgrounds/9/bg.png'), (1280, 720))
map_9_tower_positions = [(225, 183), (360, 386), (161, 574), (638, 250), (757, 455), (725, 668), (1002, 471)]
map_9_path_1 = [(0, 450), (7, 455), (133, 455), (201, 351), (261, 262), (353, 223), (480, 284), (622, 348), (603, 460), (721, 518), (932, 519), (1019, 568),
                (1257, 573), (1272, 573)]

map_9_path_2 = [(0, 450), (7, 455), (133, 455), (201, 351), (261, 262), (353, 223), (480, 284), (628, 341), (734, 263), (789, 155), (806, 131)]

# Map 10
map_10_bg = pygame.transform.scale(pygame.image.load('assets/backgrounds/10/bg.png'), (1280, 720))
map_10_tower_positions = [(282, 514), (408, 295), (570, 510), (887, 350), (1168, 346)]
map_10_path_1 = [(0, 380), (2, 382), (741, 383), (822, 433), (969, 430), (1022, 352), (1124, 212), (1258, 210), (1272, 211)]
map_10_path_2 = [(0, 380), (2, 382), (741, 383), (822, 433), (969, 430), (1022, 352), (1124, 212), (1258, 210), (1272, 211)]

# Map 11
map_11_bg = pygame.transform.scale(pygame.image.load('assets/backgrounds/11/bg.png'), (1280, 720))
map_11_tower_positions = [(208, 221), (200, 602), (254, 405), (553, 490), (845, 512), (962, 294), (1102, 304), (725, 328)]
map_11_path_1 = [(0, 80), (13, 85), (60, 239), (171, 297), (378, 295), (464, 350), (636, 369), (712, 579), (1009, 586), (1073, 672), (1076, 691)]
map_11_path_2 = [(0, 80), (13, 85), (60, 239), (171, 297), (378, 295), (464, 350), (636, 369), (698, 425), (809, 358), (896, 190), (1166, 187), (1254, 248),
                 (1277, 246)]

# Map 12
map_12_bg = pygame.transform.scale(pygame.image.load('assets/backgrounds/12/bg.png'), (1280, 720))
map_12_tower_positions = [(149, 321), (420, 228), (480, 432), (689, 588), (917, 349), (983, 146)]
map_12_path_1 = [(0, 520), (39, 527), (140, 514), (198, 371), (311, 301), (498, 303), (610, 452), (733, 431), (789, 272), (865, 225), (1106, 229), (1177, 279),
                 (1261, 279), (1273, 279)]
map_12_path_2 = [(0, 520), (39, 527), (140, 514), (198, 371), (311, 301), (498, 303), (625, 457), (535, 550), (522, 671), (528, 683)]

game_settings = [
    [map_1_bg, map_1_tower_positions, map_1_path_1, map_1_path_2],
    [map_2_bg, map_2_tower_positions, map_2_path_1, map_2_path_2],
    [map_3_bg, map_3_tower_positions, map_3_path_1, map_3_path_2],
    [map_4_bg, map_4_tower_positions, map_4_path_1, map_4_path_2],
    [map_5_bg, map_5_tower_positions, map_5_path_1, map_5_path_2],
    [map_6_bg, map_6_tower_positions, map_6_path_1, map_6_path_2],
    [map_7_bg, map_7_tower_positions, map_7_path_1, map_7_path_2],
    [map_8_bg, map_8_tower_positions, map_8_path_1, map_8_path_2],
    [map_9_bg, map_9_tower_positions, map_9_path_1, map_9_path_2],
    [map_10_bg, map_10_tower_positions, map_10_path_1, map_10_path_2],
    [map_11_bg, map_11_tower_positions, map_11_path_1, map_11_path_2],
    [map_12_bg, map_12_tower_positions, map_12_path_1, map_12_path_2]
]
