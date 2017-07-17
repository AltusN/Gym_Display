'''
Created on 08 Jul 2017

@author: altus
'''

import tkinter as tk
import sys

class GymDisplay():
    def __init__(self,image_location):
        self.image_location = image_location
        
    def showScoreForGymnast(self,timeout=None):
        #tk will quit after
        root = tk.Tk()

        root.attributes("-fullscreen",True)
        canvas = tk.Canvas(root)
        canvas.pack(fill=tk.BOTH, expand=1) # expand
        
        photo = tk.PhotoImage(file = self.image_location)
        root.geometry("1024x768")
        root.update()
        
        canvas.create_image(0,0, anchor=tk.constants.NW, image=photo)
        
        root.after(18000, lambda: root.quit())
        #root.bind("<Escape>",root.attributes("-fullscreen",False))
        root.mainloop()
        
        
if __name__== "__main__":
    #loc = sys.argv[1]
    
    #gd = GymDisplay(loc)
    #gd.showScoreForGymnast()

    pass
        
        
