# -*- coding: utf-8 -*-
from scrapy.http.response import Response
import scrapy


class PetMarketSpider(scrapy.Spider):
    name = 'petmarket'
    start_urls = ['https://petmarket.ua/zootovary-dlja-gryzunov/korm-gryzunov/']

    def parse(self, response: Response):
        products = response.xpath('//ul[@class="catalogGrid catalog-grid catalog-grid--s catalog-grid--sidebar"]/li')[:20]
        for product in products:
            yield {
                'description': product.xpath('.//div[@class="catalogCard-title"]/a/text()').get(),
                'price': product.xpath(".//div[@class='catalogCard-price']/text()").get(),
                'img': 'https://petmarket.ua' + product.xpath(".//img[@class='catalogCard-img']/@src").get()
            }
