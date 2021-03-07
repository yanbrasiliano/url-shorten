#Install
#Library to import the function directly from python. 
import pyshorteners

#Place the URL inside the quotation marks.
url = 'xxx.xxxxxx.xxx'

#Activating the function to convert and place the result in the variable 'converter'
converter = pyshorteners.Shortener()

#Your generated URL. 
print(f'Your shortened URL: {converter.tinyurl.short(url)} ')