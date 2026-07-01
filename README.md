# MVP Projects

This repository contains small MVP-style projects. The current project is an RSS feed collector built in Python.

## RSS Collector

The RSS collector fetches an RSS or Atom feed URL and prints the latest items with their titles and links.

### Run the script

From the repository root, run:

```bash
python3 src/main.py https://techcrunch.com/feed/
```

### Run the tests

```bash
python3 -m unittest discover -s tests -v
```

### What it uses

- Python 3
- feedparser
- unittest
