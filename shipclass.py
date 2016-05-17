from graphics import *
import math


def playerships(win):                                                   # These are all the players ships
    patrol = ship("Patrolboat", 2, "green", win, "point")
    battleship = ship("Battleship", 4, "green", win, "point")
    destroyer = ship("Destroyer", 3, "green", win, "point")
    submarine = ship("Submarine", 3, "green", win, "point")
    carrier = ship("Aircraft Carrier", 5, "green", win, "flat")
    patrol.placement()
    destroyer.placement()
    submarine.placement()
    battleship.placement()
    carrier.placement()
    return permanentlocation                                            # returns all the players ships coordinates to the main function
permanentlocation = []                                                  # the empty list that will hold the coordinates


class ship:                                                         #stuff for making the players ships
    def __init__(self, name, length, color, graph, bowshape):
        self.name = name
        self.length = length
        self.color = color
        self.win = graph
        self.bowshape = bowshape                                    # this is used to distinguish the aircraft carrier from the other ships

    def placement(self):
        placementerror = False                                      # this is the flag for incorrect placement
        shipname = Text(Point(300, 75), "Place your "+ self.name)   # tells you to place your ship
        win = self.win
        len = self.length
        shipname.draw(self.win)
        bow = win.getMouse()                                        # clicky for bow
        bow.x = 25 + (50 * math.floor(bow.x / 50))
        bow.y = (50 * math.floor((bow.y + 25) / 50))
        stern = win.getMouse()                                      # clicky for stern
        stern.x = 25 + (50 * math.floor(stern.x / 50))
        stern.y = (50 * math.floor((stern.y + 25) / 50))
        count = 0                                                   # used to check each tile that the ships takes up for overlap and to add it to the permanent locations list
        templocation = []                                           # a temporary list for the individual ships tiles while overlap is checked
        if self.bowshape=="flat":                                   # because aircraft carrier...
            shape = 0
            shape2 = 125
            shape3 = 125
        elif self.bowshape == "point":
            shape = 25
            shape2 = 0
            shape3 = 25
        if bow.x == stern.x:                                                                             # vertical test
            if bow.y < stern.y:                                                                       # top to bottom
                bow.y -= 25
                if (bow.y + len * 50) <= 625 and 125 <= bow.y and 50 <= bow.x <= 550:             # inside the grid test
                    ship = Polygon(Point(bow.x, bow.y), Point(bow.x - 15, bow.y + shape), Point(bow.x - 15, bow.y + len * 25 + shape + shape2),
                                     Point(bow.x, bow.y + len*50), Point(bow.x + 15, bow.y + len * 25 + shape + shape2),
                                     Point(bow.x + 15, bow.y + shape))
                    while count != len:
                        for shipspace in permanentlocation:                                          # check for overlap
                            for tile in shipspace:
                                if [bow.x,bow.y + (50 * count) + 25] == tile:
                                    placementerror = True             # if the overlap check is failed a flag is raised
                        templocation.append([bow.x,bow.y + (50 * count) + 25])
                        count += 1
                else:
                    placementerror = True                 # if any part of the ship is outside the grid a flag is raised
            else:                                                                                       # bottom to top
                bow.y += 25
                if bow.y <= 625 and 125 <= (bow.y - len*50) and 50 <= bow.x <= 550:               # inside the grid test
                    ship = Polygon(Point(bow.x, bow.y), Point(bow.x + 15, bow.y - shape),
                                     Point(bow.x + 15, bow.y - len * 25 - shape - shape2), Point(bow.x, bow.y - len*50),
                                     Point(bow.x - 15, bow.y - len * 25 - shape - shape2), Point(bow.x - 15, bow.y - shape))
                    while count != len:
                        for shipspace in permanentlocation:                                          # check for overlap
                            for tile in shipspace:
                                if [bow.x, bow.y - (50 * count) - 25] == tile:
                                    placementerror = True
                        templocation.append([bow.x, bow.y - (50 * count) - 25])
                        count += 1
                else:
                    placementerror = True
        else:
            if bow.x < stern.x:                                                                         # left to right
                bow.x -= 25
                if 50 <= bow.x and (bow.x + len * 50) <= 550 and 125 <= bow.y <= 625:             # inside the grid test
                    ship = Polygon(Point(bow.x, bow.y), Point(bow.x + shape, bow.y - 15), Point(bow.x + len * 25 + shape3, bow.y - 15),
                            Point(bow.x + len * 50, bow.y), Point(bow.x + len * 25 + shape3, bow.y + 15), Point(bow.x + shape, bow.y + 15 ))
                    while count != len:
                        for shipspace in permanentlocation:                                       # check for overlap
                            for tile in shipspace:
                                if [bow.x + (50 * count) + 25, bow.y] == tile:
                                    placementerror = True
                        templocation.append([bow.x + (50 * count) + 25, bow.y])
                        count += 1
                else:
                    placementerror = True
            else:                                                                                       # right to left
                bow.x += 25
                if 50 <= (bow.x - len * 50) and bow.x <= 550 and 125 <= bow.y <= 625:             # inside the grid test
                    ship = Polygon(Point(bow.x, bow.y), Point(bow.x - shape, bow.y - 15),
                         Point(bow.x - len * 25 - shape3, bow.y - 15),
                         Point(bow.x - len * 50, bow.y), Point(bow.x - len * 25 - shape3, bow.y + 15),
                         Point(bow.x - shape, bow.y + 15))
                    while count != len:
                        for shipspace in permanentlocation:                                         # check for overlap
                            for tile in shipspace:
                                if [bow.x - (50 * count) - 25, bow.y] == tile:
                                    placementerror = True
                        templocation.append([bow.x - (50 * count) - 25, bow.y])
                        count += 1
                else:
                    placementerror = True
        if placementerror is False:
            ship.setFill("green")                                                              # makes the ships green
            templocation.append(self.name)                                     # adds the ships name to the coordinates
            permanentlocation.append(templocation)                   # adds the ships coordinates to the permanent list
            ship.draw(win)                                                                             # draws the ship
            shipname.undraw()                                                                   # removes the ship name
        else:                                                                                   # redo the ship drawing
            shipname.undraw()
            self.placement()