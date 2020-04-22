import requests
import bs4
im = "https://www.google.com"
req = requests.get( im  )
print (type(req))
text = req.text
file = "index.html"
bs = bs4.BeautifulSoup(text , "html.parser")
bsp = bs.prettify()
#print (bsp)
with open (file , "w" ) as f :
    f.write(text)

c = bs.find_all("img")
b = bs.find_all("a")
print (len(c))
print (len(b))
