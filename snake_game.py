#!/usr/bin/env python

#NoCopyrightCode --- Feel free to use and distribute

#Author : Parikshit Sharma

#The Classic Snake Game

#Use arrows to navigate, space bar to pause and Esc to exit

#Uncomment line    to make the boundaries inaccessible

#pip install curses for dependencies. That's it let's play!

import curses
from curses import KEY_RIGHT, KEY_LEFT, KEY_DOWN, KEY_UP
from random import randint

curses.initscr()
window = curses.newwin(30, 90, 0, 0)										   #Initialize size of canvas
window.keypad(1)															   #Turn on keypad translation
curses.noecho()																   #Turn off echoing of char (printing)
curses.curs_set(0)															   #Set cursor to invisible
window.border(0)															   #Set default borders
window.nodelay(1)										                       #getch is non blocking(no wait for input)


key= KEY_LEFT																   #Initialize direction of snake                    
score= 0																	   #Initialize score to zero

snake = [[5,20],[5,21], [5,22]]  										       #Initialize the position of the snake
food = [15,30]																   #Initialize the position of the food

window.addch(food[0], food[1], '@')											   #Prints an '*' for food position

while key != 27:															   #While Esc key is not presed
	window.border(0)
	window.addstr(0, 5, 'Score: '+ str(score)+ ' ')			                   #Prints the score on top of the screen
	window.addstr(0, 30, 'Classic Snake Game')										   #Prints the title of the game
	window.timeout(int(150 - (len(snake)/5 + len(snake)/10)%120))			   #Decreases the timeout ms as the length incr

	prevKey = key
	event = window.getch()
	key = key if key == -1 else event 										   #-1 corresponds to pause/resume 


	if key == ord(' '):															#ord return unicode of first character
		key = -1																							
		while key != ord(' '):
			key = window.getch()												
		key = prevKey
		continue


	if key not in [KEY_LEFT, KEY_RIGHT, KEY_UP, KEY_DOWN, 27]:					# If an invalid key is pressed
		key = prevKey

	snake.insert(0, [snake[0][0] + (key == KEY_DOWN and 1) + \
    	(key == KEY_UP and -1), snake[0][1] + (key == KEY_LEFT and -1) + \
    		(key == KEY_RIGHT and 1)])                                         #Calculates the new coordinates of the snake head.

	if snake[0][0] == 0: snake[0][0] = 28									   #If snake head crosses boundary, make it enter from the other side.
	if snake[0][1] == 0: snake[0][1] = 88
	if snake[0][0] == 29: snake[0][0] = 1
	if snake[0][1] == 89: snake[0][1] = 1

    #if snake[0][0] == 0 or snake[0][0] == 19 or snake[0][1] == 0 \ 		   #Uncomment this line to enable
    #	or snake[0][1] == 59: break
    
	if snake[0] in snake[1:]:												   #If snake touches itself
		print('You Lose')
		break;

	if snake[0] == food:
		food = []
		score += 1
		while food == []:
			food = [randint(1, 29), randint(1, 59)]							   #Generate new food
			if food in snake: food = []										   #Making sure new food is not in snake
			window.addch(food[0], food[1], '@')									   #Assigning '@' to food

	else:
		last = snake.pop()                                          		   #If it does not eat the food, length decreases
		window.addch(last[0], last[1], ' ')
	window.addch(snake[0][0], snake[0][1], '#')						           #Assigning '#' to snake

curses.endwin()
print("\nScore: " + str(score))		



