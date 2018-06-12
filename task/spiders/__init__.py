# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

import scrapy


class TaskSpider(scrapy.Spider):
    name = 'task'
    start_urls = ['http://books.toscrape.com/catalogue/page-1.html']

    def parse(self, response):
        els = response.css('.product_pod')
        for el in els:
            title = el.css('[title]::attr(title)').get()
            print(title)

        # Follow to next page
        next_page = response.css('li.next a::attr(href)').extract_first()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
