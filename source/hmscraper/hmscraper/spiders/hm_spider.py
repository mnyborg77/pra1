import scrapy


class HmSpider(scrapy.Spider):
    """
    A class used to represent a scrapy Spider.

    ...

    Attributes
    ----------
    name : str
        the name of the spider
    allowed_domains : list
        a list of the allowed domain the spider can crawl
    start_urls : list
        a list of the start urls for the spider

    Methods
    -------
    parse(response)
        Parse all urls for HM for each European country.
    parse_deals(response)
        Parse all the urls containing deals/offers.
    parse_products(response)
        Parse all the products inside the deals/offers pages.
    """

    name = "hm"
    allowed_domains = ["www2.hm.com"]
    start_urls = ["https://www.hm.com/entrance.ahtml"]

    def parse(self, response):
        """Parse all urls for HM for each European country.

        Args:
            response (Response obj): response object recieved when a request is sent to the start_urls.

        Yields:
            link to follow in the next step
        """
        # Gets links for the countries in Europe identified by "column col-three" and
        # then follow that link.
        europe = response.css("div.column.col-three")
        for url in europe.css("a.market-link::attr(href)"):
            yield response.follow(url.get(), callback=self.parse_deals)

    def parse_deals(self, response):
        """Parse all the urls containing deals/offers.

        Args:
            response (Response obj): response object recieved when a request is sent to a country url.

        Yields:
            link to follow in the next step
        """
        # Processes only responses with status 200 or 302.
        if response.status == 200 or response.status == 302:
            # Find links that contain the words "deal" or "offers" or "angebote".
            # Then follows that link to get the products.
            try:
                for link in response.xpath(
                    '//a/@href[contains(., "deal") or contains(., "offers") or contains(., "angebote")]'
                ):
                    yield response.follow(link.get(), callback=self.parse_products)
            except:
                pass

    def parse_products(self, response):
        """Parse all the products inside the deals/offers pages.

        Args:
            response (Response obj): response object recieved when a request is sent to a deals/offers url.

        Yields:
            dict: return a dictionary with the following keys:
                main page: url to where the deal is found
                name: name of the the product scraped
                url: url of the product
                price: price of the product
        """
        # Extract the product data inside the tag div with class "item-details".
        # Store the data in a dictionary
        products = response.css("div.item-details")
        for product in products:
            yield {
                "main page": response.url,
                "name": product.css("a.link::text").get().strip(),
                "url": product.css("a.link::attr(href)").get(),
                "price": product.css("strong.item-price span::text").get().strip(),
            }
        # The product are distributed in several pages. When finished scraping one page,
        # follow the link at the end with a tag with class "pagination-links-list".
        # Repeat until all product are retrieved.
        try:
            next_page = response.css("a.pagination-links-list").attrib["href"]
        except:
            next_page = None
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse_products)
