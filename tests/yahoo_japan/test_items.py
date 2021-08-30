from main.yahoo_japan.items import YahooJapanItem


class TestYahooJapanItem:
    def test(self):
        item = YahooJapanItem()
        assert item.fields == {"headline": {}, "title": {}, "url": {}}
