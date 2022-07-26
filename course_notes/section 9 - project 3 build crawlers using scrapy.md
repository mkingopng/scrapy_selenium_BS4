Unfortunately, IMDB has updated their UI which means the HTML markup has also changed. So in order for you to get the
same version of the website I covered in the course, you can use the way-back machine which allows you to go back in
time and load the same version of the website I covered in the course.

Please use this URL

http://web.archive.org/web/20200715000935if_/https://www.imdb.com/search/title/?groups=top_250&sort=user_rating

instead of

https://www.imdb.com

Not all the web pages are archived (only the first one) which is unfortunate. Sorry about that, it's completely out of my control.

# The crawl spider
we've been using the basic templates so far.

- how to fix new line characters and whitespace characters using xpath
```normalize-space```
- you can also get rid of the utf-8 characters as shown previously
- you can do the same for HTML characters

## following links in pagination  
- the order of the rules matters.

## spoofing request headers
- search for "my user agent" in google and copy that as your spoof agent
- if we only leave it at start_requests, we'll send the user_agent details to the first page but not to subsequent 
pages. for that we need to set another argument called ```process_request='set_user_agent'```.
