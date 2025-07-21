from PIL import Image
import os

#Globals
path = "D:/Py/final_project/"

#Zpracovani datasetu, Crop and resize photos, save to new place
image_number = 0
for quality in sorted(os.listdir(path + "dataset/")):
  photos = sorted(os.listdir(path + "dataset/" + quality))
  for photo in range(0, len(photos)-1):
    img = Image.open(path + "dataset/" + quality + '/' + photos[photo])
    img = img.reduce(factor=[2, 2], box=[150, 150, 748, 748])
    img.save(path + "dataset_299/" + quality + '/' + photos[photo])
    image_number = image_number + 1
