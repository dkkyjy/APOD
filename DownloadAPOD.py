import pdfkit
import requests
from requests_html import HTMLSession

URLbase = 'https://apod.nasa.gov/apod/'
URL = URLbase + 'archivepix.html'
session = HTMLSession()
r = session.get(URL)

links = r.html.links
for link in links:
    if len(link) == 13:
        title = link[:8]
        url = URLbase + link
        try:
            pdfkit.from_url(url, title+'.pdf')
            r = session.get(url)
            img = r.html.find('img')[0]
            src = img.attrs['src']
            imgurl = URLbase + src
            r = requests.get(imgurl)
            with open(title+'.jpg', 'wb') as imgfile:
                imgfile.write(r.content)
        except:
            continue
