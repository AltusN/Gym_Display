'''
Created on 08 Jul 2017

@author: altus

Displays a gymnast name and the associated score on the display
'''
from gym_image import GymImage
from gym_display import GymDisplay
import sys

#make this listen for a connection

def createImageForDisplay(name, aparatus, score):
    '''
        Creates an image using the name
        and score of the Gymnast for display
    '''
    gi = GymImage()
    
    image_location = gi.createImage(name, aparatus, score)
    
    if(image_location is not None):
        print('[i] Image for {} created'.format(name))
    else:
        print('[!] Could not create image for {}'.format(name))
    
    return image_location
    
    
def displayImage(location):
    '''
        Displays the image
    '''
    
    gd = GymDisplay(location)
    
    gd.showScoreForGymnast()


##==================================================##

name = sys.argv[1]
aparatus = sys.argv[2]
score = sys.argv[3]

print("[i] I got this to work with: {} {} {}".format(name,aparatus,score))


    #name = input("Name:\t")
    #score = input("Score:\t")
    
    #response = input("\n[i] You entered {} and {}. is this correct?".format(name, score))
    #if(response == 'y' or response == ''):
loc = createImageForDisplay(name, aparatus, score)
if(loc):
    print("[i] Display {}".format(loc))
    displayImage(loc)
else:
    print("[!] Could not create a display image")
#print("[i] Done.\n")
# I don't know why this does not want to close the display in a  loop
exit()
    