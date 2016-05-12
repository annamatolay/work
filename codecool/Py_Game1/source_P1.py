#This is created by Edina Berkes and Pál Matolay.
#Py_Game1.3

import curses, time, random

screen = curses.initscr()
curses.noecho() #Nem látszik a bevitt karakter
curses.curs_set(0) #Nincs kurzor
screen.keypad(1)
screen.nodelay(1) #Nincs késés
#'0' és '1' létrehozása, kezdőpont
BARRIER = "0"
barriery, barrierx = 5, 79
PLAYER = "1"
playerY, playerX = 5, 5

while True:
    screen.clear()
    #Itt kezdődik az 1-es(megjelenítés, mozgatás)
    screen.addstr(playerY, playerX, PLAYER)
    screen.refresh()
    event = screen.getch()
    if event == ord("q"): break
    elif event == curses.KEY_UP:
        playerY += -1
        screen.erase()
        screen.addstr(playerY,playerX,PLAYER)
        screen.getch()
    elif event == curses.KEY_DOWN:
        playerY += 1
        screen.erase()
        screen.addstr(playerY,playerX,PLAYER)
    #Itt kezdődik az 0-ás(megjelenítés, folyamatos mozgás)
    screen.addstr(barriery, barrierx, BARRIER)
    screen.refresh()
    barrierx += -1
    if barrierx == -1:
        barrierx = 79
    time.sleep(0.03)

screen.getch()
curses.endwin()
