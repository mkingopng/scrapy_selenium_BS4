# Task
your job is to build a Crawler which will crawl all the books from all the available pages in this website 

'http://books.toscrape.com/'

This website was mainly created for scraping purpose by "ScrapingHub" the company behind Scrapy.

As mentioned previously the goal is to **visit each book page** and scrape the **"book name"** and the **"price"** 
from all the available pages.

Now, because this is the first time you build a CrawlSpider, I'm gonna give you a little of guidance:
- You probably need to write two "Rule" objects:
- The first Rule object will handle opening each book URL
- The second Rule object will handle pagination
- Make sure to store all the data in a JSON or a CSV file it's up to you.

Feel free to download the solution from this link 

"https://www.dropbox.com/sh/a8anjg5z1oinxhv/AABWn-1nH-gJ7FMc6aoTrLy0a?dl=0".

# Notes

```scrapy startproject book_store```