'''
Python Image Library Basics
Extracting EXIF Data from a JPEG
Joshua Urianza
'''
import sys

# pip install Pillow
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS

# Extract Basic EXIF Data
print("\nExtract JPEG EXIF Data \n")
imageFileName = input("Enter JPEG: ")

try:
    pilImage = Image.open(imageFileName)
    exifData = pilImage._getexif()

except Exception as err:
    sys.exit("\nPIL Exception: "+str(err))
    
if not exifData:
    sys.exit("\nNo EXIF data\n")
    
# Process eachTag 
for tag, theValue in exifData.items():
    
        tagValue = TAGS.get(tag, tag)
        tagData  = exifData.get(tag)

        if tagValue != "GPSInfo":
            # Display the Basic Tag Data
            print("="*40)
            print("TAG:  ", tagValue)
            print("Data: ", tagData)
        else:
            print("GPS Data Found")
            # Process GPS data
            for tag in theValue:
                gpsTag = GPSTAGS.get(tag, tag)
                print("\t", gpsTag, theValue[tag])
        

