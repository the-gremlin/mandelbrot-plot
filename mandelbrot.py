from graphics import *
import math
import multiprocessing as mp

win = GraphWin("", 1000, 1000)

proc_num = mp.cpu_count() * 4

#TODO: gotta color the pixels based on the number of iterations it takes them to go over the limit

g = 0
const_1 = win.width / 4
const_2 = win.width / 2

# splitting the process into chunks

def chunks(sequence, chunks):
    size = len(sequence)
    start = 0
    for i in range(0, chunks):
        stop = i * size // chunks
        yield sequence[start : stop]
        start = stop


# takes graphics pixel thingy i dont understand this library pls help, anyways... takes pixel object and returns its cartesian equivalent
def convert_to_cart(pixel_object): #this function has ruined me and i don't know why im still doing this project ffs
    # subtract half the width of the window and then divide by a fourth to make it a point on a 4 x 4 plot of the cartesian plane 
    x = (pixel_object.x - const_2) / const_1 
    y = (pixel_object.y - const_2) / const_1 
    return x, y

#this is working no need to change it for the love of god
#Passing a number through the formula to check if it escapes after x iterations, if it doesnt then we paint it
def mandelbrot(comp, x, pixel):
    z = 0
    for i in range(x):
        z = (z ** 2) + comp
        if math.sqrt((z.real ** 2) + (z.imag ** 2)) > 2:
            pass    
    pixel.draw(win)

# ok so, i need to make the func that passes over ever pixel, then split the rows into chunks using chunks(), then does pool.map(mandelbrot, complex_number, iterations, pixel)


                        )
if __name__ == "__main__":
   


win.getMouse()
win.close()





