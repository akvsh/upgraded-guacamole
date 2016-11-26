import random

backcolour = (255, 255, 255)
boardcolour = (0, 0, 0)
lightblue = (102, 255, 255)
blue = (0, 0, 128)
green = (0, 255, 0)
brown = (153, 76, 0)
purple = (138, 6, 255)
pink = (255, 180, 180)
orange = (255, 215, 0)

DaihansFaveColour = (152, 152, 211)
AkashColour = (240, 42, 0)
Shit = (113, 119, 30)

def generateColour(seed=False):
    hashMap = random.random()
    if seed: 
        if (hashMap) <= 0.33:
            return AkashColour
        elif (hashMap) <= 0.66:
            return lightblue
        else:
            return orange
    if (hashMap) <= 0.5:
        return pink
    else:
        return DaihansFaveColour
