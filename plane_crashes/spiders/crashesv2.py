import scrapy


class CrashInfoV2Spider(scrapy.Spider):
    name = "crashesv2"
    start_urls = ["https://aviation-safety.net/database/"]

    def parse(self, response):
        for href in response.xpath('//a[contains(., "1") or contains(., "2")]'):
            yield response.follow(href, self.parse_crashes_in_a_year)

    def parse_crashes_in_a_year(self, response):
        for href in response.xpath("//td//nobr//a"): 
            yield response.follow(href, self.parse_crash_info)

    def parse_crash_info(self, response):
        yield {
            'date': response.xpath('//td/font/text()')[0].get(),
            'time': response.xpath('//td/font/text()')[1].get(),
            'location': response.xpath('//td/font/text()')[2].get(),
            'operator': response.xpath('//td/font/text()')[3].get(),
            'flight_number': response.xpath('//td/font/text()')[4].get(),
            'route': response.xpath('//td/font/text()')[5].get(),
            'ac_type': response.xpath('//td/font/text()')[6].get(),
            'registration': response.xpath('//td/font/text()')[7].get(),
            'cn/in': response.xpath('//td/font/text()')[8].get(),
            'aboard': response.xpath('//td/font/text()')[9].get(),
            'fatalities': response.xpath('//td/font/text()')[10].get(),
            'ground': response.xpath('//td/font/text()')[11].get(),
            'summary': response.xpath('//td/font/text()')[12].get()
        }
