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
- a faster alternative is ```scrapy shell "https://www.worldometers.info/world-population/population-by-country/"```
- you can also inspect the site via your browser
- our spider sees the website without javascript. this is a common problem in scraping. the spider can't directly render 
javascript. There is a tool called splash that helps us with that.

## how to enable and disable javascript from a page (Firefox)
- Enter ```about:config``` into the URL bar in Firefox
- Select the blue ```Accept the Risk and Continue``` button.
- Enter ```javascript.enabled``` into the search box at the top of the page.
- Select the toggle to the right of ```javascript.enabled``` to change its value to false. 
- JavaScript is now disabled in your Firefox browser. To re-enable it at any time, change the value of 
```javascript.enabled``` to true.
- test XPath in chrome vs firefox developer

## how do enable and disable javascript in Chrome
- ```ctrl-shift-i``` to open up development tools
- ```crtl-shit-p``` to open up the command path
- type in ```javascript```
- select the second option
- ```ctrl-r```

## XPath and CSS selectors (need to re-watch section 9 for this)
we're trying to scrape the title of worldometers. we want to scrape the title using xpath. Before scraping we need to follow these steps:
- disable javascript, because scrapy will return the raw html without javascript, so we want to see the same raw html 
markup in browser that scrapy will return. see above for instructions.
- use the inspection tool to select the title, either by clicking on it or right clicking and selecting ```inspect```
- we need to test our XPath expression first before implementing in scrapy. 
- for that we click on the elements table and ```ctrl-f```, and a new search box will appear
- type ```\\h1``` into the search box, and the element will be highlighted
- we copy this xpath expression back to python
- in the scrapy shell we enter ```title = response.xpath('//h1')```
- if we only want the text, we need to make a slight change to the XPath expression: ```title = response.xpath('//h1/text()')```
- now if we just want to return the title as a string we just type ```title.get()```

we can do the same thing with css
- ```title_css = response.css('h1::text')```
- ```title_css```
- note that scrapy automatically casts the return to XPath even when you use CSS selectors, so its recommended to use XPath
- ```title_css.get()```

## selecting countries
- use the selection tool in chrome to select a country. 
- we notice that ```//a``` returns all the information including all the script tags that are not related to the country, not just the country
- we notice that ```//a``` is inside ```td``` so we can modify our expression to ```//td/a```
- in the scrapy shell we can now create a variable called countries ```countries = response.xpath('//td/a')```
- and to refine it further we can say ```countries = response.xpath('//td/a/text()').getall()```
- and we get a list of all the countries.