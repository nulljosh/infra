"""BFS web crawler -- fetches pages and follows links up to a depth limit."""
from collections import deque
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup
import requests
from .robots import is_allowed

class Crawler:
    """BFS link crawler. Checks robots.txt before fetching each URL."""

    def __init__(self, seed_urls: list[str], max_depth: int = 2):
        self.seed_urls = seed_urls
        self.max_depth = max_depth
        self.visited: set[str] = set()

    def crawl(self):
        """Run BFS from seed_urls, yielding (url, text) tuples."""
        queue = deque()
        for url in self.seed_urls:
            queue.append((url, 0))

        while queue:
            url, depth = queue.popleft()
            if url in self.visited or depth > self.max_depth:
                continue
            if not is_allowed(url):
                continue

            self.visited.add(url)

            try:
                resp = requests.get(url, timeout=10, headers={"User-Agent": "NullBot/1.0"})
                resp.raise_for_status()
            except Exception:
                continue

            content_type = resp.headers.get("Content-Type", "")
            if "text/html" not in content_type:
                continue

            soup = BeautifulSoup(resp.text, "html.parser")

            # Extract visible text
            for tag in soup(["script", "style", "nav", "footer", "header"]):
                tag.decompose()
            text = soup.get_text(separator=" ", strip=True)

            yield url, text

            # Follow links if not at max depth
            if depth < self.max_depth:
                for link in soup.find_all("a", href=True):
                    abs_url = urljoin(url, link["href"])
                    parsed = urlparse(abs_url)
                    if parsed.scheme in ("http", "https") and abs_url not in self.visited:
                        queue.append((abs_url, depth + 1))
