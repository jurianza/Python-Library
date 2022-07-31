'''
Scraping Website
Joshua Urianza
'''

# Python Standard Libaries
import requests                         # Python Standard Library for url requests
import re                               # Python regular expression library
import os

# Python 3rd Party Libraries
from bs4 import BeautifulSoup           # 3rd Party BeautifulSoup Library - pip install Beautifulsoup4

IMG_SAVE = "./IMAGES/"  # Directory to store images

# Create the directory if necessary
if not os.path.exists(IMG_SAVE):
    os.makedirs(IMG_SAVE)
    
pageLinks = set()
imgDict   = {}


def RecurseURL(newURL, base, local):
    try:
        if base not in newURL:
            return
        page = requests.get(newURL)                         # retrieve a page from your favorite website
        soup = BeautifulSoup(page.text, 'html.parser')      # convert the page into soup
        print(soup.title)

        links= soup.findAll('a')   # Find all the possible links
        if links:
            for eachLink in links:
                
                newLink = eachLink.get('href') 
                
                if not newLink:
                    continue
                
                if 'http' not in newLink:
                    newLink = base+newLink
                    
                if not local in newLink:
                    continue   
                
                if newLink not in pageLinks: 
                    # verify this is a true new link
                    
                    # Process any images found
                    images = soup.findAll('img')  # Find the image tags
                    for eachImage in images:      # Process and display each image
                        try:
                            imgURL = eachImage['src']
                            print("Processing Image:", imgURL, end="")
                            if imgURL[0:4] != 'http':       # If URL path is relative
                                imgURL = base+imgURL         # try prepending the base url
                            
                            imageName = os.path.basename(imgURL)  # Get the basename 
                            imgOutputPath = IMG_SAVE+imageName    # Prepare the output path
                            
                            response = requests.get(imgURL)       # Get the image from the URL

                            imgContent = response.content
                            with open(imgOutputPath, 'wb') as outFile:
                                outFile.write(imgContent)
                                
                            # Save the image
                            print("  >> Saved Image:", imgOutputPath)
                        except Exception as err:
                            print(imgURL, err)
                            continue    
                    
                    pageLinks.add(newLink)              # add the link to our set of unique links 
                    RecurseURL(newLink, base, local)           # Process this link
                else:
                    continue
                    
    except Exception as err:
        # display any errors that we encounter
        print(err)

if __name__ == '__main__':
    
    ''' Main Program Entry Point ''' 

    baseURL     = 'https://casl.website/'
    baseDomain  = 'https://casl.website/'
    mustInclude  ='casl'    

    pageLinks.add(baseURL)
    
    print("\nScanning: ", baseURL, '\n')
    RecurseURL(baseURL, baseDomain, mustInclude)
    
    print("\nScanning Complete\n")
    print("Unique URLs Discovered\n")
    
    for eachEntry in pageLinks:
        print(eachEntry)
    
print('\n\nScript Complete')

