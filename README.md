scrapy program to download all the images in a page 

main idea relly on is this --> response.css('img::attr(src)').extract()    , it takes all image link and return them as json file

at the end you are gonna obtain .json file , after that you can download all images 
