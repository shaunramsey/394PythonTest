# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 16:12:47 2018

@author: Ramsey
"""

v = range(4)
print(v)
print(v[0])
print(v[1])
for i in range(4):  #just a loop walking through 4 numbers 0 - 3
    print("i is ", i)
    
#a small list of colors
mycolors = [0,0,255, 255, 255, 255, 0,0,0, 255,0,0]

#a way to skip around walking through the colors but using
#an index for colors instead of every single element in the list
for i in range(4): #i is which color
    print("When i is",i,"index is",3*i,"color is",mycolors[3*i])
    print(mycolors[3*i],mycolors[3*i+1], mycolors[3*i+2])
    
originalwidth = 256
originalheight = 256
width = originalwidth // 2
height = originalheight
for i in range(int(height/2)): #here i is which set of rows
    print("final:",i,i*width*3*2)
    for j in range(width): # j is which color in that row
        print(j,i*width*3*2 + 3*j)
        firstr = i*width*3*2 + 3*j
        firstg = firstr + 1
        firstb = firstr + 2
        secondr = i*width*3*2 + 3*j + 3*width
        secondg = secondr + 1
        secondb = secondr + 2
        print(firstr,firstg,firstb,secondr,secondg,secondb)

