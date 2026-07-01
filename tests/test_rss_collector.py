import unittest
from pathlib import Path
import importlib.util


MODULE_PATH = Path(__file__).resolve().parents[1] / "src" / "main.py"
spec = importlib.util.spec_from_file_location("rss_collector", MODULE_PATH)
rss_collector = importlib.util.module_from_spec(spec)
spec.loader.exec_module(rss_collector)


class RssCollectorTests(unittest.TestCase):
    def test_parse_rss_feed(self):
        xml = """<?xml version=\"1.0\"?>
        <rss version=\"2.0\">
          <channel>
            <title>Example Feed</title>
            <item>
              <title>First item</title>
              <link>https://example.com/1</link>
              <description>Example description</description>
            </item>
          </channel>
        </rss>
        """

        items = rss_collector.parse_feed(xml)

        self.assertEqual(len(items), 1)
        self.assertEqual(items[0]["title"], "First item")
        self.assertEqual(items[0]["link"], "https://example.com/1")
        self.assertEqual(items[0]["description"], "Example description")

    def test_parse_atom_feed(self):
        xml = """<?xml version=\"1.0\"?>
        <feed xmlns=\"http://www.w3.org/2005/Atom\">
          <title>Example Atom Feed</title>
          <entry>
            <title>Atom item</title>
            <link href=\"https://example.com/atom\"/>
            <summary>Atom summary</summary>
          </entry>
        </feed>
        """

        items = rss_collector.parse_feed(xml)

        self.assertEqual(len(items), 1)
        self.assertEqual(items[0]["title"], "Atom item")
        self.assertEqual(items[0]["link"], "https://example.com/atom")
        self.assertEqual(items[0]["description"], "Atom summary")


if __name__ == "__main__":
    unittest.main()
