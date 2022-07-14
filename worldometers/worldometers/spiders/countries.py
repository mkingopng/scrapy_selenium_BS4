import scrapy


class CountriesSpider(scrapy.Spider):
    name = 'countries'
    allowed_domains = ['www.worldometers.info']
    start_urls = ['https://www.worldometers.info/']

    def parse(self, response):
        """
        catch the response from the spider's scraping
        :param response:
        :return:
        """
        title = response.xpath("title = response.xpath('//h1')").get()
        countries = response.xpath('//td/a/text()').getall()

        yield {
            'title': title,
            'countries': countries
        }

