"""Tests for crawler and robots.txt parser."""
import pytest
from unittest.mock import patch, MagicMock
from src.crawler.crawler import Crawler
from src.crawler import robots

def test_robots_allowed():
    with patch("src.crawler.robots.RobotFileParser") as mock_rp_class:
        mock_rp = MagicMock()
        mock_rp.can_fetch.return_value = True
        mock_rp_class.return_value = mock_rp
        robots._parsers.clear()
        assert robots.is_allowed("http://example.com/page") is True

def test_robots_disallowed():
    with patch("src.crawler.robots.RobotFileParser") as mock_rp_class:
        mock_rp = MagicMock()
        mock_rp.can_fetch.return_value = False
        mock_rp_class.return_value = mock_rp
        robots._parsers.clear()
        assert robots.is_allowed("http://example.com/private") is False

def test_crawler_basic():
    html = '<html><body><p>Hello world</p><a href="/page2">link</a></body></html>'
    mock_resp = MagicMock()
    mock_resp.text = html
    mock_resp.headers = {"Content-Type": "text/html"}
    mock_resp.raise_for_status = MagicMock()

    with patch("src.crawler.crawler.requests.get", return_value=mock_resp), \
         patch("src.crawler.crawler.is_allowed", return_value=True):
        crawler = Crawler(["http://example.com"], max_depth=0)
        results = list(crawler.crawl())
        assert len(results) == 1
        assert results[0][0] == "http://example.com"
        assert "Hello world" in results[0][1]

def test_crawler_respects_depth():
    html = '<html><body><p>Page</p><a href="http://example.com/deep">link</a></body></html>'
    mock_resp = MagicMock()
    mock_resp.text = html
    mock_resp.headers = {"Content-Type": "text/html"}
    mock_resp.raise_for_status = MagicMock()

    with patch("src.crawler.crawler.requests.get", return_value=mock_resp), \
         patch("src.crawler.crawler.is_allowed", return_value=True):
        crawler = Crawler(["http://example.com"], max_depth=0)
        results = list(crawler.crawl())
        assert len(results) == 1  # only seed, no following links

def test_crawler_skips_visited():
    html = '<html><body><p>Page</p></body></html>'
    mock_resp = MagicMock()
    mock_resp.text = html
    mock_resp.headers = {"Content-Type": "text/html"}
    mock_resp.raise_for_status = MagicMock()

    with patch("src.crawler.crawler.requests.get", return_value=mock_resp), \
         patch("src.crawler.crawler.is_allowed", return_value=True):
        crawler = Crawler(["http://example.com", "http://example.com"], max_depth=0)
        results = list(crawler.crawl())
        assert len(results) == 1  # deduplicated
