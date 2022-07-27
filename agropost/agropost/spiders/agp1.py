import scrapy


class Agp1Spider(scrapy.Spider):
    name = 'agp1'
    allowed_domains = ['agropost.wordpress.com']

    def start_requests(self):
        urls = [
            'http://agropost.wordpress.com/',
            'http://agropost.wordpress.com/page/2/'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f'agropost-{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')

