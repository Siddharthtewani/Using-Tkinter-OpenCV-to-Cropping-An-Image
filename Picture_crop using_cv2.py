from tkinter import filedialog
import cv2
import os
import numpy as np
import tkinter as tk
import time
from PIL import Image,ImageTk
root = Tk()
root.geometry('300x200')
drawing = False
point1 = ()
point2 = ()

def mouse_draw(event,x,y,flags,params):
    global point1, point2,drawing,img2
    if event==cv2.EVENT_LBUTTONDOWN :
        point1=(x,y)
        drawing=True               
    
    elif event==cv2.EVENT_LBUTTONUP:      
        if drawing ==True:
            point2=(x,y)
        image_fresh=img2
        cv2.destroyAllWindows()
        cv2.rectangle(img2, point1, point2, (255, 121, 0), 2)     
        cv2.imshow('rectangle_image', img2)
        cv2.waitKey(0)
        cv2.destroyAllWindows()      
        cropped = image_fresh[point1[0]:point1[1], point2[0]:point2[1]]
        stretch_near =cv2.resize(cropped,(500,500))
        cv2.imshow('cropped_image', stretch_near)  
        cv2.waitKey(0)
        cv2.destroyAllWindows()


def browsering():
    global img2
    fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Select Image File",filetypes=(("JPG File","*jpg"),("JPEG File","*jpeg"),("PNG File","*.png"),("All","*.*")))
    img=Image.open(fln)
    img.thumbnail((350,350))
    bg= ImageTk.PhotoImage(img)
    label.configure(image=bg)
    root.destroy()
    img2 = np.array(img)   
    cv2.namedWindow("image")
    cv2.setMouseCallback("image",mouse_draw)         
    cv2.imshow("image",img2)  
    key=cv2.waitKey()  
    cv2.destroyAllWindows()


label=Label(root)
label.pack(side=tk.LEFT)
btn=Button(root,text="Browse Imnage",command=browsering)
btn2=Button(root,text="Exit",command=lambda : exit())
btn.pack(side=tk.LEFT,padx=57)
btn2.pack(side=tk.LEFT,padx=4)
root.mainloop()

