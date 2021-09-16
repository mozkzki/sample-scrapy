# sample-scrapy

Scrapyのサンプルプロジェクト。

| No | 種別 | 起動方法 | Spider名 | Spiderファイル |
|--|--|--|--|--|
| 1 | 手動クローリング | make start1 | topics | main/yahoo_japan/spiders/topics.py |
| 2 | 自動クローリング | make start2 | news_crawl | main/yahoo_japan/spiders/news_crawl.py |

※ 2021/08/31 動作確認 (サイト変更により動かなくなる可能性あり)
## 参考サイト

- [Python, Scrapyの使い方（Webクローリング、スクレイピング） | note.nkmk.me](https://note.nkmk.me/python-scrapy-tutorial/)

## 開発環境

- 始め方は下記参照 (下記がベース)
  - [mozkzki/template-python-simple-with-dev-container](https://github.com/mozkzki/template-python-simple-with-dev-container)

## 開発方法

※ 以降のコマンドは、devcontainer (Dockerコンテナ) を起動し、そこで実行

### とりあえず一通り動確したい時

```sh
make lint
make ut
make start
```

### 実行

#### 1. リンクを指定してクローリング、スクレイピングする例

コード中で明示的にURLを指定してリンク先情報を取得する例。`topics.csv`が出力される。

```sh
cd main
scrapy crawl topics -o ./out/topics.csv
```

#### 2. リンクを抽出してクローリング、スクレイピングする例

Scrapyにページ内リンクを抽出させて自動でクロールする例。`news_crawl.csv`が出力される。

```sh
cd main
scrapy crawl news_crawl -o ./out/news_crawl.csv
```

#### scrapy shellによるデバッグ

インタラクティブシェルで`response.css("div.hoge")`等が試せる。

```sh
scrapy shell http://quotes.toscrape.com
# user angentの指定も可能
# scrapy shell -s USER_AGENT='<user_agent>' <url>
```

### Unit Test

全部実行

```sh
pytest
pytest -v # verbose
pytest -s # 標準出力を出す (--capture=noと同じ)
pytest -ra # サマリーを表示 (テストをpassしたもの以外)
pytest -rA # サマリーを表示 (テストをpassしたものも含む)
```

指定して実行  
(テストファイル名, パッケージ名, テストクラス名, メソッド名, 割と何でも拾ってくれる。部分一致でも。)

```sh
pytest -k items
pytest -k test_items.py
pytest -k yahoo_japan
```

マーカーを指定して実行

```sh
pytest -m 'slow'
pytest -m 'not slow'
```

カバレッジレポートも作成

```sh
pytest -v --capture=no --cov-config .coveragerc --cov=main --cov-report=xml --cov-report=term-missing .
# もしくは
make ut
```

VSCodeでコードカバレッジを見るには、Coverage Gutters (プラグイン) を入れる。表示されない場合は、コマンドパレットで`Coverage Gutters: Display Coverage`する。

- [VSCodeでカバレッジを表示する（pytest-cov）](https://zenn.dev/tyoyo/articles/769df4b7eb9398)

### Lint

```sh
flake8 --max-line-length=100 --ignore=E203,W503 ./main
# もしくは
make lint
```

### 依存パッケージ追加

下記ファイルに追記して`Rebuild Container`する。

- `requirements.txt`

`pip install`で追加すると下記の警告が出る場合がある。`--upgrade`すると`bin`以下が消えて既に導入済みのパッケージが使えなくなる。このため上記手順が無難。

```zsh
WARNING: Target directory /home/../. already exists. Specify --upgrade to force replacement.
```

## 参考

- [Configuration — pytest documentation](https://docs.pytest.org/en/6.2.x/customize.html)
- [Usage and Invocations — pytest documentation](https://docs.pytest.org/en/6.2.x/usage.html)
