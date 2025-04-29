import feedparser

# RSS feed URL'si
rss_url = "http://feeds.bbci.co.uk/news/rss.xml"

# Feed'i parse et
feed = feedparser.parse(rss_url)

# Feed'deki her bir entry'i yazdır
for entry in feed.entries:
    print("Başlık:", entry.title)
    print("Link:", entry.link)
    print("Yayın Tarihi:", entry.published)
    print("Özet:", entry.summary)
    print("\n")