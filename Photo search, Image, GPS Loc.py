
'''
Joshua Urianza
Version 1
October 2020
Photo Search/IMage/JSON/CSV/Prettytable 
'''


import sys      # System Specifics
import os       # File system Operations
import json     # json library
import csv
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS # GPS location
from prettytable import PrettyTable # Prettyable

DIR = input('Filename:') # Try .\\photos
cnt = 0 # Files processed
photoDict = {}
print("Searching for Photos: ", DIR, "\n")
        
fileList = os.listdir(DIR)

try:
    with open("results.csv", 'w', newline='') as outFile: #CSV Result Start
        
        reportWriter = csv.writer(outFile, delimiter=',', quotechar='"')
        heading = ['File', 'Ext', 'Format', 'Width', 'Height', 'Mode']
        reportWriter.writerow([fld for fld in heading])   # CSV Result End 
        
        for eachFile in fileList:
            
            path = os.path.join(DIR, eachFile)
            if os.path.isfile(path):
                cnt += 1
                ext = os.path.splitext(path)[1]
            
                try:
                    with Image.open(path) as im:
                        reportWriter.writerow([path, ext, im.format, im.size[0], im.size[1], im.mode])
                except Exception as err:
                    reportWriter.writerow([path, ext, "[NA]", "[NA]", "[NA]", "[NA]"])            
                    pass
                
            else:
                continue       
   

            

    with open("photo.json", "w") as outFile:
            
        for eachFile in fileList:
                        
            path = os.path.join(DIR, eachFile)
            if os.path.isfile(path):
                cnt += 1
                ext = os.path.splitext(path)[1]
                    
                try:
                    with Image.open(path) as im:
                        photoDict[path] = [ext, im.format, im.size[0], im.size[1], im.mode]
                except Exception as err:
                    photoDict[path] = [ext, "[NA]", "[NA]", "[NA]", "[NA]"]           
                    pass
            else:
                continue
        json.dump(photoDict, outFile, indent=4)
                    
except Exception as err:
    sys.exit("Exception: "+str(err))

#PRETTY TABLE START     
tbl = PrettyTable(['ERR','FilePath','Ext', 'Format', 'Width', 'Height', 'Mode'])

for eachFile in fileList:
    path = os.path.join(DIR, eachFile)
    if os.path.isfile(path):
        ext = os.path.splitext(path)[1]
        try:
            with Image.open(path) as im:
                tbl.add_row([ERR, path, ext, im.format, im.size[0], im.size[1], im.mode])
        except Exception as err:
            tbl.add_row(["[*]",path, ext, im.format, im.size[0], im.size[1], im.mode])            
            pass
    else:
        continue
    
tbl.align = 'l'
print(tbl.get_string(sortby="Format"))
#PRETTY TABLE END

print("Files Processed: ", '{:,}'.format(cnt))
print("\nScript End")



