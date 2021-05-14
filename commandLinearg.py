import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-d', help='Enter Source directory')
parser.add_argument('-a', help='Enter Name of Destination Album')
parser.add_argument('-mk', help='Create Album in Google Photo')

userInput  = parser.parse_args()

sourceDir = userInput.d
destinationAlbum = userInput.a
newAlbum = userInput.mk 
