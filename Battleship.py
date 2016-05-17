from graphics import *
import math
from shipclass import playerships
from AI import ai, AI_ships
from popup import popupwindow, winnerspopup, updatehighscores


def playerboard():
    xstep = 50
    ystep = 50
    win = GraphWin("TestGraphics", 1300, 650)                       # draw the windows
    win.setBackground("blue")                                       # make it blue
    for x in range(50, 550, xstep):                                 # draw the grid
        for y in range(125, 625, ystep):
            a = Rectangle(Point(x, y), Point(x+xstep, y+ystep))
            a.draw(win)
    enemyboard(win)                                                 # draw the enemy board
    name = popupwindow(win)                                         # gets the players name
    playertitle = Text(Point(300, 25), name + "'s Board")
    playertitle.draw(win)
    shipssunk = Text(Point(650, 200), "Enemy ships sunk")
    shipssunk.draw(win)
    enemytile = AI_ships(win)                                       # draw the enemy ships and store the coordinates
    shiptile = playerships(win)                                     # draw the player ships and store the coordinates
    score = 0                                                       # keeps track of the score (number of shots taken)
    while len(shiptile) != 0 and len(enemytile) !=0:                # start the fight and test for a win
        score += 1
        shots(win, enemytile, name, score)                          # calls the shots function for the player
        if len(shiptile) != 0 and len(enemytile) !=0:
            ai(win, shiptile)                                       # calls the shots function for the ai
    win.getMouse()
    win.close()


def enemyboard(win):                                                # build the enemy board
    xstep = 50
    ystep = 50
    for x in range(750, 1250, xstep):
        for y in range(125, 625, ystep):
            a = Rectangle(Point(x, y), Point(x + xstep, y + ystep))
            a.draw(win)
    opponentheader = Text(Point(1000, 25), "Enemy Board")
    opponentheader.draw(win)


def shots(win, shiplocation, name, score):                                            # function for the players shots
    if len(shiplocation) != 0:
        mark = win.getMouse()
        mark.x = 25+(50*math.floor(mark.x/50))
        mark.y = (50*math.floor((mark.y+25)/50))
        shot = Circle(Point(mark.x, mark.y), 20)                                                     # center the shot
        hit = False
        if 750 <= mark.x <= 1250 and 125 <= mark.y <= 625:                                 # is the shot on the board?
            for shipspace in shiplocation:                                                    # start testing for a hit
                for point in shipspace:
                    if [mark.x, mark.y] == point:
                        hit = True
                        shot.setFill("Red")
                        shot.draw(win)
                        shipspace.remove(point)
                        hittext = Text(Point(650, 75), "Hit!")
                        hittext.setSize(28)
                        hittext.setTextColor("red")
                        hittext.setStyle("bold")
                        hittext.draw(win)
                        time.sleep(.6)
                        hittext.undraw()
                        if len(shipspace) == 1:                                               # test for a sunken ship
                            time.sleep(.5)
                            shipsunk = Text(Point(650, 75), "You sunk their " + shipspace[0] + "!")
                            shipsunk.setSize(28)
                            shipsunk.setTextColor("red")
                            shipsunk.setStyle("bold")
                            shipname = Text(Point(650, 350 - (len(shiplocation) * 25)), shipspace[0])
                            shipsunk.draw(win)
                            time.sleep(1.5)
                            shipsunk.undraw()
                            time.sleep(.25)
                            shipname.draw(win)
                            shiplocation.remove(shipspace)

            if hit is True:                                                                             # test for a win
                if len(shiplocation) == 0:
                    winner = Text(Point(650, 75), "You Won!!")
                    winner.setSize(30)
                    winner.setStyle("bold")
                    winner.setTextColor("Green")
                    winner.draw(win)
                    updatehighscores(name, score)                                               # check for a high score
                    time.sleep(3)
                    winner.undraw()
                    winnerspopup(win)                            # ask to display high score. if yes, popup high scores
            else:                                                                                      # test for a miss
                shot.setFill("White")
                shot.draw(win)
                misstext = Text(Point(650, 75), "Miss!")
                misstext.setSize(28)
                misstext.setTextColor("white")
                misstext.draw(win)
                time.sleep(.6)
                misstext.undraw()
        else:                                                                     # if the shot is outside area, retry
            shots(win, shiplocation, name, score)
playerboard()