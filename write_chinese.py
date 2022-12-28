from PIL import Image, ImageFont, ImageDraw
import numpy as np
import cv2

class Write_chinese:
    def write(img, font_type, font_size, color, position, content):
        img_PIL = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        font = ImageFont.truetype(font_type, font_size)
        draw = ImageDraw.Draw(img_PIL)
        draw.text(position, content, font=font, fill=color)
        img_OpenCV = cv2.cvtColor(np.asarray(img_PIL), cv2.COLOR_RGB2BGR)
        return img_OpenCV
    
   
