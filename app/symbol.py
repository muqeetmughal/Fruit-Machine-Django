from enum import Enum


class Symbol(Enum):
    """
    Class to represent each possible symbol in the slot machine.
    Each number represents the background texture y coordinate from the reel image.
    """
    LEAF = 109
    DIAMOND = 220
    HORSESHOE = 331
    DOLLAR = 442
    ORANGE = 553
    BELL = 664
    WATERMELON = 775
    HEART = 886
    LEMON = 997
    CHERRY = 1108
    BANANA = 1219
    GRAPE = 1330
    BAR = 1441
    SEVEN = 1552
