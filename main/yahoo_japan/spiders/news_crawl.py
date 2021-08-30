from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from yahoo_japan.items import YahooJapanNewsItem


class NewsCrawlSpider(CrawlSpider):
    name = "news_crawl"
    # www.yahoo.co.jpやnews.yahoo.co.jpを全部許可する
    allowed_domains = ["yahoo.co.jp"]
    start_urls = ["http://news.yahoo.co.jp/"]

    # ナビゲーションのタブを全てチェックする
    rules = (Rule(LinkExtractor(restrict_css="nav div#snavi ul li"), callback="parse_item"),)

    def parse_item(self, response):
        # 選択されたタブは`.jTRJbz`が付与される
        # 選択されたタブのカテゴリ文字列を取得
        category = response.css("nav div#snavi ul li.jTRJbz a::text").extract_first()
        # 記事(トピックス)を1件ずつ取得
        for topic in response.css("section.topics div ul li"):
            item = YahooJapanNewsItem()
            item["headline"] = topic.css("a::text").extract_first()
            item["url"] = topic.css("a::attr(href)").extract_first()
            item["category"] = category
            yield item
