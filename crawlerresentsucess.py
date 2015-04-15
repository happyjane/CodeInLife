import html5lib
import urllib2
import argparse
import codecs
from lxml import etree
from BeautifulSoup import BeautifulSoup
from html5lib import treebuilders
from sgmllib import SGMLParser
url='http://www.tutiempo.net/en/Climate/ANQING/584240.htm'
parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('-y',dest="year", default='',  action="store", type=int 
                   ,help='a year for the crawler')
parser.add_argument('-m',dest="month", default='',  action="store", type=int
                   ,help='a year for the crawler')
parser.add_argument('-c',dest="city", default='',  action="store", type=str
                   ,help='a city for the crawler')
results = parser.parse_args()
year=results.year
month=results.month
city=results.city

class Crawler(object):

    def __init__(self,year,month,city):
        self.prefix = 'http://www.tutiempo.net/clima'
        self.year = year
        self.month = month
        self.city=city

    def url_back(self):
    	url = '%s/%s/%02d-%04d/%d.htm' % (self.prefix, self.city, self.month, self.year, self.getstation(self.city))
        #url= str(self.prefix) + '/'+ self.city+'/'+ self.month + '-' + self.year + '/' + getstation(self.city)+".html"
        return url 
    def getstation(self,city):
        if city=="Beijing":
            return 545110
        else:
            return None

    def getHtml(self,url):
        page = urllib2.urlopen(url)
        html = page.read()
        #f=open('/home/sunying/hello-jane/weathercrawler/f.txt','w')
        #f.write(html)
        #f.close()
        page.close()
        return html
crawler= Crawler(year,month,city)
#print crawler.url_back()
print crawler.getHtml(url)

