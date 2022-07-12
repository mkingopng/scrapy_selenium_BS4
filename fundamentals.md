# Scraping Fundamentals

in theory, we can do simple scraping with Requests and BS4, but these tools struggle with complex projects. Scrapy is the right framework to scrape
for large scale projects.

## in scraping we have 5 main components:
- spiders: this is where we define what we want to extract from a web page. Scrapy has 5 kinds of spiders: scrapy.Spider, 
CrawlSpider, XMLFeedSpider, CSVFeedSpider, SitemapSpider. This course focuses on the first 2 types.
- pipeline: related to the data we extract. Covers cleaning, remove duplication, storing the data in external database
- middlewares: related to Request/Response. Injecting custom headers, proxying, 
- engine: responsible for coordinating between all the other components. Ensures the consistency of all the operations.
- scheduler: responsible for preserving the order of operations. follows the FIFO methodology.

## Robots.txt
- are you allowed to scrape me? contains 3 basic sets of rules.
- user-agent: represents the identity of the spider
- allow: represents the web pages that the spider is allowed to scrape
- disallow: specifies the webpages that are forbidden
example: https://www.facebook.com/robots.txt

## available commands in scrapy CLI
```scrapy```
```bench```
```fetch```
```genspider```
```runspider```
```settings```
```shell```
```startproject```
```version```
```view```

## create a new scrapy project
```scrap startproject worldometers```

the objects created are:
- ```config.py```:
- ```items.py``` is used to clean the data and store the data in some fields we create. the commented out part is an 
example of how fields are defined in scrapy
- ```middlewares.py``` contains everything to do with the request/response objects. we have the spider middleware which 
is responsible for returning the data, and the downloader middleware which is responsible for downloading the HTML 
markup of a website. we can see these two predefined classes in the file 
- ```pipelines.py```: used to store the items you scrape in a database
- ```settings.py```: used to tweak or add some extra configuration to the file


you can start your first spider with ```cd worldometers``` then use ```scrapy genspider <example> <example>```

in one project you can have many spiders. each spider must have a unique name

## scrapy shell
- great tool for building a spider
- test basic element selection
- debug xpath or css selectors

gave example of using ```scrapy shell``` then ```fetch()``` to crawl site

the second way to opening a URL in the scrpay shell is to construct a requests object and pass it as an argument to the 
```fetch()``` method
- ```r = scrapy.Request(url="https://www.worldometers.info/world-population/population-by-country/")```
- ```fetch(r)```
- ```response.body```
- you can also inspect the site via your browser
- our spider sees the website without javascript. this is a common problem in scraping. the spider can't directly render 
javascript. There is a tool called splash that helps us with that.

## XPath and CSS selectors (need to re-watch section 9 for this)
- disable javascript
- test XPath in chrome developer
- need to learn how to use the same tools for firefox
- 