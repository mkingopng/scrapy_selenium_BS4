# Section 7: Debugging Spiders
sometimes the logs are not enough to figure out whats wring with your spider. Most of the time you'll end up on stack 
overflow. Often due to the dynamic nature of scraping, you won't find a post thats exactly what you need, and you will 
have to rely on yourself.

## debugging: solving errors and issues (realised or potential)
- logical errors
- syntactical errors

## 35 - Some ways to debug scraping projects(ref the docs)
- the parse command via the terminal
- he has some really clever ways of debugging using the terminal. It would be worth rewatching this and making detailed 
notes. also take time stamps to refer back to in future
- 
## in lesson 36 he shows his own method using VS Code
- runner.py method. This is really cool and needs to be re-watched
- even though he's demonstrating it in vs code it would work fine in pycharm

# rules object
crawl spiders must contain rules (tuple), and the rules tuple must contain at least one rule object
- Link Extractor = 
- allow = 
- callback = 
- follow = 
this bit is obviously important for the automation of spider behaviour on large complex sites
- we can also use Xpath and css selectors
- 