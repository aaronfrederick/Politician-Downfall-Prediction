***Metis Passion Project Readme***

The premise of this passion project is to predict the downfall of US polititians who get wrapped up in various controversies. Many politians endure scandals and get reelected, many fail when election time comes, and many are forced to resign. This project will involve a multifaceted approach to classifying these polititians outlined below:

1. Creating an updateable list of who is in office at any given time (SENATE, HOUSE, WHITE HOUSE) *Currently Only Cabinet Members*
2. Aggregating data to classify who is about to perish
    a. Grabbing news articles about various scandals
        ~ Classifying the subject of the news source
        ~ Classifying the news source as sympathetic/unsympathetic
        ~ Quantifying the seriousness of the allegations
    b. Grabbing Wikipedia pages for 'background' on politician
3. Training a Reinforcement Learning-Style classifier to stay up-to-date with American political goings-on

***Tasks:***
    - find source of list of current American politicians or timeline that can be scraped
        -White House staffers can be found in govtlist.txt
        -Senators and Members of the House will have to be scraped cleverly, address later 
    - Article Scraping:
        - Use NYT article search API
        - https://developer.nytimes.com/article_search_v2.json#/Console/GET/articlesearch.json
        - For the future collection of multi-sourced data, use NEWSAPI
        - https://newsapi.org/
        -Logic is to be as follows: for politician in current_pols_list, make a daily API call, collect articles for analysis
    - Make a document classifier that determines right/left leaning sentiments
    - Use that classifier to assert which news sources lean which ways with a threshold
    - Train a classifier that reads documents about politicians and determines the probability of removed from the timeline
    

    
***Data Storage:***
    - MongoDB
        ~ Collections of news articles (NYTAPI)
        ~ Collection Wikipedia pages on politicians  (WIKIPEDIA)
        ~ Table of writers, their news organization, their political sentiment, an 'impact' factor in politician removal 
