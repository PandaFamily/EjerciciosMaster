from BeautifulSoup import BeautifulSoup as BS
import urllib2

WebDownloader = urllib2.build_opener()
CodigoHTML = WebDownloader.open('http://meneame.net')
CodigoSOUP = BS(CodigoHTML)

Enlaces = [link['href'] for link
                        in CodigoSOUP.findAll('a')
                        if link.has_key('href')]
print Enlaces
#print CodigoHTML
#print CodigoSOUP 

