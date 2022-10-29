
#___________________


import os
from PIL import Image

x = r'C:\Users\aditi\Documents\google_images'
directory = os.fsencode(x)
    
for file in os.listdir(directory):
     filename = os.fsdecode(file)
     if filename.endswith(".jpg") or filename.endswith(".png"):
         # print(os.path.join(directory, filename))
         img = Image.open(filename)
         rgb_img = img.convert('RGB')
         rgb_img.save(filename+'.jpeg')
     else:
         continue
#__________________________

