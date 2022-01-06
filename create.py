from PIL import Image
import numpy as np
import random

#background = ["Blue","Orange","Purple","Red","Yellow"]
#background_weights = [30,40,15,5,10]

accessoriesEyes = ["Empty", "Empty","Empty","Empty","Empty","Empty","Empty","Empty"]
accessoriesHats = ["Empty","Empty","Empty","Empty","Empty","Empty","Empty","Empty","Empty"]
accessoriesMouth = ["Empty","Empty","Empty","Empty","Empty","Empty","Empty","Empty","Empty","Empty","Empty","Empty","Empty","Empty"]
accessoriesSunglasses = ["Empty","Empty","Empty","Empty","Empty","Empty","Empty","Empty","Empty","Empty","Empty","Empty","Empty","Empty"]


background_files= {
    "Blue" : "blue",
    "Orange": "orange",
    "Purple": "purple",
    "Red": "red",
    "Yellow": "yellow"
}

basePath = r'/home/godhead/Desktop/nft'
generatedImagePath = r'/home/godhead/Desktop/nft/results'

def alteredImageColor(im, originalColor, newColor):
    data = np.array(im)
    r1, g1, b1 = originalColor[0], originalColor[1], originalColor[2]
    r2,g2,b2 = newColor[0], newColor[1], newColor[2]

    red, green, blue = data[:,:,0], data[:,:,1],data[:,:,2]
    mask = (red == r1) & (green == g1) & (blue == b1 )
    data[:,:,:3][mask] = [r2,g2,b2]

    newImage = Image.fromarray(data)
    return newImage


def getRandomColorArray():
    return [random.randint(0,255), random.randint(0,255), random.randint(0,255)]

def getBaseImage():
    baseImage = Image.open(basePath  + "/Fans/sanfran.jpg")
    baseImage = alteredImageColor(baseImage,[255,0,155], getRandomColorArray())
    return baseImage

def getHatsImage():
    hatsImage = Image.open(basePath + "/common/Hat/Green_crown.png")
    hatsImage = alteredImageColor(hatsImage,[0,162,232],getRandomColorArray())
    hatsImage = alteredImageColor(hatsImage,[255,255,255],getRandomColorArray())
    hatsImage = alteredImageColor(hatsImage,[137,217,232],getRandomColorArray())
    return hatsImage

    


def getSunglassesImage():
    bananaImage = Image.open(basePath + "/common/Accessory/banana.png")
    bananaImage = alteredImageColor(bananaImage,[0,162,232], getRandomColorArray())
    bananaImage = alteredImageColor(bananaImage, [255,255,255],getRandomColorArray())
    bananaImage = alteredImageColor(bananaImage,[153,217,232], getRandomColorArray())
    return bananaImage


def getEyesImage():
    eyesColors = Image.open(basePath + "/common/Eyes/None.png") 
    eyesColors = alteredImageColor(eyesColors,[0,162,232],getRandomColorArray())
    eyesColorse =alteredImageColor(eyesColors,[255,255,255],getRandomColorArray())
    eyesColors = alteredImageColor(eyesColors,[153,217,232],getRandomColorArray())
    return eyesColors
 
def getMouthImage():
    mouthImage = Image.open(basePath  + "/common/Mouth/None.png")
    mouthImage = alteredImageColor(mouthImage,[0,162,232],getRandomColorArray())
    mouthImage = alteredImageColor(mouthImage,[255,255,255],getRandomColorArray())
    mouthImage = alteredImageColor(mouthImage,[153,217,232],getRandomColorArray())
    return mouthImage

"""    
def getBackgroundImage():
    background = Image.open(basePath + "/backgrounds/red.jpg").convert("RGBA")
    return background
"""

def combineImages(baseImage, onTopImage):
    baseImage.paste(onTopImage,(0,0),mask = onTopImage)
    return baseImage

def applyAccessory(baseImage,accessoryList):
    accessory = accessoryList[random.randint(0, len(accessoryList)-1)]
    if accessory != "Empty":
         accessoryImage = Image.open(basePath + accessory).convert('RGBA')
         baseImage.past(accessoryImage,(0,0), mask = accessoryImage)

def saveHighResImage(baseImage, imageID):
    baseImage = baseImage.resize((600,600),Image.NEAREST)
    imageLocation = generatedImagePath  + "/results" + str(imageID) + ".png"
    baseImage.save(imageLocation)


def createNFT(labelNumber):
    baseImage = getBaseImage()
    #backgroundImage = getBackgroundImage()
    hatsImage = getHatsImage()
    eyesImage = getEyesImage()
    sunglassesImage = getSunglassesImage()
    mouthImage = getMouthImage()
    #combineImages(baseImage, backgroundImage)
    #combineImages(baseImage,outlineImage)
    combineImages(baseImage, hatsImage)
    combineImages(baseImage,eyesImage)
    combineImages(baseImage,sunglassesImage)
    combineImages(baseImage,mouthImage)

    applyAccessory(baseImage, accessoriesHats)
    applyAccessory(baseImage, accessoriesEyes)
    applyAccessory(baseImage, accessoriesSunglasses)
    applyAccessory(baseImage, accessoriesMouth)
    
    saveHighResImage(baseImage, labelNumber)

"""
all_images = []

def create_new_image():
    new_image = {}
    new_image["Background"] = random.choices(background,background_weights)[0]
    if new_image in all_images:
        return create_new_image()
    else:
        return new_image
"""

def makeMultiNft(count):
    for i in range(count):
        createNFT(i)

makeMultiNft(20)
