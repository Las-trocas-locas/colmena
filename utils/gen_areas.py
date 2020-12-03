import math

def generateHexGrid(itemCount, this):
    size = 0
    pushed = 0

    if (itemCount <= 7):
        size = 3
    elif (itemCount <= 19):
        size = 5
    elif (itemCount <= 37):
        size = 7
    elif (itemCount <= 61) :
        size = 9
  
    radius = this["radius"] / size
    toReturn = []
    ang30 = 30 * (math.pi/180)
    xOff = math.cos(ang30) * (radius)
    yOff = math.sin(ang30) * (radius)
    half = math.floor(size / 2)

    for row in range(size):
        cols = size - abs(row - half)

        for col in range(cols):
            x = this["x"] + xOff * (col * 2 + 1 - cols)
            y = this["y"] + yOff * (row - half) * 3
            toReturn.append([x,y])
            pushed = pushed + 1
            if (pushed == itemCount):
                return toReturn
    return toReturn


def radio(p1,p2):
    return math.sqrt(  math.pow(abs(p1["x"] - p2["x"]),2) + math.pow(abs(p1["x"] - p2["x"]),2))

if __name__ == "__main__" :
    r = radio({"x": 19.267676882004178, "y": -99.33173919690998}, {"x":19.307947227320163, "y": -98.96197511230774})
    print(r)
    print(generateHexGrid(7, {"radius":r, "x":19.321588822147294,"y":-99.1448001932143}))