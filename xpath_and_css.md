# XPath and CSS

## what are they?
- comes from XML path langauge but can be used to select elements. syntax is sometimes over complex
- cascading style sheets (CSS)

## CSS selectors (this whole section is worth reviewing when planning out selectors)
- **https://try.jsoup.org/** is a really useful tool for testing css and xpath
- classes vs id's
- we don't just have classes and id's. we can also have href attributes for links, or others like data-identifier
- we also have conditions in css selectors, eg: ```a[href^=https]```. This seems a lot like regex
- we can also select based on position: ```div.intro p```
- if we want to include its descendants, we can use: ```div.intro p, span#location``` or ```div.intro > p```
- repetition is the mother of learning

## CSS selectors in theory

## xpath 
- this will be the default
- **https://scrapinghub.github.io/xpath-playground/** is a really useful tool for testing xpath

##