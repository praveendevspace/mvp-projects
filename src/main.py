from __future__ import annotations

import io
import ssl
import sys
import urllib.request
from typing import Dict, List

import feedparser


def collect_feed(feed_url: str) -> List[Dict[str, str]]:
    """Fetch and parse an RSS or Atom feed from a URL."""
    feed_xml = fetch_feed_content(feed_url)
    return parse_feed(feed_xml)


def fetch_feed_content(feed_url: str) -> str:
    """Download feed content with a browser-like user agent."""
    request = urllib.request.Request(
        feed_url,
        headers={"User-Agent": "Mozilla/5.0"},
    )
    context = ssl._create_unverified_context()
    with urllib.request.urlopen(request, context=context, timeout=15) as response:
        return response.read().decode("utf-8", errors="replace")


def parse_feed(feed_xml: str) -> List[Dict[str, str]]:
    """Parse raw RSS or Atom XML into a list of item dictionaries."""
    parsed = feedparser.parse(io.BytesIO(feed_xml.encode("utf-8")))
    return _items_from_parsed(parsed)


def _items_from_parsed(parsed) -> List[Dict[str, str]]:
    return [
        {
            "title": entry.get("title", ""),
            "link": entry.get("link", ""),
            "description": entry.get("summary", entry.get("description", "")),
        }
        for entry in getattr(parsed, "entries", [])
    ]


if __name__ == "__main__":
    if len(sys.argv) > 1:
        feed_url = sys.argv[1]
        for item in collect_feed(feed_url):
            print(f"{item['title']} -> {item['link']}")
    else:
        print("Usage: python3 src/main.py <feed-url>")
