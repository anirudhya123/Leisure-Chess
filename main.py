from glob import glob
import json
import random
import sys
import time
import pygame
from pygame.locals import *
import webbrowser

# Global Variables
pygame.mixer.init()
FPS = 30
VOLUME = 1.0
SCREEN_HEIGHT = 700
SCREEN_WIDTH = 1000
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
BOARD = pygame.image.load(
    "Gallery\\sprites\\CHESS_BOARD.png").convert_alpha()
BACKGROUND = pygame.image.load(
    "Gallery\\sprites\\BACKGROUND__.jpg").convert_alpha()
GAME_SPRITES = {}
GAME_SOUNDS = {}
GAME_GRAPHICS = {}
BLOCK_POSITION = {'1': (53, 55), '9': (53, 130), '17': (53, 205), '25': (53, 280), '33': (53, 357), '41': (53, 434), '49': (53, 511), '57': (53, 587), '2': (128, 55), '10': (128, 130), '18': (128, 205), '26': (128, 280), '34': (128, 357), '42': (128, 435), '50': (128, 510), '58': (128, 587), '3': (205, 55),
                  '11': (205, 130), '19': (205, 205), '27': (205, 280), '35': (205, 357), '43': (205, 434), '51': (205, 511), '59': (205, 587), '4': (280, 55), '12': (280, 130), '20': (280, 205), '28': (280, 280), '36': (280, 357), '44': (280, 435), '52': (280, 510), '60': (280, 587), '5': (357, 55), '13': (357, 130), '21': (357, 205), '29': (357, 280), '37': (357, 357), '45': (357, 435), '53': (357, 510), '61': (357, 587), '6': (428, 55), '14': (434,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                   130), '22': (434, 205), '30': (434, 280), '38': (434, 357), '46': (434, 435), '54': (434, 510), '62': (434, 587), '7': (511, 55), '15': (511, 130), '23': (511, 205), '31': (511, 280), '39': (511, 357), '47': (511, 435), '55': (511, 510), '63': (511, 587), '8': (588, 55), '16': (588, 130), '24': (588, 205), '32': (588, 280), '40': (588, 357), '48': (588, 435), '56': (588, 510), '64': (588, 587)}
PIECE_POSITION_XT = {1: 'Boats-0', 2: 'Elephants-0', 3: 'Horses-0', 4: 'Queens-0', 5: 'Kings-0', 6: 'Horses-0', 7: 'Elephants-0', 8: 'Boats-0', 9: 'Armies-0', 10: 'Armies-0', 11: 'Armies-0', 12: 'Armies-0', 13: 'Armies-0', 14: 'Armies-0', 15: 'Armies-0', 16: 'Armies-0', 17: '', 18: '', 19: '', 20:
                     '', 21: '', 22: '', 23: '', 24: '', 25: '', 26: '', 27: '', 28: '', 29: '', 30: '', 31: '', 32: '', 33: '', 34: '', 35: '', 36: '', 37: '', 38: '',
                     39: '', 40: '', 41: '', 42: '', 43: '', 44: '', 45: '', 46: '', 47: '', 48: '', 49: 'Armies-1', 50: 'Armies-1', 51: 'Armies-1', 52: 'Armies-1', 53: 'Armies-1', 54: 'Armies-1', 55: 'Armies-1', 56: 'Armies-1', 57:
                     'Boats-1', 58: 'Elephants-1', 59: 'Horses-1', 60: 'Queens-1', 61: 'Kings-1', 62: 'Horses-1', 63: 'Elephants-1', 64: 'Boats-1'}
PIECE_POSITION = {1: 'Boats-0', 2: 'Elephants-0', 3: 'Horses-0', 4: 'Queens-0', 5: 'Kings-0', 6: 'Horses-0', 7: 'Elephants-0', 8: 'Boats-0', 9: 'Armies-0', 10: 'Armies-0', 11: 'Armies-0', 12: 'Armies-0', 13: 'Armies-0', 14: 'Armies-0', 15: 'Armies-0', 16: 'Armies-0', 17: '', 18: '', 19: '', 20:
                  '', 21: '', 22: '', 23: '', 24: '', 25: '', 26: '', 27: '', 28: '', 29: '', 30: '', 31: '', 32: '', 33: '', 34: '', 35: '', 36: '', 37: '', 38: '',
                  39: '', 40: '', 41: '', 42: '', 43: '', 44: '', 45: '', 46: '', 47: '', 48: '', 49: 'Armies-1', 50: 'Armies-1', 51: 'Armies-1', 52: 'Armies-1', 53: 'Armies-1', 54: 'Armies-1', 55: 'Armies-1', 56: 'Armies-1', 57:
                  'Boats-1', 58: 'Elephants-1', 59: 'Horses-1', 60: 'Queens-1', 61: 'Kings-1', 62: 'Horses-1', 63: 'Elephants-1', 64: 'Boats-1'}
BLOCK_AREA = {1: (45, 45, 75, 75), 2: (121, 45, 75, 75), 3: (197, 45, 75, 75), 4: (273, 45, 75, 75), 5: (350, 45, 75, 75), 6: (427, 45, 75, 75), 7: (503, 45, 75, 75), 8: (580, 45, 75, 75), 9: (45, 121, 75, 75), 10: (121, 121, 75, 75), 11: (197, 121, 75, 75), 12: (273, 121, 75, 75), 13: (350, 121, 75, 75), 14: (427, 121, 75, 75), 15: (503, 121, 75, 75), 16: (580, 121, 75, 75), 17: (45, 197, 75, 75), 18: (121, 197, 75, 75), 19: (197, 197, 75, 75), 20: (273, 197, 75, 75), 21: (350, 197, 75, 75), 22: (427, 197, 75, 75), 23: (503, 197, 75, 75), 24: (580, 197, 75, 75), 25: (45, 273, 75, 75), 26:
              (121, 273, 75, 75), 27: (197, 273, 75, 75), 28: (273, 273, 75, 75), 29: (350, 273, 75, 75), 30: (427, 273, 75, 75), 31: (503, 273, 75, 75), 32: (580, 273, 75, 75), 33: (45, 350, 75, 75), 34: (121, 350, 75, 75), 35: (197, 350, 75, 75), 36: (273, 350, 75, 75), 37: (350, 350, 75, 75), 38: (427, 350, 75, 75), 39: (503, 350, 75, 75), 40: (580, 350, 75, 75), 41: (45, 427, 75, 75), 42: (121, 427, 75, 75), 43: (197, 427, 75, 75), 44: (273, 427, 75, 75), 45: (350, 427, 75, 75), 46: (427, 427, 75, 75), 47: (503, 427, 75, 75), 48: (580, 427, 75, 75), 49: (45, 503, 75, 75), 50: (121, 503,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            75, 75), 51: (197, 503, 75, 75), 52: (273, 503, 75, 75), 53: (350, 503, 75, 75), 54: (427, 503, 75, 75), 55: (503, 503, 75, 75), 56: (580, 503, 75, 75), 57: (45, 580, 75, 75), 58: (121, 580, 75, 75), 59: (197, 580, 75, 75), 60: (273, 580, 75, 75), 61: (350, 580, 75, 75), 62: (427, 580, 75, 75), 63: (503, 580, 75, 75), 64: (580, 580, 75, 75)}

BLOCK_RANGE = {1: ([1, 8], [1, 57], [1, 1], [1, 64]), 2: ([1, 8], [2, 58], [2, 9], [2, 56]), 3: ([1, 8], [3, 59], [3, 17], [3, 48]), 4: ([1, 8], [4, 60], [4, 25], [4, 40]), 5: ([1, 8], [5, 61], [5, 33], [5, 32]), 6: ([1, 8], [6, 62], [6, 41], [6, 24]), 7: ([1, 8], [7, 63], [7, 49], [7, 16]), 8: ([1, 8], [8, 64], [8, 57], [8, 8]), 9: ([9, 16], [1, 57], [2, 9], [9, 63]), 10: ([9, 16], [2, 58], [3, 17], [1, 64]), 11: ([9, 16], [3, 59], [4, 25], [2, 56]), 12: ([9, 16], [4, 60], [5, 33], [3, 48]), 13: ([9, 16], [5, 61], [6, 41], [4, 40]), 14: ([9, 16], [6, 62], [7, 49], [5, 32]), 15: ([9, 16], [7, 63], [8, 57], [6, 24]), 16: ([9, 16], [8, 64], [16, 58], [7, 16]), 17: ([17, 24], [1, 57], [3, 17], [17, 62]), 18: ([17, 24], [2, 58], [4, 25], [9, 63]), 19: ([17, 24], [3, 59], [5, 33], [1, 64]), 20: ([17, 24], [4, 60], [6, 41], [2, 56]), 21: ([17, 24], [5, 61], [7, 49], [3, 48]), 22: ([17, 24], [6, 62], [8, 57], [4, 40]), 23: ([17, 24], [7, 63], [16, 58], [5, 32]), 24: ([17, 24], [8, 64], [24, 59], [6, 24]), 25: ([25, 32], [1, 57], [4, 25], [25, 61]), 26: ([25, 32], [2, 58], [5, 33], [17, 62]), 27: ([25, 32], [3, 59], [6, 41], [9, 63]), 28: ([25, 32], [4, 60], [7, 49], [1, 64]), 29: ([25, 32], [5, 61], [8, 57], [2, 56]), 30: ([25, 32], [6, 62], [16, 58], [3, 48]), 31: ([25, 32], [7, 63], [24, 59], [4, 40]), 32: ([25, 32], [8, 64], [32, 60], [5, 32]), 33: ([33, 40], [1, 57], [
    5, 33], [33, 60]), 34: ([33, 40], [2, 58], [6, 41], [25, 61]), 35: ([33, 40], [3, 59], [7, 49], [17, 62]), 36: ([33, 40], [4, 60], [8, 57], [9, 63]), 37: ([33, 40], [5, 61], [16, 58], [1, 64]), 38: ([33, 40], [6, 62], [24, 59], [2, 56]), 39: ([33, 40], [7, 63], [32, 60], [3, 48]), 40: ([33, 40], [8, 64], [40, 61], [4, 40]), 41: ([41, 48], [1, 57], [6, 41], [41, 59]), 42: ([41, 48], [2, 58], [7, 49], [33, 60]), 43: ([41, 48], [3, 59], [8, 57], [25, 61]), 44: ([41, 48], [4, 60], [16, 58], [17, 62]), 45: ([41, 48], [5, 61], [24, 59], [9, 63]), 46: ([41, 48], [6, 62], [32, 60], [1, 64]), 47: ([41, 48], [7, 63], [40, 61], [2, 56]), 48: ([41, 48], [8, 64], [48, 62], [3, 48]), 49: ([49, 56], [1, 57], [7, 49], [49, 58]), 50: ([49, 56], [2, 58], [8, 57], [41, 59]), 51: ([49, 56], [3, 59], [16, 58], [33, 60]), 52: ([49, 56], [4, 60], [24, 59], [25, 61]), 53: ([49, 56], [5, 61], [32, 60], [17, 62]), 54: ([49, 56], [6, 62], [40, 61], [9, 63]), 55: ([49, 56], [7, 63], [48, 62], [1, 64]), 56: ([49, 56], [8, 64], [56, 63], [2, 56]), 57: ([57, 64], [1, 57], [8, 57], [57, 57]), 58: ([57, 64], [2, 58], [16, 58], [49, 58]), 59: ([57, 64], [3, 59], [24, 59], [41, 59]), 60: ([57, 64], [4, 60], [32, 60], [33, 60]), 61: ([57, 64], [5, 61], [40, 61], [25, 61]), 62: ([57, 64], [6, 62], [48, 62], [17, 62]), 63: ([57, 64], [7, 63], [56, 63], [9, 63]), 64: ([57, 64], [8, 64], [64, 64], [1, 64])}

BLOCK_CONDITION = {}
for i in range(1, 65, 1):
    BLOCK_CONDITION[i] = ["", "", ""]

KNOCKED_PIECE_W_POSITION = {'0': (720, 100), '1': (750, 100), '2': (780, 100), '3': (810, 100), '4': (840, 100), '5': (870, 100), '6': (900, 100), '7': (
    930, 100), '8': (720, 150), '9': (750, 150), '10': (780, 150), '11': (810, 150), '12': (840, 150), '13': (870, 150), '14': (900, 150), '15': (930, 150)}
KNOCKED_PIECE_B_POSITION = {'0': (720, 550), '1': (750, 550), '2': (780, 550), '3': (810, 550), '4': (840, 550), '5': (870, 550), '6': (900, 550), '7': (
    930, 550), '8': (720, 600), '9': (750, 600), '10': (780, 600), '11': (810, 600), '12': (840, 600), '13': (870, 600), '14': (900, 600), '15': (930, 600)}
KNOCKED_PIECE_W = []
KNOCKED_PIECE_B = []

GAME_SOUNDS['Key-moved'] = pygame.mixer.Sound("Gallery/audio/key_moved2.wav")
GAME_SOUNDS['GameOver'] = pygame.mixer.Sound("Gallery/audio/Game Over.mp3")
GAME_SOUNDS['GameOverfinal'] = pygame.mixer.Sound(
    "Gallery/audio/Game Over final.mp3")


RED = (218, 18, 18, 99)  # Red Shadow
GREEN = (18, 218, 38, 99)  # Green Shadow
AQUA = (18, 211, 218, 99)  # Aqua Shadow
GOLDEN = (249, 228, 2)  # Golden color
SILVER = (218, 218, 218)  # SILVER COLOR
SHADOW_SILVER = (112, 112, 112)  # SHADOW_SILVER
SHADOW_GOLD = (154, 120, 0)  # shadow gold
TURN = "0"
MOVECOUNTER = 1
HISTORY = {MOVECOUNTER: PIECE_POSITION.copy()}
KNOCKED_WHITE_HISTORY = {MOVECOUNTER: KNOCKED_PIECE_W.copy()}
KNOCKED_BLACK_HISTORY = {MOVECOUNTER: KNOCKED_PIECE_B.copy()}
move_ = True


def Facebook():
    url = "https://www.facebook.com/anirudhya.das.104"
    chrome_path = "C://Program Files//Google//Chrome//Application//Chrome.exe %s"
    webbrowser.get(chrome_path).open(url)


def Instagram():
    url = "https://www.instagram.com/anirudhya_______das_______/"
    chrome_path = "C://Program Files//Google//Chrome//Application//Chrome.exe %s"
    webbrowser.get(chrome_path).open(url)


def jsonKeys2int(x):
    if isinstance(x, dict):
        return {int(k): v for k, v in x.items()}
    return x


def Blit_Pieces(Piece, array):
    Piece_name = Piece.split('-')[0]
    Piece_code = Piece.split('-')[1]
    SCREEN.blit(GAME_SPRITES[f'{Piece_name}']
                [int(Piece_code)], (array[0], array[1]))


def Blit_Text(text, color, x, y, font_name, font_size, bold, italic):
    font = pygame.font.SysFont(font_name, font_size, bold, italic)
    text_blit = font.render(text, True, color)
    SCREEN.blit(text_blit, [x, y])


def Print_Box(color_, rect):
    # This Function for Tranparent Box
    surface = SCREEN
    color = color_
    shape_surf = pygame.Surface(pygame.Rect(rect).size, pygame.SRCALPHA)
    pygame.draw.rect(shape_surf, color, shape_surf.get_rect())
    surface.blit(shape_surf, rect)


def Move_Generator(Box_Number, Piece):
    Piece_Name = Piece.split('-')[0]
    if Piece_Name == "Armies":
        x = []
        if Piece.split('-')[1] == "0":
            if (Box_Number+8) <= BLOCK_RANGE[Box_Number][1][1]:
                if PIECE_POSITION[Box_Number+8] == "":
                    x.append(Box_Number+8)
            if (Box_Number+7) <= BLOCK_RANGE[Box_Number][2][1]:
                if PIECE_POSITION[Box_Number+7] != "":
                    if PIECE_POSITION[Box_Number+7].split("-")[1] == "1":
                        x.append(Box_Number+7)
            if (Box_Number+9) <= BLOCK_RANGE[Box_Number][3][1]:
                if PIECE_POSITION[Box_Number+9] != "":
                    if PIECE_POSITION[Box_Number+9].split("-")[1] == "1":
                        x.append(Box_Number+9)
        else:
            if (Box_Number-8) >= BLOCK_RANGE[Box_Number][1][0]:
                if PIECE_POSITION[Box_Number-8] == "":
                    x.append(Box_Number-8)
            if (Box_Number-7) >= BLOCK_RANGE[Box_Number][2][0]:
                if PIECE_POSITION[Box_Number-7] != "":
                    if PIECE_POSITION[Box_Number-7].split("-")[1] == "0":
                        x.append(Box_Number-7)
            if (Box_Number-9) >= BLOCK_RANGE[Box_Number][3][0]:
                if PIECE_POSITION[Box_Number-9] != "":
                    if PIECE_POSITION[Box_Number-9].split("-")[1] == "0":
                        x.append(Box_Number-9)
        return x
    if Piece_Name in ['Kings']:
        x = []
        if (Box_Number+1) <= BLOCK_RANGE[Box_Number][0][1]:
            x.append(Box_Number+1)
        if (Box_Number-1) >= BLOCK_RANGE[Box_Number][0][0]:
            x.append(Box_Number-1)
        if (Box_Number+8) <= BLOCK_RANGE[Box_Number][1][1]:
            x.append(Box_Number+8)
        if (Box_Number-8) >= BLOCK_RANGE[Box_Number][1][0]:
            x.append(Box_Number-8)
        if (Box_Number+9) <= BLOCK_RANGE[Box_Number][3][1]:
            x.append(Box_Number+9)
        if (Box_Number-9) >= BLOCK_RANGE[Box_Number][3][0]:
            x.append(Box_Number-9)
        if (Box_Number+7) <= BLOCK_RANGE[Box_Number][2][1]:
            x.append(Box_Number+7)
        if (Box_Number-7) >= BLOCK_RANGE[Box_Number][2][0]:
            x.append(Box_Number-7)
        return x
    elif Piece_Name == 'Horses':
        x = []
        if (Box_Number+16) <= BLOCK_RANGE[Box_Number][1][1]:
            if (Box_Number+15) >= BLOCK_RANGE[Box_Number+16][0][0]:
                x.append(Box_Number+15)
            if (Box_Number+17) <= BLOCK_RANGE[Box_Number+16][0][1]:
                x.append(Box_Number+17)
        if (Box_Number-16) >= BLOCK_RANGE[Box_Number][1][0]:
            if (Box_Number-15) <= BLOCK_RANGE[Box_Number-16][0][1]:
                x.append(Box_Number-15)
            if (Box_Number-17) >= BLOCK_RANGE[Box_Number-16][0][0]:
                x.append(Box_Number-17)
        if (Box_Number+2) <= BLOCK_RANGE[Box_Number][0][1]:
            if (Box_Number+10) <= BLOCK_RANGE[Box_Number+2][1][1]:
                x.append(Box_Number+10)
            if (Box_Number-6) >= BLOCK_RANGE[Box_Number+2][1][0]:
                x.append(Box_Number-6)
        if (Box_Number-2) >= BLOCK_RANGE[Box_Number][0][0]:
            if (Box_Number+6) <= BLOCK_RANGE[Box_Number-2][1][1]:
                x.append(Box_Number+6)
            if (Box_Number-10) >= BLOCK_RANGE[Box_Number-2][1][0]:
                x.append(Box_Number-10)
        return x
    elif Piece_Name == 'Elephants':
        x = []
        for_rf = Box_Number
        for_lf = Box_Number
        for_rb = Box_Number
        for_lb = Box_Number
        while for_rf < BLOCK_RANGE[Box_Number][3][1]:
            for_rf += 9
            if PIECE_POSITION[for_rf] != "":
                if PIECE_POSITION[for_rf].split('-')[1] == Piece.split('-')[1]:
                    break
                elif PIECE_POSITION[for_rf].split('-')[1] != Piece.split('-')[1]:
                    x.append(for_rf)
                    break
                else:
                    pass
            x.append(for_rf)
        while for_rb > BLOCK_RANGE[Box_Number][3][0]:
            for_rb -= 9
            if PIECE_POSITION[for_rb] != "":
                if PIECE_POSITION[for_rb].split('-')[1] == Piece.split('-')[1]:
                    break
                elif PIECE_POSITION[for_rb].split('-')[1] != Piece.split('-')[1]:
                    x.append(for_rb)
                    break
                else:
                    pass
            x.append(for_rb)
        while for_lf < BLOCK_RANGE[Box_Number][2][1]:
            for_lf += 7
            if PIECE_POSITION[for_lf] != "":
                if PIECE_POSITION[for_lf].split('-')[1] == Piece.split('-')[1]:
                    break
                elif PIECE_POSITION[for_lf].split('-')[1] != Piece.split('-')[1]:
                    x.append(for_lf)
                    break
                else:
                    pass
            x.append(for_lf)
        while for_lb > BLOCK_RANGE[Box_Number][2][0]:
            for_lb -= 7
            if PIECE_POSITION[for_lb] != "":
                if PIECE_POSITION[for_lb].split('-')[1] == Piece.split('-')[1]:
                    break
                elif PIECE_POSITION[for_lb].split('-')[1] != Piece.split('-')[1]:
                    x.append(for_lb)
                    break
                else:
                    pass
            x.append(for_lb)
        return x
    elif Piece_Name == 'Boats':
        x = []
        for_rf = Box_Number
        for_lf = Box_Number
        for_rb = Box_Number
        for_lb = Box_Number
        while for_rf < BLOCK_RANGE[Box_Number][0][1]:
            for_rf += 1
            if PIECE_POSITION[for_rf] != "":
                if PIECE_POSITION[for_rf].split('-')[1] == Piece.split('-')[1]:
                    break
                elif PIECE_POSITION[for_rf].split('-')[1] != Piece.split('-')[1]:
                    x.append(for_rf)
                    break
                else:
                    pass
            x.append(for_rf)
        while for_rb > BLOCK_RANGE[Box_Number][0][0]:
            for_rb -= 1
            if PIECE_POSITION[for_rb] != "":
                if PIECE_POSITION[for_rb].split('-')[1] == Piece.split('-')[1]:
                    break
                elif PIECE_POSITION[for_rb].split('-')[1] != Piece.split('-')[1]:
                    x.append(for_rb)
                    break
                else:
                    pass
            x.append(for_rb)
        while for_lf < BLOCK_RANGE[Box_Number][1][1]:
            for_lf += 8
            if PIECE_POSITION[for_lf] != "":
                if PIECE_POSITION[for_lf].split('-')[1] == Piece.split('-')[1]:
                    break
                elif PIECE_POSITION[for_lf].split('-')[1] != Piece.split('-')[1]:
                    x.append(for_lf)
                    break
                else:
                    pass
            x.append(for_lf)
        while for_lb > BLOCK_RANGE[Box_Number][1][0]:
            for_lb -= 8
            if PIECE_POSITION[for_lb] != "":
                if PIECE_POSITION[for_lb].split('-')[1] == Piece.split('-')[1]:
                    break
                elif PIECE_POSITION[for_lb].split('-')[1] != Piece.split('-')[1]:
                    x.append(for_lb)
                    break
                else:
                    pass
            x.append(for_lb)
        return x
    elif Piece_Name == "Queens":
        x = []
        for_rf = Box_Number
        for_lf = Box_Number
        for_rb = Box_Number
        for_lb = Box_Number
        while for_rf < BLOCK_RANGE[Box_Number][3][1]:
            for_rf += 9
            if PIECE_POSITION[for_rf] != "":
                if PIECE_POSITION[for_rf].split('-')[1] == Piece.split('-')[1]:
                    break
                elif PIECE_POSITION[for_rf].split('-')[1] != Piece.split('-')[1]:
                    x.append(for_rf)
                    break
                else:
                    pass
            x.append(for_rf)
        while for_rb > BLOCK_RANGE[Box_Number][3][0]:
            for_rb -= 9
            if PIECE_POSITION[for_rb] != "":
                if PIECE_POSITION[for_rb].split('-')[1] == Piece.split('-')[1]:
                    break
                elif PIECE_POSITION[for_rb].split('-')[1] != Piece.split('-')[1]:
                    x.append(for_rb)
                    break
                else:
                    pass
            x.append(for_rb)
        while for_lf < BLOCK_RANGE[Box_Number][2][1]:
            for_lf += 7
            if PIECE_POSITION[for_lf] != "":
                if PIECE_POSITION[for_lf].split('-')[1] == Piece.split('-')[1]:
                    break
                elif PIECE_POSITION[for_lf].split('-')[1] != Piece.split('-')[1]:
                    x.append(for_lf)
                    break
                else:
                    pass
            x.append(for_lf)
        while for_lb > BLOCK_RANGE[Box_Number][2][0]:
            for_lb -= 7
            if PIECE_POSITION[for_lb] != "":
                if PIECE_POSITION[for_lb].split('-')[1] == Piece.split('-')[1]:
                    break
                elif PIECE_POSITION[for_lb].split('-')[1] != Piece.split('-')[1]:
                    x.append(for_lb)
                    break
                else:
                    pass
            x.append(for_lb)
        for_rf = Box_Number
        for_lf = Box_Number
        for_rb = Box_Number
        for_lb = Box_Number
        while for_rf < BLOCK_RANGE[Box_Number][0][1]:
            for_rf += 1
            if PIECE_POSITION[for_rf] != "":
                if PIECE_POSITION[for_rf].split('-')[1] == Piece.split('-')[1]:
                    break
                elif PIECE_POSITION[for_rf].split('-')[1] != Piece.split('-')[1]:
                    x.append(for_rf)
                    break
                else:
                    pass
            x.append(for_rf)
        while for_rb > BLOCK_RANGE[Box_Number][0][0]:
            for_rb -= 1
            if PIECE_POSITION[for_rb] != "":
                if PIECE_POSITION[for_rb].split('-')[1] == Piece.split('-')[1]:
                    break
                elif PIECE_POSITION[for_rb].split('-')[1] != Piece.split('-')[1]:
                    x.append(for_rb)
                    break
                else:
                    pass
            x.append(for_rb)
        while for_lf < BLOCK_RANGE[Box_Number][1][1]:
            for_lf += 8
            if PIECE_POSITION[for_lf] != "":
                if PIECE_POSITION[for_lf].split('-')[1] == Piece.split('-')[1]:
                    break
                elif PIECE_POSITION[for_lf].split('-')[1] != Piece.split('-')[1]:
                    x.append(for_lf)
                    break
                else:
                    pass
            x.append(for_lf)
        while for_lb > BLOCK_RANGE[Box_Number][1][0]:
            for_lb -= 8
            if PIECE_POSITION[for_lb] != "":
                if PIECE_POSITION[for_lb].split('-')[1] == Piece.split('-')[1]:
                    break
                elif PIECE_POSITION[for_lb].split('-')[1] != Piece.split('-')[1]:
                    x.append(for_lb)
                    break
                else:
                    pass
            x.append(for_lb)
        return x
    else:
        return []


def On_Click(event):
    global move_
    if event.type == MOUSEBUTTONDOWN:
        for Box_Number, Box_Area in BLOCK_AREA.items():
            rect_ = Rect(Box_Area)
            if rect_.collidepoint(event.pos):
                for i in BLOCK_CONDITION.keys():
                    if i == Box_Number:
                        BLOCK_CONDITION[Box_Number][0] = "0"
                    else:
                        BLOCK_CONDITION[i][0] = ""
                if PIECE_POSITION[Box_Number] != '':
                    if PIECE_POSITION[Box_Number].split('-')[1] == TURN:
                        return_list = Move_Generator(
                            Box_Number, PIECE_POSITION[Box_Number])
                        for i in BLOCK_CONDITION.keys():
                            if i in return_list:
                                if PIECE_POSITION[i] == '' or PIECE_POSITION[i].split('-')[1] == ('1' if PIECE_POSITION[Box_Number].split('-')[1] == '0' else '0'):
                                    if PIECE_POSITION[i] != '':
                                        BLOCK_CONDITION[i][1] = ""
                                        BLOCK_CONDITION[i][2] = "2"
                                    else:
                                        BLOCK_CONDITION[i][1] = "1"
                                    move_ = False
                            else:
                                BLOCK_CONDITION[i][1] = ""
                    else:
                        for i in BLOCK_CONDITION.keys():
                            if BLOCK_CONDITION[i][1] != "":
                                BLOCK_CONDITION[i][1] = ""
                            if BLOCK_CONDITION[i][2] != "":
                                BLOCK_CONDITION[i][2] = ""
                else:
                    for i in BLOCK_CONDITION.keys():
                        if BLOCK_CONDITION[i][1] != "":
                            BLOCK_CONDITION[i][1] = ""
                        if BLOCK_CONDITION[i][2] != "":
                            BLOCK_CONDITION[i][2] = ""


def On_Click2(event):
    global TURN, MOVECOUNTER, HISTORY
    for Box_Number, Box_Area in BLOCK_AREA.items():
        rect_ = Rect(Box_Area)
        if rect_.collidepoint(event.pos):
            if BLOCK_CONDITION[Box_Number][1] == "1" or BLOCK_CONDITION[Box_Number][2] == "2":
                for j in BLOCK_CONDITION.keys():
                    if BLOCK_CONDITION[j][0] == "0":
                        if PIECE_POSITION[Box_Number] != "":
                            KNOCKED_PIECE_W.append(PIECE_POSITION[Box_Number]) if PIECE_POSITION[Box_Number].split(
                                "-")[1] == "0" else KNOCKED_PIECE_B.append(PIECE_POSITION[Box_Number])
                            # print(KNOCKED_PIECE_W, KNOCKED_PIECE_B)
                        GAME_SOUNDS['Key-moved'].play()
                        PIECE_POSITION[j], PIECE_POSITION[Box_Number] = '', PIECE_POSITION[j]
                        BLOCK_CONDITION[j][0] = ""
                        for i in BLOCK_CONDITION.keys():
                            if BLOCK_CONDITION[i][1] != "":
                                BLOCK_CONDITION[i][1] = ""
                            if BLOCK_CONDITION[i][2] != "":
                                BLOCK_CONDITION[i][2] = ""
                        TURN = '0' if TURN == '1' else '1'
                        MOVECOUNTER += 1
                        HISTORY.update({MOVECOUNTER: PIECE_POSITION.copy()})
                        KNOCKED_WHITE_HISTORY.update({MOVECOUNTER: KNOCKED_PIECE_W.copy()})
                        KNOCKED_BLACK_HISTORY.update({MOVECOUNTER: KNOCKED_PIECE_B.copy()})
            else:
                On_Click(event)


def Multiplayer_Mode():
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    pygame.display.set_caption("Leisure Chess")
    GAME_SOUNDS['GameOverfinal'].stop()
    GAME_SOUNDS['GameOver'].stop()
    GAME_SPRITES['Kings'] = (
        pygame.image.load("Gallery\\sprites\\King_White.png").convert_alpha(),
        pygame.image.load("Gallery\\sprites\\King_Black.png").convert_alpha(),
        pygame.image.load(
            "Gallery\\sprites\\Small_pieces\\King_White.png").convert_alpha(),
        pygame.image.load(
            "Gallery\\sprites\\Small_pieces\\King_Black.png").convert_alpha()
    )
    GAME_SPRITES['Queens'] = (
        pygame.image.load("Gallery\\sprites\\Queen_White.png").convert_alpha(),
        pygame.image.load("Gallery\\sprites\\Queen_Black.png").convert_alpha(),
        pygame.image.load(
            "Gallery\\sprites\\Small_pieces\\Queen_White.png").convert_alpha(),
        pygame.image.load(
            "Gallery\\sprites\\Small_pieces\\Queen_Black.png").convert_alpha()
    )
    GAME_SPRITES['Armies'] = (
        pygame.image.load("Gallery\\sprites\\Army_White.png").convert_alpha(),
        pygame.image.load("Gallery\\sprites\\Army_Black.png").convert_alpha(),
        pygame.image.load(
            "Gallery\\sprites\\Small_pieces\\Army_White.png").convert_alpha(),
        pygame.image.load(
            "Gallery\\sprites\\Small_pieces\\Army_Black.png").convert_alpha()
    )
    GAME_SPRITES['Horses'] = (
        pygame.image.load("Gallery\\sprites\\Horse_White.png").convert_alpha(),
        pygame.image.load("Gallery\\sprites\\Horse_Black.png").convert_alpha(),
        pygame.image.load(
            "Gallery\\sprites\\Small_pieces\\Horse_White.png").convert_alpha(),
        pygame.image.load(
            "Gallery\\sprites\\Small_pieces\\Horse_Black.png").convert_alpha()
    )
    GAME_SPRITES['Elephants'] = (
        pygame.image.load(
            "Gallery\\sprites\\Elephant_White.png").convert_alpha(),
        pygame.image.load(
            "Gallery\\sprites\\Elephant_Black.png").convert_alpha(),
        pygame.image.load(
            "Gallery\\sprites\\Small_pieces\\Elephant_White.png").convert_alpha(),
        pygame.image.load(
            "Gallery\\sprites\\Small_pieces\\Elephant_Black.png").convert_alpha()
    )
    GAME_SPRITES['Boats'] = (
        pygame.image.load("Gallery\\sprites\\Boat_White.png").convert_alpha(),
        pygame.image.load("Gallery\\sprites\\Boat_Black.png").convert_alpha(),
        pygame.image.load(
            "Gallery\\sprites\\Small_pieces\\Boat_White.png").convert_alpha(),
        pygame.image.load(
            "Gallery\\sprites\\Small_pieces\\Boat_Black.png").convert_alpha()
    )
    GAME_GRAPHICS['Black'] = pygame.image.load(
        "Gallery\\sprites\\Grp_des\\black3.png").convert_alpha()
    GAME_GRAPHICS['White'] = pygame.image.load(
        "Gallery\\sprites\\Grp_des\\white4.png").convert_alpha()
    GAME_GRAPHICS['Logo'] = pygame.image.load(
        "Gallery\\sprites\\Grp_des\\logo3-3.png").convert_alpha()
    GAME_GRAPHICS['Close'] = pygame.image.load(
        "Gallery\\sprites\\Grp_des\\cross.png").convert_alpha()
    GAME_GRAPHICS['Back'] = pygame.image.load(
        "Gallery\\sprites\\Grp_des\\back.png").convert_alpha()
    GAME_GRAPHICS['Prev'] = pygame.image.load(
        "Gallery\\sprites\\Grp_des\\previous.png").convert_alpha()
    GAME_GRAPHICS['Nxt'] = pygame.image.load(
        "Gallery\\sprites\\Grp_des\\next.png").convert_alpha()
    GAME_GRAPHICS['Load'] = pygame.image.load(
        "Gallery\\sprites\\Grp_des\\reload2-1.png").convert_alpha()
    btn_back = Rect(710, 20, 50, 35)
    btn_close = Rect(950, 20, 30, 30)
    btn_reload = Rect(840, 660, 40, 30)
    btn_pre = Rect(725, 660, 22, 30)
    btn_nxt = Rect(955, 660, 22, 30)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if btn_back.collidepoint(event.pos):
                    Menu_Page()
                if btn_close.collidepoint(event.pos):
                    with open("Game_State.txt", "w") as f:
                        str_ = json.dumps(PIECE_POSITION)
                        f.write(str_)
                    with open("Game Turn.txt", "w") as f:
                        f.write(TURN)
                    with open("White Knocked.txt", "w") as f:
                        str_ = json.dumps(KNOCKED_PIECE_W)
                        f.write(str_)
                    with open("Black Knocked.txt", "w") as f:
                        str_ = json.dumps(KNOCKED_PIECE_B)
                        f.write(str_)
                    Reset_game()
                    Menu_Page()
                if btn_reload.collidepoint(event.pos):
                    Reset_game()
                if btn_pre.collidepoint(event.pos):
                    Previous()
                if btn_nxt.collidepoint(event.pos):
                    Next()
            if move_ == True:
                On_Click(event)
            else:
                if event.type == MOUSEBUTTONDOWN:
                    On_Click2(event)

            for i in KNOCKED_PIECE_W+KNOCKED_PIECE_B:
                if i in ["Kings-0", "Kings-1"]:
                    GAME_SOUNDS['GameOver'].play()
                    with open("Game_State.txt", "w") as f:
                        str_ = ""
                        f.write(str_)
                    with open("Game Turn.txt", "w") as f:
                        str_ = ""
                        f.write(str_)
                    with open("White Knocked.txt", "w") as f:
                        str_ = ""
                        f.write(str_)
                    with open("Black Knocked.txt", "w") as f:
                        str_ = ""
                        f.write(str_)
                    Game_Over(i.split('-')[1])

        SCREEN.blit(BACKGROUND, (700, 0))
        SCREEN.blit(BOARD, (0, 0))
        if TURN == "0":
            SCREEN.blit(GAME_GRAPHICS['White'], (700, 100))
        else:
            SCREEN.blit(GAME_GRAPHICS['Black'], (700, 415))
        SCREEN.blit(GAME_GRAPHICS['Logo'], (730, 275))
        SCREEN.blit(GAME_GRAPHICS['Close'], (930, 0))
        SCREEN.blit(GAME_GRAPHICS['Back'], (700, 10))
        SCREEN.blit(GAME_GRAPHICS['Nxt'], (930, 645))
        SCREEN.blit(GAME_GRAPHICS['Prev'], (700, 645))
        SCREEN.blit(GAME_GRAPHICS['Load'], (807, 640))

        for i in BLOCK_AREA.keys():
            if BLOCK_CONDITION[i][1] == "1":
                Print_Box(GREEN, BLOCK_AREA[i])
            if BLOCK_CONDITION[i][2] == "2":
                Print_Box(RED, BLOCK_AREA[i])
            if BLOCK_CONDITION[i][0] == "0":
                Print_Box(AQUA, BLOCK_AREA[i])
        for i in PIECE_POSITION.keys():
            if PIECE_POSITION[i] != '':
                Blit_Pieces(PIECE_POSITION[i], BLOCK_POSITION[f'{i}'])
        for index, piece_name in enumerate(KNOCKED_PIECE_W):
            Blit_Pieces(
                f"{piece_name.split('-')[0]}-{int(piece_name.split('-')[1])+2}", KNOCKED_PIECE_W_POSITION[f'{index}'])
        for index, piece_name in enumerate(KNOCKED_PIECE_B):
            Blit_Pieces(
                f"{piece_name.split('-')[0]}-{int(piece_name.split('-')[1])+2}", KNOCKED_PIECE_B_POSITION[f'{index}'])
        pygame.display.update()
        FPSCLOCK.tick(FPS)


def Menu_Page():
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    pygame.display.set_caption("Leisure Chess")
    GAME_SOUNDS['GameOver'].stop()
    GAME_SOUNDS['GameOverfinal'].stop()
    GAME_SOUNDS['GameOverfinal'].play()
    Menu_Sprites = {}
    btns = {}

    Menu_Sprites['background_image'] = [pygame.image.load(
        "Gallery\\not final\\Menu_Back_3_Dull.jpg").convert_alpha(), (-100, 0)]
    Menu_Sprites['background_wood'] = [pygame.image.load(
        "Gallery\\sprites\\BACKGROUND___.jpg").convert_alpha(), (237.5, 0)]
    Menu_Sprites['logo_image'] = [pygame.image.load(
        "Gallery\\sprites\\Menu\\logo.png").convert_alpha(), (305, 0)]
    Menu_Sprites['single'] = [pygame.image.load(
        "Gallery\\sprites\\Menu\\single_player.png").convert_alpha(), (200, 75)]
    Menu_Sprites['multi'] = [pygame.image.load(
        "Gallery\\sprites\\Menu\\multiplayer.png").convert_alpha(), (200, 175)]
    Menu_Sprites['setting'] = [pygame.image.load(
        "Gallery\\sprites\\Menu\\setting.png").convert_alpha(), (200, 275)]
    Menu_Sprites['logo_depth'] = [pygame.image.load(
        "Gallery\\sprites\\GameOver\\logo-2.png").convert_alpha(), (830, 575)]
    Menu_Sprites['copy_right'] = [pygame.image.load(
        "Gallery\\sprites\\About\\creator-line.png").convert_alpha(), (750, 570)]
    Menu_Sprites['about'] = [pygame.image.load(
        "Gallery\\sprites\\Menu\\about_us.png").convert_alpha(), (195, 375)]
    btns['single'] = (380, 265, 240, 70)
    btns['multi'] = (380, 365, 240, 70)
    btns['setting'] = (380, 465, 240, 70)
    btns['about'] = (400, 565, 200, 70)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                for item in btns:
                    click_area = Rect(btns[item])
                    if click_area.collidepoint(event.pos):
                        if item == 'single':
                            Single_Player_Mode()
                        elif item == 'multi':
                            Resume_Menu()
                        elif item == 'setting':
                            Settings()
                        else:
                            About_us()

        for item in Menu_Sprites:
            SCREEN.blit(Menu_Sprites[item][0], Menu_Sprites[item][1])

        pygame.display.update()
        FPSCLOCK.tick(FPS)


def Loading():
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    pygame.display.set_caption("Leisure Chess")
    Menu_Sprites = {}
    Menu_Sprites['background_image'] = [pygame.image.load(
        "Gallery\\not final\\Menu_Back_3_Dull.jpg").convert_alpha(), (-100, 0)]
    Menu_Sprites['loading'] = [pygame.image.load(
        "Gallery\\sprites\\Grp_des\\loading.png").convert_alpha(), (300, 220)]
    Menu_Sprites['logo_depth'] = [pygame.image.load(
        "Gallery\\sprites\\GameOver\\logo-2.png").convert_alpha(), (830, 575)]
    Menu_Sprites['copy_right'] = [pygame.image.load(
        "Gallery\\sprites\\About\\creator-line.png").convert_alpha(), (750, 570)]
    for item in Menu_Sprites:
        SCREEN.blit(Menu_Sprites[item][0], Menu_Sprites[item][1])
    pygame.display.update()
    FPSCLOCK.tick(FPS)
    time.sleep(2)
    Multiplayer_Mode()


def Single_Player_Mode():
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    pygame.display.set_caption("Leisure Chess")
    Menu_Sprites = {}
    Menu_Sprites['background_image'] = [pygame.image.load(
        "Gallery\\not final\\Menu_Back_3_Dull.jpg").convert_alpha(), (-100, 0)]
    Menu_Sprites['statement'] = [pygame.image.load(
        "Gallery\\sprites\\Grp_des\\single_player_mode.png").convert_alpha(), (0, -25)]
    Menu_Sprites['goBack'] = [pygame.image.load(
        "Gallery\\sprites\\Grp_des\\go.png").convert_alpha(), (-350, 520)]
    Menu_Sprites['logo_depth'] = [pygame.image.load(
        "Gallery\\sprites\\GameOver\\logo-2.png").convert_alpha(), (830, 575)]
    Menu_Sprites['copy_right'] = [pygame.image.load(
        "Gallery\\sprites\\About\\creator-line.png").convert_alpha(), (750, 570)]

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                Menu_Page()
        for item in Menu_Sprites:
            SCREEN.blit(Menu_Sprites[item][0], Menu_Sprites[item][1])
        pygame.display.update()
        FPSCLOCK.tick(FPS)


def Resume_Menu():
    global PIECE_POSITION, TURN, KNOCKED_PIECE_B, KNOCKED_PIECE_W
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    pygame.display.set_caption("Leisure Chess")
    resume_menu = {}
    resume_menu['background_image'] = [pygame.image.load(
        "Gallery\\not final\\Menu_Back_3_Dull.jpg").convert_alpha(), (-100, 0)]
    resume_menu['background_wood'] = [pygame.image.load(
        "Gallery\\sprites\\BACKGROUND___.jpg").convert_alpha(), (237.5, 0)]
    resume_menu['logo_image'] = [pygame.image.load(
        "Gallery\\sprites\\About\\logo3-2.png").convert_alpha(), (400, 50)]
    resume_menu['head'] = [pygame.image.load(
        "Gallery\\sprites\\Resume Menu\\head.png").convert_alpha(), (200, -20)]
    resume_menu['continue'] = [pygame.image.load(
        "Gallery\\sprites\\Resume Menu\\continue.png").convert_alpha(), (200, 230)]
    resume_menu['new_game'] = [pygame.image.load(
        "Gallery\\sprites\\Resume Menu\\new_game.png").convert_alpha(), (200, 130)]
    resume_menu['logo_depth'] = [pygame.image.load(
        "Gallery\\sprites\\GameOver\\logo-2.png").convert_alpha(), (420, 570)]
    resume_menu['copy_right'] = [pygame.image.load(
        "Gallery\\sprites\\About\\creator-line.png").convert_alpha(), (340, 570)]
    resume_menu['back'] = [pygame.image.load(
        "Gallery\\sprites\\About\\back.png").convert_alpha(), (0, 0)]
    back_btn = Rect(15, 10, 45, 35)
    new_game_btn = Rect(375, 320, 250, 70)
    continue_btn = Rect(375, 420, 250, 70)

    with open("Game_State.txt", "r") as f:
        x = f.read()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if back_btn.collidepoint(event.pos):
                    Menu_Page()
                with open("Game_State.txt", "r") as f:
                    content = f.read()
                    if content != '':
                        if continue_btn.collidepoint(event.pos):
                            dict_cont = json.loads(
                                content, object_hook=jsonKeys2int)
                            PIECE_POSITION = dict_cont.copy()
                            with open("Game Turn.txt", "r") as p:
                                cont = p.read()
                                if cont != "":
                                    TURN = cont
                                    with open("Black Knocked.txt", "r") as k:
                                        lst = k.read()
                                        up_lst = json.loads(lst)
                                        KNOCKED_PIECE_B = up_lst
                                    with open("White Knocked.txt", "r") as l:
                                        _lst = l.read()
                                        _up_lst = json.loads(_lst)
                                        KNOCKED_PIECE_W = _up_lst.copy()
                                    Loading()
                if new_game_btn.collidepoint(event.pos):
                    Loading()
        for item in resume_menu:
            if x != '':
                SCREEN.blit(resume_menu[item][0], resume_menu[item][1])
            else:
                if item != 'continue':
                    SCREEN.blit(resume_menu[item][0], resume_menu[item][1])

        pygame.display.update()
        FPSCLOCK.tick(FPS)


def About_us():
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    pygame.display.set_caption("Leisure Chess")

    About = {}
    buttons = {}

    About['background_image'] = [pygame.image.load(
        "Gallery\\not final\\Menu_Back_3_Dull.jpg").convert_alpha(), (-100, 0)]
    About['background_wood'] = [pygame.image.load(
        "Gallery\\sprites\\BACKGROUND___.jpg").convert_alpha(), (237.5, 0)]
    About['logo_image'] = [pygame.image.load(
        "Gallery\\sprites\\About\\logo3-2.png").convert_alpha(), (400, 0)]
    About['head'] = [pygame.image.load(
        "Gallery\\sprites\\About\\About us heading.png").convert_alpha(), (200, -70)]
    About['version'] = [pygame.image.load(
        "Gallery\\sprites\\About\\version.png").convert_alpha(), (250, 70)]
    About['game_name'] = [pygame.image.load(
        "Gallery\\sprites\\About\\Game_name.png").convert_alpha(), (200, 90)]
    About['creator'] = [pygame.image.load(
        "Gallery\\sprites\\About\\creator-.png").convert_alpha(), (300, 250)]
    About['creator_name'] = [pygame.image.load(
        "Gallery\\sprites\\About\\creator-name.png").convert_alpha(), (200, 230)]
    About['follow_us'] = [pygame.image.load(
        "Gallery\\sprites\\About\\follow-us.png").convert_alpha(), (300, 400)]
    About['facebook'] = [pygame.image.load(
        "Gallery\\sprites\\About\\facebook.png").convert_alpha(), (160, 420)]
    About['logo_depth'] = [pygame.image.load(
        "Gallery\\sprites\\GameOver\\logo-2.png").convert_alpha(), (830, 575)]
    About['instagram'] = [pygame.image.load(
        "Gallery\\sprites\\About\\instagram.png").convert_alpha(), (320, 420)]
    About['copy_right'] = [pygame.image.load(
        "Gallery\\sprites\\About\\creator-line.png").convert_alpha(), (750, 570)]
    About['back'] = [pygame.image.load(
        "Gallery\\sprites\\About\\back.png").convert_alpha(), (0, 0)]

    buttons['fb'] = (345, 585, 130, 40)
    buttons['insta'] = (505, 585, 130, 40)
    buttons['beck'] = (15, 15, 45, 30)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                for item in buttons:
                    clicks = Rect(buttons[item])
                    if clicks.collidepoint(event.pos):
                        if item == 'beck':
                            Menu_Page()
                        elif item == 'fb':
                            Facebook()
                        else:
                            Instagram()

        for item in About:
            SCREEN.blit(About[item][0], About[item][1])

        pygame.display.update()
        FPSCLOCK.tick(FPS)


def Settings():
    global VOLUME, FPS, TURN
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    pygame.display.set_caption("Leisure Chess")

    About = {}
    buttons = {}

    About['background_image'] = [pygame.image.load(
        "Gallery\\not final\\Menu_Back_3_Dull.jpg").convert_alpha(), (-100, 0)]
    About['background_wood'] = [pygame.image.load(
        "Gallery\\sprites\\BACKGROUND___.jpg").convert_alpha(), (237.5, 0)]
    About['logo_image'] = [pygame.image.load(
        "Gallery\\sprites\\About\\logo3-2.png").convert_alpha(), (400, -20)]
    About['head'] = [pygame.image.load(
        "Gallery\\sprites\\About\\Setting Heading.png").convert_alpha(), (200, -90)]
    About['graphics'] = [pygame.image.load(
        "Gallery\\sprites\\About\\graphics.png").convert_alpha(), (0, 70)]
    About['high'] = [pygame.image.load(
        "Gallery\\sprites\\About\\high.png").convert_alpha(), (-120, 130)]
    About['normal'] = [pygame.image.load(
        "Gallery\\sprites\\About\\normal.png").convert_alpha(), (0, 130)]
    About['low'] = [pygame.image.load(
        "Gallery\\sprites\\About\\low.png").convert_alpha(), (120, 130)]
    About['sound'] = [pygame.image.load(
        "Gallery\\sprites\\About\\Sound.png").convert_alpha(), (0, 190)]
    About['off'] = [pygame.image.load(
        "Gallery\\sprites\\About\\off.png").convert_alpha(), (-75, 250)]
    About['on'] = [pygame.image.load(
        "Gallery\\sprites\\About\\on.png").convert_alpha(), (60, 250)]
    About['first move'] = [pygame.image.load(
        "Gallery\\sprites\\About\\First_move.png").convert_alpha(), (0, 250)]
    About['black'] = [pygame.image.load(
        "Gallery\\sprites\\About\\black.png").convert_alpha(), (-75, 390)]
    About['white'] = [pygame.image.load(
        "Gallery\\sprites\\About\\white.png").convert_alpha(), (60, 390)]
    About['logo_depth'] = [pygame.image.load(
        "Gallery\\sprites\\GameOver\\logo-2.png").convert_alpha(), (420, 575)]
    About['copy_right'] = [pygame.image.load(
        "Gallery\\sprites\\About\\creator-line.png").convert_alpha(), (340, 570)]
    About['back'] = [pygame.image.load(
        "Gallery\\sprites\\About\\back.png").convert_alpha(), (0, 0)]

    buttons['beck'] = (15, 15, 45, 30)
    buttons['high'] = (330, 260, 100, 40)
    buttons['nor'] = (450, 260, 100, 40)
    buttons['low'] = (570, 260, 100, 40)
    buttons['off'] = (375, 380, 100, 40)
    buttons['on'] = (510, 380, 100, 40)
    buttons['black'] = (375, 520, 105, 40)
    buttons['white'] = (510, 520, 105, 40)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                for item in buttons:
                    clicks = Rect(buttons[item])
                    if clicks.collidepoint(event.pos):
                        if item == 'beck':
                            Menu_Page()
                        elif item == 'high':
                            FPS = 90
                        elif item == 'nor':
                            FPS = 60
                        elif item == 'low':
                            FPS = 30
                        elif item == 'off':
                            VOLUME = 0.0
                            GAME_SOUNDS['Key-moved'].set_volume(VOLUME)
                            GAME_SOUNDS['GameOver'].set_volume(VOLUME)
                            GAME_SOUNDS['GameOverfinal'].set_volume(VOLUME)
                        elif item == 'black':
                            TURN = "1"
                        elif item == 'white':
                            TURN = "0"
                        else:
                            VOLUME = 1.0
                            GAME_SOUNDS['Key-moved'].set_volume(VOLUME)
                            GAME_SOUNDS['GameOver'].set_volume(VOLUME)
                            GAME_SOUNDS['GameOverfinal'].set_volume(VOLUME)

        for item in About:
            SCREEN.blit(About[item][0], About[item][1])

        pygame.display.update()
        FPSCLOCK.tick(FPS)


def Reset_game():
    global move_, TURN, KNOCKED_PIECE_B, KNOCKED_PIECE_W, PIECE_POSITION, PIECE_POSITION_XT, MOVECOUNTER, HISTORY
    move_ = True
    TURN = "0"
    KNOCKED_PIECE_W = []
    KNOCKED_PIECE_B = []
    PIECE_POSITION = {1: 'Boats-0', 2: 'Elephants-0', 3: 'Horses-0', 4: 'Queens-0', 5: 'Kings-0', 6: 'Horses-0', 7: 'Elephants-0', 8: 'Boats-0', 9: 'Armies-0', 10: 'Armies-0', 11: 'Armies-0', 12: 'Armies-0', 13: 'Armies-0', 14: 'Armies-0', 15: 'Armies-0', 16: 'Armies-0', 17: '', 18: '', 19: '', 20:
                      '', 21: '', 22: '', 23: '', 24: '', 25: '', 26: '', 27: '', 28: '', 29: '', 30: '', 31: '', 32: '', 33: '', 34: '', 35: '', 36: '', 37: '', 38: '',
                      39: '', 40: '', 41: '', 42: '', 43: '', 44: '', 45: '', 46: '', 47: '', 48: '', 49: 'Armies-1', 50: 'Armies-1', 51: 'Armies-1', 52: 'Armies-1', 53: 'Armies-1', 54: 'Armies-1', 55: 'Armies-1', 56: 'Armies-1', 57:
                      'Boats-1', 58: 'Elephants-1', 59: 'Horses-1', 60: 'Queens-1', 61: 'Kings-1', 62: 'Horses-1', 63: 'Elephants-1', 64: 'Boats-1'}
    MOVECOUNTER = 1
    HISTORY = {MOVECOUNTER: PIECE_POSITION.copy()}


def Previous():
    global MOVECOUNTER, HISTORY, PIECE_POSITION, TURN, KNOCKED_PIECE_B, KNOCKED_PIECE_W
    if MOVECOUNTER > 1:
        MOVECOUNTER -= 1
    else:
        MOVECOUNTER = 1
    PIECE_POSITION.clear()
    PIECE_POSITION = HISTORY[MOVECOUNTER].copy()
    KNOCKED_PIECE_B = KNOCKED_BLACK_HISTORY[MOVECOUNTER].copy()
    KNOCKED_PIECE_W = KNOCKED_WHITE_HISTORY[MOVECOUNTER].copy()
    if MOVECOUNTER % 2 == 0:
        TURN = "1"
    else:
        TURN = "0"


def Next():
    global MOVECOUNTER, HISTORY, PIECE_POSITION, TURN, KNOCKED_PIECE_B, KNOCKED_PIECE_W
    if MOVECOUNTER < len(HISTORY.keys()):
        MOVECOUNTER += 1
    else:
        MOVECOUNTER = len(HISTORY.keys())

    PIECE_POSITION.clear()
    PIECE_POSITION = HISTORY[MOVECOUNTER].copy()
    KNOCKED_PIECE_B = KNOCKED_BLACK_HISTORY[MOVECOUNTER].copy()
    KNOCKED_PIECE_W = KNOCKED_WHITE_HISTORY[MOVECOUNTER].copy()
    if MOVECOUNTER % 2 == 0:
        TURN = "1"
    else:
        TURN = "0"


def Game_Over(white_won):
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    pygame.display.set_caption("Leisure Chess")
    GAME_SOUNDS['GameOver'].play()
    game_over = {}
    btns = {}
    Reset_game()
    game_over['background_image'] = [pygame.image.load(
        "Gallery\\not final\\Menu_Back_3_Dull.jpg").convert_alpha(), (-100, 0)]
    game_over['background_wood'] = [pygame.image.load(
        "Gallery\\sprites\\BACKGROUND___.jpg").convert_alpha(), (237.5, 0)]
    game_over['logo_image'] = [pygame.image.load(
        "Gallery\\sprites\\About\\logo3-2.png").convert_alpha(), (400, 50)]
    game_over['head'] = [pygame.image.load(
        "Gallery\\sprites\\GameOver\\Heading.png").convert_alpha(), (200, -20)]
    game_over['white_win'] = [pygame.image.load(
        "Gallery\\sprites\\GameOver\\white-win-line.png").convert_alpha(), (275, 170)]
    game_over['black_win'] = [pygame.image.load(
        "Gallery\\sprites\\GameOver\\black-win-line.png").convert_alpha(), (275, 170)]
    game_over['btn_play'] = [pygame.image.load(
        "Gallery\\sprites\\GameOver\\btn-play-agian.png").convert_alpha(), (80, 230)]
    game_over['btn_menu'] = [pygame.image.load(
        "Gallery\\sprites\\GameOver\\btn-menu.png").convert_alpha(), (310, 230)]
    game_over['logo_depth'] = [pygame.image.load(
        "Gallery\\sprites\\GameOver\\logo-2.png").convert_alpha(), (420, 570)]
    game_over['copy_right'] = [pygame.image.load(
        "Gallery\\sprites\\About\\creator-line.png").convert_alpha(), (340, 570)]

    btns['play_again'] = (280, 420, 205, 70)
    btns['menu'] = (510, 420, 205, 70)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                for item in btns:
                    clicks = Rect(btns[item])
                    if clicks.collidepoint(event.pos):
                        if item == 'play_again':
                            Multiplayer_Mode()
                        else:
                            Menu_Page()
        for item in game_over:
            if white_won == "1":
                if item != 'black_win':
                    SCREEN.blit(game_over[item][0], game_over[item][1])
            else:
                if item != 'white_win':
                    SCREEN.blit(game_over[item][0], game_over[item][1])
        pygame.display.update()
        FPSCLOCK.tick(FPS)


if __name__ == '__main__':
    Menu_Page()
