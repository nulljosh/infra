"""robots.txt parser -- check crawl permissions before fetching."""
from urllib.parse import urlparse
from urllib.robotparser import RobotFileParser
import requests

_parsers: dict[str, RobotFileParser] = {}

def _get_parser(url: str) -> RobotFileParser:
    """Fetch and cache robots.txt for the given URL's host."""
    parsed = urlparse(url)
    base = f"{parsed.scheme}://{parsed.netloc}"
    if base not in _parsers:
        rp = RobotFileParser()
        robots_url = f"{base}/robots.txt"
        rp.set_url(robots_url)
        try:
            rp.read()
        except Exception:
            rp.allow_all = True
        _parsers[base] = rp
    return _parsers[base]

def is_allowed(url: str, user_agent: str = "*") -> bool:
    """Return True if crawling url is permitted by that host's robots.txt."""
    try:
        parser = _get_parser(url)
        return parser.can_fetch(user_agent, url)
    except Exception:
        return True
