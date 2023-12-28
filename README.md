scrapy program to download all the images in a page 

main idea relly on is this --> response.css('img::attr(src)').extract()    , it takes all image link and return them as json file

you can initialize your spider from terminal like below :<br>
scrapy crawl imdb_spider -o imdb.json 

with that json file you are gonna obtain bunch of images links after that you can download them easily 

