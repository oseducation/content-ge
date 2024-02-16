import scrapy
from scrapy.crawler import CrawlerProcess
from urllib.parse import urlencode
import json
import csv

# udemy scraper class
class UdemyScraper(scrapy.Spider):
    # scraper name
    name = 'udemy_scraper'
    
    # custom headers
    headers = {
        # "accept": "application/json, text/plain, */*",
        # "accept-encoding": "gzip, deflate, br",
        # "accept-language": "en-US,en;q=0.9",
        # "cache-control": "no-cache",
        # "pragma": "no-cache",
        "referer": "//www.udemy.com/courses/search/?p=1&q=entrepreneurship",
        # "sec-fetch-mode": "cors",
        # "sec-fetch-site": "same-origin",
        "user-agent":'Mozilla/5.0'
        # "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36",
        # "x-requested-with": "XMLHttpRequest",
        # "x-udemy-cache-brand": "UAen_US",
        # "x-udemy-cache-campaign-code": "UDEMYBASICS0720",
        # "x-udemy-cache-device": "desktop",
        # "x-udemy-cache-language": "en",
        # "x-udemy-cache-logged-in": "0",
        # "x-udemy-cache-marketplace-country": "UA",
        # "x-udemy-cache-modern-browser": "1",
        # "x-udemy-cache-price-country": "UA",
        # "x-udemy-cache-release": "a50355e6f369173f712c",
        # "x-udemy-cache-user": "",
        # "x-udemy-cache-version": "1"
    }

    headers2 = {
        "referer": "https://www.udemy.com/courses/search/?q=entrepreneurship",
        "user-agent":'Mozilla/5.0'
    }
    
    
    # output file column names
    column_names = [
        'title',
        'url',
        'rating',
        'num_reviews',
        'authors'
    ]

    # courses URL
    course_url = 'https://www.udemy.com/api-2.0/search-courses/?'
    
    # string query parameters
    params = {
        'p': 1,
        'q': 'entrepreneurship',
        'skip_price': 'true',
        'visible_instructors': '@all'
    }
    
    # init constructor
    def __init__(self):
        with open('udemy_entrepreneurship_courses.csv', 'w') as f:
            f.write(','.join(self.column_names) + '\n')
    
    # crawler's entry point
    def start_requests(self):
        # loop over the range of pages
        for page in range(1, 501): # replace '11' with '501' to scrape ALL data
            # update string query parameters
            self.params['p'] = page
            
            # crawl next page
            yield scrapy.Request(
                url=self.course_url + urlencode(self.params),
                headers=self.headers,
                callback=self.parse_courses
            )
    
    # courses API call response callback function
    def parse_courses(self, response):
        # parse JSON response
        courses = json.loads(response.text)['courses']
        
        # # extract courses' ids
        # ids = [str(course['id']) for course in courses]
        
        # # generate price API URL
        # price_url = 'https://www.udemy.com/api-2.0/pricing/?'
        
        # # price API string query parameters
        # price_params = {
        #     'course_ids': ','.join(ids),
        #     'fields[pricing_result]': 'price,discount_price,list_price,price_detail,price_serve_tracking_id'
        # }
        
        # fetch course author

        for course in courses:
            print("!!1 -> " , course)
            yield scrapy.Request(
                url='https://www.udemy.com' + course['url'],
                headers=self.headers2,
                meta={
                    'courses': courses
                },
                callback=self.parse_instructors
            )
        
    def parse_instructors(self, response):
        # get courses from meta container
        courses = response.meta.get('courses')
        
        print("!!!! -> ", response.text)

        # parse courses
        course_prices = json.loads(response.text)['courses']

        # map pricings to courses
        for course in courses:
            # extracted features
            # print("!!!! -> ", course)
            features = {
                'title': course['title'],
                
                'url': 'https://www.udemy.com' + course['url'],
                
                'rating': course['rating'],
                
                'num_reviews': course['num_reviews'],

                'authors': []
            }
            
            # try to extract price
            try:
                features['price'] = course_prices[str(course['id'])]['price']['price_string']
            
            except:
                pass
            
            # try to extract list price
            try:
                features['list_price'] = course_prices[str(course['id'])]['list_price']['price_string']
            
            except:
                pass
            
            # try to extract discount price
            try:
                features['discount_price'] = course_prices[str(course['id'])]['discount_price']['price_string']
            
            except:
                pass
            
            # try to extract price details
            try:
                features['price_detail'] = course_prices[str(course['id'])]['price_detail']['price_string']
            
            except:
                pass
            
            print(json.dumps(features, indent=2))
            
            # write features to CSV
            with open('udemy_entrepreneurship_courses.csv', 'a') as f:
                writer = csv.DictWriter(f, self.column_names)
                writer.writerow(features)
        

# main driver
if __name__ == '__main__':
    # run scraper
    process = CrawlerProcess()
    process.crawl(UdemyScraper)
    process.start()