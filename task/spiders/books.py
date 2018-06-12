import scrapy


class BooksSpider(scrapy.Spider):
    name = 'books'
    start_urls = ['http://books.toscrape.com/catalogue/page-1.html']

    def parse(self, response):
        # Print out book titles
        els = response.css('.product_pod')
        for el in els:
            title = el.css('[title]::attr(title)').get()
            print(title)

        # Follow to next page
        next_page = response.css('li.next a::attr(href)').extract_first()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
