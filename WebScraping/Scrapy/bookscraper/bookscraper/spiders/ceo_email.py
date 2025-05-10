import scrapy
from urllib.parse import urlencode
import re

class CeoEmailSpider(scrapy.Spider):
    name = "ceo_email"
    allowed_domains = ["google.com"]
    start_urls = ["https://google.com"]
    def start_requests(self):
            search_url = 'https://www.google.com/search?q=%22%40gmail.com%22+AND+%22CEO%22&gl=us&hl=en'
            yield scrapy.Request(url=search_url, callback=self.parse)

    def parse(self, response):
        # Extract visible text content
        text = response.xpath('//body//text()').getall()
        full_text = ' '.join(text)
        
        # Find email addresses using regex
        emails = re.findall(r'\b[A-Za-z0-9._%+-]+@gmail\.com\b', full_text)
        
        for email in emails:
            yield {'email': email.lower()}

        # Pagination (next page)
        next_page = response.xpath('//a[@id="pnnext"]/@href').get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)