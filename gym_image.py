'''
Created on 08 Jul 2017

@author: altus
'''

from PIL import Image, ImageDraw, ImageFont

class FileTypes():
    PNG = 'PNG'
    JPG = 'JPG'

class GymImage():
    background_image_loc = '/home/altus/Pictures/image.png'
    #flag_image_loc = '/home/altus/Pictures/south_africa.png'
    #flag_image_loc = '/home/altus/Pictures/usa.png'
    save_path = '/home/altus/Pictures/'
    flag_location = (20,20)
    
    
    def __init__(self):
        #Set the image
        self.background_image = Image.open(self.background_image_loc)
        #self.flag_image = Image.open(self.flag_image_loc)
        
        #Set the fonts for the image
        self.font_score = ImageFont.truetype('/home/altus/Downloads/LED2.ttf', 300)
        self.font_aparatus = ImageFont.truetype('/home/altus/Downloads/name.ttf', 130)
        self.font_name = ImageFont.truetype('/home/altus/Downloads/name.ttf', 215)
        
        
        #create something to draw on
        self.draw = ImageDraw.Draw(self.background_image)
    
    def createImage(self, name, aparatus, score):
        
        try:
            #first past the flag onto the background image
            #Can change this so that it reads from a dictionary
            #self.background_image.paste(self.flag_image,(self.flag_location))
            name_postition = 5
            aparatus_position = 2.2
            score_postition = 1.2
            
            #Get the dimensions of the draw object
            background_x, background_y = self._getSizeOfImage(self.background_image)
            
            # get the dimensions of the name and the score
            score_x, score_y = \
                self._getTextSize(score, self.font_score)
            aparatus_x, aparatus_y = \
                self._getTextSize(aparatus, self.font_aparatus)
            name_x, name_y = \
                self._getTextSize(name,self.font_name)
    
            #Now draw the name on the image
            self.draw.text(((background_x - name_x)/2, (background_y - name_y)/name_postition),\
                           name,\
                           (0,0,0),\
                           font=self.font_name)
            
            #Now draw the
            self.draw.text(((background_x - aparatus_x)/2, (background_y - aparatus_y)/aparatus_position),\
                           aparatus,\
                           (0,0,0),\
                           font=self.font_aparatus)
            
            #Draw the score on the image
            self.draw.text(((background_x - score_x)/2, (background_y - score_y)/score_postition),\
                           score,\
                           (0,0,0),\
                           font=self.font_score)
            
            #Done. Save the image whith the childname
            file_location = self.save_path + '{}.png'.format(name)
            self.background_image.save(file_location,FileTypes.PNG)
            
            return file_location
        
        except Exception as ex:
            print(ex)
            return None
    
    def _getSizeOfImage(self,image):
        return image.size
    
    def _getBackgroundImage(self):
        return self.background_image
    
    def _getFlagImage(self):
        return self.flag_image
    
    def _getTextSize(self,text,font):
        return(self.draw.textsize(text, font))
        
if __name__ == "__main__":
    
    go = GymImage()
    if(go.createImage("Altus Hetfield", "Hoop", "23.197") is not None):
        print("Image created")
    else:
        print("Image creation failed.")
        