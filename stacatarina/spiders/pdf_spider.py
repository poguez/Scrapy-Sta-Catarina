from scrapy.spider import Spider
from scrapy.selector import Selector
#from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

from stacatarina.items import StacatarinaItem

class DmozSpider(Spider):
  name = "pdf"
  allowed_domains = ["stacatarina.gob.mx"]
  start_urls = [
      "http://www.stacatarina.gob.mx/wsc1215/transparency/browse/10",
      ]

  def parse(self, response):
    #filename = response.url+".txt"
    #open(filename, 'wb').write(response.body)
    sel = Selector(response)
    sites = sel.xpath('//ul/li')
    notes = []
    for site in sites:
      note = StacatarinaItem()
      note['title'] = site.xpath('text()').extract()
      if len(site.xpath('@data-url').extract()) > 0 :
        note['link'] = "http://www.stacatarina.gob.mx/wsc1215/transparency/browse/10"+str(site.xpath('@data-url').extract()[0])
        notes.append(note)
    return notes
