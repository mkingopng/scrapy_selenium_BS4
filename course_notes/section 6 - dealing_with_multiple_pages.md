# Dealing with pagination
we have two options to deal with pagination
- extract the page link
- find the <next page> link (prefered)
- there may be another way used by a site. you have to be adaptable

```
next_page = response.xpath("//a[@class='nextPage']/@href").get()

if next_page:
    yield scrapy.Request(url=next_page, callback=self.parse)
```

# section 6: spoofing request headers
a good explanation of requests between the browser and the site. Note the difference between the request headers from 
scrapy vs the browser. sometimes this alone is enough to get you blocked.

there are several ways we can modify the identification of our spider
- the first one is to chane the user agent in settings.py to match a browser's identification. This is not always a great option
- if you want to over ride multiple request headers, you can do two things:
1) use DEFAULT_REQUEST_HEADERS
2) use a more complete approach that he demonstrates in lecture 31. **this bit was very interesting!**
