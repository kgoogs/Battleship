from graphics import *


def popupwindow(win):
    ask = Text(Point(650, 75), "Enter your name")                                                    # asks for the name
    popup = Entry(Point(650, 100), 15)                                                 # coordinates for the entry point
    ask.draw(win)                                                                                  # draws the question
    popup.draw(win)                                                                         # draws the name entry point
    while win.checkKey() != 'Return':                                                     # makes the blinking red dot
        time.sleep(.3)
        circle = Circle(Point(565, 100), 10)
        circle.setFill("Red")
        circle.draw(win)
        time.sleep(.3)
        circle.undraw()
    name = popup.getText()
    ask.undraw()
    popup.undraw()
    return name                                                                    # gives the name to the main program


def updatehighscores(name, score):                                                              # Updates the highscores
    newtop10 = []
    temp = []
    player = name
    playerscore = str(score)
    highscore = False                                                                            # flag for a high score

    newscores = open("winners.txt", "r")
    for x in range(10):                                                          # checks if the player got a high score
        readname = str(newscores.readline())
        readscore = str(newscores.readline())
        readscore = readscore.rstrip("\n")
        if playerscore < readscore:
            highscore = True
    newscores.close()

    if highscore is True:                                                 # adds the players score if it is a high score
        newscores = open("winners.txt", "a")
        newscores.write(player + "\n")
        newscores.write(playerscore + "\n")
        newscores.close()
        scores = open("winners.txt", "r")
        for x in range(11):
            readname = str(scores.readline())
            readscore = str(scores.readline())
            readscore = readscore.rstrip("\n")
            readname = readname.rstrip("\n")
            temp.append([readscore, readname])
        scores.close()
        temp.sort()                                                                            # sorts the high scores
        for x in temp:
            newtop10.append([x[1], x[0]])
        new = open("winners.txt", "w")                                                 # rewrites the high scores file
        count = 0
        while count != 10:
            x = newtop10[count]
            new.write(str(x[0]) + "\n")
            new.write(str(x[1]) + "\n")
            count += 1
        new.close()


def winnerspopup(win):
    ask = Text(Point(650, 50), "Would you like to see the high scores?")     # prompts the player to see the high scores
    button = Rectangle(Point(550, 70), Point(625, 110))                                         # draws the yes button
    ask.draw(win)
    button.draw(win)
    yes = Text(Point(585, 90), "Yes")
    yes.draw(win)
    button2 = Rectangle(Point(675, 70), Point(750, 110))                                        # draws the no button
    button2.draw(win)
    no = Text(Point(710, 90), "No")
    no.draw(win)
    mark = win.getMouse()                                                                       # wait for a mouseclick
    button.undraw()
    button2.undraw()
    yes.undraw()
    no.undraw()
    ask.undraw()

    if 550 <= mark.x <= 625 and 70 <= mark.y <= 110:                                 # check if the player clicked yes
        winnerwindow = GraphWin("High scores", 500, 500)
        winnerwindow.setBackground("Grey")
        title = Text(Point(250, 50), "Top 10 Winners")
        title.draw(winnerwindow)
        scores = open("winners.txt", "r")
        for x in range(10):
            readname = str(scores.readline())
            readscore = str(scores.readline())
            readname = readname.rstrip("\n")
            readscore = readscore.rstrip("\n")
            names = Text(Point(250, 100 + (x * 25)), readname + "     " + readscore)
            names.draw(winnerwindow)
        scores.close()
        winnerwindow.getMouse()
        winnerwindow.close()
    elif 675 <= mark.x <= 750 and 70 <= mark.y <= 110:                                  # check if the player clicked no
        choice = "no"
    else:                                                # if the player clicked outside the buttons then re-prompt them
        winnerspopup(win)