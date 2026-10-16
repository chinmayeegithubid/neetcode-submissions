class Solution:
    def __init__(self):
        self.urls = {}
        self.next_id = 1

    def encode(self, longUrl: str) -> str:
        shortUrl = f"http://tinyurl.com/{self.next_id}"
        self.urls[shortUrl] = longUrl
        self.next_id += 1
        return shortUrl

    def decode(self, shortUrl: str) -> str:
        return self.urls[shortUrl]