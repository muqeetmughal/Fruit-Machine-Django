import logging
import random
import numpy

from django.shortcuts import get_object_or_404

from app.models import UniqueCode, Prize

# Get an instance of a logger
from app.symbol import Symbol

logger = logging.getLogger(__name__)


def is_code_valid(code) -> bool:
    try:
        ucode = UniqueCode.objects.get(code=code)
        if ucode.used is not True:
            return True
    except Exception as e:
        logger.error(e)
    return False


def set_code_used(code, state):
    try:
        ucode = UniqueCode.objects.get(code=code)
        ucode.used = state
        ucode.save()
    except Exception as e:
        logger.error(e)


def get_prize(pk) -> object:
    try:
        return get_object_or_404(Prize, pk=pk)
    except Exception as e:
        logger.error(e)
    return None


def get_prize_result():
    """
    Prizes Odd:
    https://docs.google.com/spreadsheets/d/1eSlEaMWPp9xBceZczfQ3lIeaJF8CKRwQeKL1wmH4DYU/edit?usp=sharing
    |--------|--------------|--------------------------
    |PRIZEID |    RESULT    |        ODD              |
    |--------|--------------|--------------------------
    |   1    | 3 DIAMONDS   |  1000:1	0.001	0.100%
    |   2    | 2 DIAMONDS   |  500:1	0.002	0.200%
    |   3    | 1 DIAMOND    |  200:1	0.005	0.500%
    |   4    | 3 DOLLARS    |  150:1	0.0066	0.660%
    |   5    | 3 BARS       |  100:1	0.01	1.000%
    |   6    | 3 SEVENS     |  75:1	    0.0133	1.330%
    |   7    | 3 BELLS      |  	        0.015	1.500%
    |   8    | 3 HORSESHOES |  	        0.0175	1.750%
    |   9    | 3 LEAF       |  50:1	    0.02	2.000%
    |   10   | 3 HEARTS     |  	        0.0225	2.250%
    |   11   | 3 WATERMELONS|  	        0.025	2.500%
    |   12   | 3 CHERRIES   |  	        0.0275	2.750%
    |   13   | 3 GRAPES     |  	        0.03	3.000%
    |   14   | 3 LEMONS     |  	        0.04	4.000%
    |   15   | 3 ORANGES    |  20:1	    0.05	5.000%
    |   16   | 3 BANANAS    |  10:1	    0.1	    10.000%
    |   17   |    LOSE      |  	        0.6146	61.460%
    """
    r = numpy.random.choice(numpy.arange(0, 17), p=[
        0.0001,
        0.0005,
        0.002,
        0.003,
        0.007,
        0.008,
        0.009,
        0.0095,
        0.01,
        0.0125,
        0.015,
        0.0175,
        0.02,
        0.025,
        0.06,
        0.07,
        0.7309,
    ])

    return r+1


def get_slot_result(r):
    if r == 1:
        return Symbol.DIAMOND.value, Symbol.DIAMOND.value, Symbol.DIAMOND.value
    elif r == 2:
        return Symbol.DIAMOND.value, Symbol.DIAMOND.value, get_random_symbol_with_no_diamond()
    elif r == 3:
        return Symbol.DIAMOND.value, get_random_symbol_with_no_diamond(), get_random_symbol_with_no_diamond()
    elif r == 4:
        return Symbol.DOLLAR.value, Symbol.DOLLAR.value, Symbol.DOLLAR.value
    elif r == 5:
        return Symbol.BAR.value, Symbol.BAR.value, Symbol.BAR.value
    elif r == 6:
        return Symbol.SEVEN.value, Symbol.SEVEN.value, Symbol.SEVEN.value
    elif r == 7:
        return Symbol.BELL.value, Symbol.BELL.value, Symbol.BELL.value
    elif r == 8:
        return Symbol.HORSESHOE.value, Symbol.HORSESHOE.value, Symbol.HORSESHOE.value
    elif r == 9:
        return Symbol.LEAF.value, Symbol.LEAF.value, Symbol.LEAF.value
    elif r == 10:
        return Symbol.HEART.value, Symbol.HEART.value, Symbol.HEART.value
    elif r == 11:
        return Symbol.WATERMELON.value, Symbol.WATERMELON.value, Symbol.WATERMELON.value
    elif r == 12:
        return Symbol.CHERRY.value, Symbol.CHERRY.value, Symbol.CHERRY.value
    elif r == 13:
        return Symbol.GRAPE.value, Symbol.GRAPE.value, Symbol.GRAPE.value
    elif r == 14:
        return Symbol.LEMON.value, Symbol.LEMON.value, Symbol.LEMON.value
    elif r == 15:
        return Symbol.ORANGE.value, Symbol.ORANGE.value, Symbol.ORANGE.value
    elif r == 16:
        return Symbol.BANANA.value, Symbol.BANANA.value, Symbol.BANANA.value
    else:
        # LOSE
        return get_random_lose_result()


def get_random_symbol_with_no_diamond():
    symbols = list(Symbol)
    symbols.remove(Symbol.DIAMOND)
    return random.choice(symbols).value


def get_random_lose_result():
    symbols = list(Symbol)
    symbols.remove(Symbol.DIAMOND)

    l = list(Symbol)
    l.remove(Symbol.DIAMOND)

    for s in l:
        symbols.append(s)

    s1 = random.choice(symbols)
    symbols.remove(s1)

    s2 = random.choice(symbols)
    symbols.remove(s2)

    s3 = random.choice(symbols)

    return s1.value, s2.value, s3.value


