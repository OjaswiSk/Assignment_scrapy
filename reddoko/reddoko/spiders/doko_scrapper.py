import scrapy

class dokoscraper(scrapy.Spider):

    name = 'doko'

#https://www.reddoko.com/categories/mobile-phone?q=price%3A1110%2C32468

    start_urls = ['https://www.reddoko.com/categories/mobile-phone?q=price%3A1110%2C32468']

    def parse(self, response):
        #items = ScraperItem()
        allitem = response.css('div.productinfo')

        for news in allitem:
            prodname = response.css('div.product-list--name p::text').getall()
            prodbrand = response.css('div.productinfo span::text').getall()
            prodprice = response.css('div > span:nth-child(1)::text').getall() 
            yield {
                'productname': prodname,
                'productbrand': prodbrand,
                'productprice': prodprice
            }
       

