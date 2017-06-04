***reuters spider***

this project is a scrapy spider that a list of symbols in a text file then scrap reuters.com to get required information.

***Installation***
you just need to have python 3.6 installed and all packages included in requirements.txt.

***Used Packages***

-scrapy: get and parse pages.

-sqlite database: to store the scrapped data.

***How to run***

on the project root folder,

# cd reuters

update symbol.txt for the targeted symbols (one each line).

# scrapy crawl reuters -o output.csv --logfile errors.log --loglevel ERROR

this cmd will start the crawler that 
1- read all symbols from symbols.txt
2- get html code for all symbol pages (one by one)
3- parse each page to get date we are interested in
4- store each item (parsed data) into sqlite db
5- write the item to the output csv file

after the crawler is done, it will generate errors.log file that contains the crawler errors and output.csv that contains the scrapped data
