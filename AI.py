from graphics import *
import random


def AI_ships(graph):                                                                        # these are the AIs ships
    win = graph
    aipatrol = ai_ship("Patrolboat", 2, "green", win, "point")
    aibattleship = ai_ship("Battleship", 4, "green", win, "point")
    aidestroyer = ai_ship("Destroyer", 3, "green", win, "point")
    aisubmarine = ai_ship("Submarine", 3, "green", win, "point")
    aicarrier = ai_ship("Aircraft Carrier", 5, "green", win, "flat")
    aipatrol.placement()
    aidestroyer.placement()
    aisubmarine.placement()
    aibattleship.placement()
    aicarrier.placement()
    return aipermanentlocation                                       # return the AI ship locations to the main program
aipermanentlocation = []


class ai_ship:                                                                                  # stuff for making ships
    def __init__(self, name, length, color, graph, bowshape):
        self.name = name
        self.length = length
        self.color = color
        self.win = graph
        self.bowshape = bowshape

    def placement(self):
        placementerror = False
        win = self.win
        len = self.length
        bowx, bowy = airandom()
        sternx, sterny = airandom()
        count = 0
        aitemplocation = []
        if self.bowshape == "flat":                                                     # because aircraft carrier...
            shape = 0
            shape2 = 125
            shape3 = 125
        elif self.bowshape == "point":
            shape = 25
            shape2 = 0
            shape3 = 25
        if bowx == sternx:                                                                              # vertical test
            if bowy < sterny:                                                                            # top to bottom
                bowy -= 25
                if (bowy + len * 50) <= 625 and 125 <= bowy and 750 <= bowx <= 1250:             # inside the grid test
                    ship = Polygon(Point(bowx, bowy), Point(bowx - 15, bowy + shape), Point(bowx - 15, bowy + len * 25 + shape + shape2),
                                     Point(bowx, bowy + len*50), Point(bowx + 15, bowy + len * 25 + shape + shape2),
                                     Point(bowx + 15, bowy + shape))
                    while count != len:
                        for shipspace in aipermanentlocation:                                     # check for overlap
                            for tile in shipspace:
                                if [bowx, bowy + (50 * count) + 25] == tile:
                                    placementerror = True
                        aitemplocation.append([bowx, bowy + (50 * count) + 25])
                        count += 1
                else:
                    placementerror = True
            else:                                                                                    # bottom to top
                bowy += 25
                if bowy <= 625 and 125 <= (bowy - len*50) and 750 <= bowx <= 1250:               # inside the grid test
                    ship = Polygon(Point(bowx, bowy), Point(bowx + 15, bowy - shape),
                                     Point(bowx + 15, bowy - len * 25 - shape - shape2), Point(bowx, bowy - len*50),
                                     Point(bowx - 15, bowy - len * 25 - shape - shape2), Point(bowx - 15, bowy - shape))
                    while count != len:
                        for shipspace in aipermanentlocation:                                    # check for overlap
                            for tile in shipspace:
                                if [bowx, bowy - (50 * count) - 25] == tile:
                                    placementerror = True
                        aitemplocation.append([bowx, bowy - (50 * count) - 25])
                        count += 1
                else:
                    placementerror = True
        elif bowy == sterny:
            if bowx < sternx:                                                                        # left to right
                bowx -= 25
                if 750 <= bowx and (bowx + len * 50) <= 1250 and 125 <= bowy <= 625:             # inside the grid test
                    ship = Polygon(Point(bowx, bowy), Point(bowx + shape, bowy - 15), Point(bowx + len * 25 + shape3, bowy - 15),
                            Point(bowx + len * 50, bowy), Point(bowx + len * 25 + shape3, bowy + 15), Point(bowx + shape, bowy + 15 ))
                    while count != len:
                        for shipspace in aipermanentlocation:                                     # check for overlap
                            for tile in shipspace:
                                if [bowx + (50 * count) + 25, bowy] == tile:
                                    placementerror = True
                        aitemplocation.append([bowx + (50 * count) + 25, bowy])
                        count += 1
                else:
                    placementerror = True
            else:                                                                                     # right to left
                bowx += 25
                if 750 <= (bowx - len * 50) and bowx <= 1250 and 125 <= bowy <= 625:             # inside the grid test
                    ship = Polygon(Point(bowx, bowy), Point(bowx - shape, bowy - 15),
                         Point(bowx - len * 25 - shape3, bowy - 15),
                         Point(bowx - len * 50, bowy), Point(bowx - len * 25 - shape3, bowy + 15),
                         Point(bowx - shape, bowy + 15))
                    while count != len:
                        for shipspace in aipermanentlocation:                                      # check for overlap
                            for tile in shipspace:
                                if [bowx - (50 * count) -25, bowy] == tile:
                                    placementerror = True
                        aitemplocation.append([bowx - (50 * count) -25, bowy])
                        count += 1
                else:
                    placementerror = True
        else:
            placementerror = True
        if placementerror is False:
            ship.setFill("red")
            aitemplocation.append(self.name)
            aipermanentlocation.append(aitemplocation)
            # ship.draw(win)                                                  # draws the ship (uncomment for easy mode)
        else:
            self.placement()


def airandom():
    tiledictionary = {}
    for y in range(0, 10):
        for x in range(1, 11):
            z = y * 10 + x
            tiledictionary[z] = [725 + (50 * x), 100 + (50 * (y + 1))]  # gives the correct x, y coordinates for the tile
    number = list(tiledictionary.keys())
    index = random.randint(0, len(number) - 1)
    shotcoordinates = tiledictionary.pop(number[index])
    number.remove(number[index])
    x = shotcoordinates[0]
    y = shotcoordinates[1]
    return x, y


tiledictionary = {}
for y in range(0, 10):
    for x in range(1, 11):
        z = y * 10 + x
        tiledictionary[z] = [25+(50*x), 100+(50*(y + 1))]           # gives the correct x, y coordinates for the tile
number = list(tiledictionary.keys())                                                    # holds all the tile coordinates


def ai(win, shiplocation):
    index = random.randint(0, len(number) - 1)
    shotcoordinates = tiledictionary.pop(number[index])
    number.remove(number[index])
    x = shotcoordinates[0]
    y = shotcoordinates[1]
    shot = Circle(Point(x, y), 20)
    hit = False
    if 50 <= x <= 550 and 125 <= y <= 625:
        for shipspace in shiplocation:
            for point in shipspace:
                if [x, y] == point:
                    hit = True                                                                          # test for a hit
                    shipspace.remove(point)
                    if len(shipspace) == 1:                                                     # test for a sunken ship
                        shipsunk = Text(Point(650, 75), "Your " + shipspace[0] + " was sunk!")
                        shipsunk.setSize(28)
                        shipsunk.setTextColor("red")
                        shipsunk.setStyle("bold")
                        shipsunk.draw(win)
                        time.sleep(1)                                                             # time between shots
                        shipsunk.undraw()
                        time.sleep(.25)
                        shiplocation.remove(shipspace)
        if hit is True:
            shot.setFill("Red")
            if len(shiplocation) == 0:                                                              # check for a loss
                loser = Text(Point(650, 75), "You Lost!!")
                loser.setSize(30)
                loser.setStyle("bold")
                loser.setTextColor("Red")
                loser.draw(win)
        else:
            shot.setFill("White")
        shot.draw(win)
    else:
        ai(win, shiplocation)