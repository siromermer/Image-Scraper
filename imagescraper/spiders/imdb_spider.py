import scrapy
import os
import urllib.parse

class IMDbSpider(scrapy.Spider):
    name = 'imdb_spider'
    
    celebrity_list = [
        {"name": "Conan O'Brien", "link": "https://www.imdb.com/name/nm0005277/mediaindex?page=1&ref_=nmmi_mi_sm"},
        {"name": "John Wayne", "link": "https://www.imdb.com/name/nm0000078/mediaindex?page=1&ref_=nmmi_mi_sm"},
        {"name": "Robert De Niro", "link": "https://www.imdb.com/name/nm0000134/mediaindex?page=1&ref_=nmmi_mi_sm"},
        {"name": "Tom Cruise", "link": "https://www.imdb.com/name/nm0000129/mediaindex?page=1&ref_=nmmi_mi_sm"},
        {"name": "Leonardo DiCaprio", "link": "https://www.imdb.com/name/nm0000138/mediaindex?page=1&ref_=nmmi_mi_sm"}
    ]

    def start_requests(self):
        for celeb in self.celebrity_list:
            for page_num in range(1, 21):  # 1'den 20'ye kadar olan sayfaları tarar
                link=f'{celeb["link"].split("?")[0]}?&page={page_num}&ref_=nmmi_mi_sm'
                # link = f"{celeb['link']}&page={page_num}"  # Sayfa numarasını URL'ye ekleme
                yield scrapy.Request(url=link, callback=self.parse, meta={'celebrity': celeb['name'], 'page_num': page_num})

    def parse(self, response):
        celebrity_name = response.meta['celebrity']
        page_num = response.meta['page_num']
        folder_name = celebrity_name.lower().replace(' ', '_').replace("'", '')


        img_tags = response.css('img::attr(src)').extract()
        for index, img_url in enumerate(img_tags, 1):
            img_url = urllib.parse.urljoin(response.url, img_url)
            img_name = f"{celebrity_name}_{(page_num - 1) * len(img_tags) + index}.jpg"

            yield {
                'image_url': img_url,
                'image_name': img_name,
            }
