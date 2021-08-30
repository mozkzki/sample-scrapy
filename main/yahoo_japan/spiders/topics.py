import scrapy
from yahoo_japan.items import YahooJapanItem


class TopicsSpider(scrapy.Spider):
    name = "topics"
    # www.yahoo.co.jpやnews.yahoo.co.jpを全部許可する
    allowed_domains = ["yahoo.co.jp"]
    start_urls = ["http://yahoo.co.jp/"]

    def parse(self, response):
        for topic in response.css("section#tabpanelTopics1 article"):
            item = YahooJapanItem()
            item["headline"] = topic.css("h1 span::text").extract_first()
            # 自前でリンク先ページ(第一引数がURL)をリクエストしてクローリング
            yield scrapy.Request(
                topic.css("a::attr(href)").extract_first(),
                callback=self.parse_detail,
                meta={"item": item},
            )

    # リンク先ページのスクレイピング
    def parse_detail(self, response):
        item = response.meta["item"]
        item["url"] = response.url
        item["title"] = response.css(
            "div#yjnMain article div[data-ual-view-type='digest'] a p::text"
        ).extract_first()
        yield item
