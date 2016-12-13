from Tkinter import *
import random
import time
#Variable List:
#w, h, lost = width, height, if we've lost yet

######## bombs, adj, table, items
# bombs is a 10 x 10 matrix of where the bombs are
# adj is a 10 x 10 matrix of the number of bombs next to each square
# table[x][y] = 1 means red square, 2 means blue square, 0 means nothing inside (no numbers or red/blue squares)
# -1 means we've clicked it and nothing, -2 means we've clicked it and something inside

# item[x][y] tells us if we have a rectangle inside or a number or w/e


root = Tk()
row, col = 50,50
scale_x, scale_y = 20,20
w,h = 1000,1000

white,black = "#CCCCCC", "#444444"
iteration = 1

xpos,ypos = 50,50
dirz = 0
graph = [["#EEEEEE"]* 200 for x in range(200)]

def slots(event): #this takes the absolute location and transforms it into grid slots
  return event.x /scale_x, event.y /scale_y


def click_l(event): #left clicking squares. If it's a bomb we lose
  global iteration,xpos,ypos, graph, dirz
  iteration +=1


  if graph[xpos][ypos] == black:
    graph[xpos][ypos] = white
    dirz += 1
  else:
    graph[xpos][ypos] = black
    dirz -= 1


  frame.create_rectangle(10*xpos, 10*ypos, 10*xpos+8,10*ypos+8, fill = graph[xpos][ypos])
  dirz = dirz%4
  if dirz == 0: xpos += 1
  elif dirz == 1: ypos += 1
  elif dirz == 2: xpos -= 1
  elif dirz == 3: ypos -= 1


  if xpos >= len(graph) or xpos < 0 or ypos >= len(graph) or ypos < 0:
    print "exited the graph at:", i


  #frame.create_rectangle(x*scale_x, y*scale_y, (x+1)*scale_x, (y+1)*scale_y, fill=free)
  #frame.create_text(x*scale_x+scale_x/2,y*scale_y+scale_y/2, text = adj[x][y])


def draws(frame, x,y): #creates the basic 10 x 10 grid on the map.
  frame.create_rectangle(0,0,w,h, fill = white)



#root.resizable(width=FALSE, height=FALSE)

frame = Canvas(root, width=w, height=h)
frame.bind("<B1-Motion>", click_l)
frame.height = h
frame.width = w
draws(frame,row,col)
frame.pack(side=BOTTOM)

frame.mainloop()
root.mainloop()
