from extract import extract_markdown_images, extract_markdown_links
from extract_title import extract_title
import unittest

class TestExtract(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)
    

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a [link](https://example.com)"
        )
        self.assertListEqual([("link", "https://example.com")], matches)
    def test_extract_title(self):
        title = extract_title("# This is a title\nThis is some text")
        self.assertEqual("This is a title", title)