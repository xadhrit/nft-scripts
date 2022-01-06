#!/usr/bin/env python3
import os, sys
import glob
import cv2
from PIL import Image
from IPython.display import display
import random
import json

#  Each image is made up of a series of traits which decides their weightness for each trait which is solely responsible for their rarity.


background = ["Blue","Orange","Purple","Red","Yellow"]
background_weights = [30,40,15,5,10]

background_files = {
      "Blue": "blue" ,
      "Orange":"orange",
      "Purple": "purple",
      "Red": "red",
      "Yellow" : "yellow",
}

#fur = []

team = ["Indy MoonWalkers","Chi-Town Crypto Cadets","Miami Stargazers","Los Angeles Lightyears","New York Space Rangers","Toronto Cyberogs","Philly UFO's","Atlanta Abominable Aliens", "Houston Star Hoopers", "Orlando Moon Rockers", "Brooklyn Apollos", "Las Vages Comet Crushers","Detroit Big Dippers","Denver X-Men","Oregon Planets","San Fransisco Meteor Stroms","Hawaii Galaxy Heros","Arizona Black Holes", "D.C. Planeteers","Boston Belts","Utah Lava Planets","Dalla Beam Rays","Phoenix Sun Flares","Vancouver Voyagers","Michigan Martian's","Alaskan Natives","Nashville Astronauts", "Memphis Moon Patrol","Louisiana Lunars","Oklahoma"]


#level = ["Fans","Super Fans","Players","HOF Players","Coaches","Owners"]
#level_files = {
    
#}

fan = ["Alaska","Arizona","Atlanta","Boston","Brooklyn","Chicago","Dallas"]

fan_files=  {
     "Alaska": "alaska-fan",
     "Arizona":"arizona-fan",
     "Atlanta":"atlanta-fan",
     "Boston": "boston-fan",
     "Brooklyn": "brooklyn-fan",
     "Chicago" : "chicago-fan",
     "Dallas": "dallas-fan"
}


TOTAL_IMAGES = 20

all_images = []

def create_new_image():
    new_image = {}

    new_image["Background"] = random.choices(background, background_weights)[0]
    #new_image["Fur"] = random.choices(fur, fur_weights)[0]
    new_image["Team"] = random.choice(team)
    new_image["Fan"] = random.choice(fan)

    if new_image in all_images:
          print("Generating new image")
          return create_new_image()
    else:
         return new_image

for i in range(TOTAL_IMAGES):
    new_trait_image = create_new_image()
    all_images.append(new_trait_image)
    

# image_uniqueness(all_images):

def image_uniqueness(all_images):
    seen = list()
    return not any(i in seen or seen.append(i) for i in all_images) 

print("Check if all images are unique ....", image_uniqueness(all_images))

#add token id to each image
i = 0
for item in all_images:
    item["tokenId"] = i
    i = i + 1
#print(all_images)

background_count = {}
for item in background:
    background_count[item] = 0

"""
fur_count = {}
for item in fur:
    fur_count[item] = 0

"""
team_count = {}
for item in team:
    team_count[item] = 0

fan_count = {}
for item in fan:
    fan_count[item] = 0

for image in all_images:
    background_count[image["Background"]] += 1
    #fur_count[image["Fur"]]  += 1
    team_count[image["Team"]] += 1
    fan_count[image["Fan"]] += 1

print("Background : ", len(background_count)) 
#print("Fur : ", fur_count)
print("Team :  ", len(team_count))
print("Fan : ", len(fan_count))


"""
Generate Metadata for all traits
"""
if not os.path.exists('metadata'):
     os.mkdir('metadata')

METADATA_FILENAME = './metadata/all-traits.json';
with open(METADATA_FILENAME,'w') as outfile:
     json.dump(all_images, outfile, indent=4)

## generate images
for item in all_images: 
     im1 = Image.open(f'./backgrounds/{background_files[item["Background"]]}.jpg').convert('RGBA')
     #im2 = Image.open(f'./trait-layers/fur/{fur_files[item["Fur"]]}.jpg')
     #im3= Image.open(f'./trait-layers/team/{team_files[item["Team"]]}.jpg')
     im4 = Image.open(f'./Fans/{fan_files[item["Fan"]]}.jpg').convert('RGBA')

     conv1 = Image.alpha_composite(im1,im4)
     #conv2 = Image.alpha_composite(conv1, im3)
     #conv3 = Image.alpha_composite(conv2,im4)

     #coloring composition
     rgb_im = conv1.convert('RGB')
     file_name = str(item["tokenId"]) + ".png"
     rgb_im.save( "./images/" + file_name )


"""
Generate metdata for each image
"""
f = open("./metadata/all-traits.json",)
data = json.load(f)

IMAGE_BASE_URI = "INSERT_IMAGES_BASE_URI_HERE"
#PROJECT_NAME = "WRITE_PROJECT_NAME_HERE"

def getAttribute(key, value):
    return {
         "trait_type": key,
         "value" : value
    }

for i in data:
    token_id = i['tokenId'] 
    token  = {
      "image": IMAGE_BASE_URI + str(token_id) + '.png',
      "tokenId": token_id,
      "attributes" : []
    }

    token["attributes"].append(getAttribute("Background",i["Background"]))
    #token["attributes"].append(getAttribute("Fur",i["Fur"]))
    #token["attributes"].append(getAttribute["Team",i["Team"]])
    token["attributes"].append(getAttribute("Fan",i["Fan"]))

    with open('./metadata/' + str(token_id),'w') as outfile:
         json.dump(token, outfile, indent=7)
f.close()
