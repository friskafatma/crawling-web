# -*- coding: utf-8 -*-
import scrapy


class CobaSpider(scrapy.Spider):
    name = 'coba'
    #allowed_domains = ['https://brickset.com/sets/year-2016']
    start_urls = ['https://brickset.com/sets/year-2016/']

    def parse(self, response):

        barang = response.css(".meta h1 a::text").extract()

        scraped_info = {'barang'  : barang}

        yield scraped_info
