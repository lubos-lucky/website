from textnode import TextNode, TextType
from text_to_textnodes import text_to_textnodes
import unittest

class TestTextToTextNodes(unittest.TestCase):
    def test_plain_text(self):
        text = "This is a plain text."
        nodes = text_to_textnodes(text)
        self.assertEqual(len(nodes), 1)
        self.assertEqual(nodes[0].text, text)
        self.assertEqual(nodes[0].text_type, TextType.PLAIN)

    def test_markdown_image(self):
        text = "This is an image: ![alt text](http://example.com/image.jpg)"
        nodes = text_to_textnodes(text)
        self.assertEqual(len(nodes), 2)
        self.assertEqual(nodes[0].text, "This is an image: ")
        self.assertEqual(nodes[0].text_type, TextType.PLAIN)
        self.assertEqual(nodes[1].text, "alt text")
        self.assertEqual(nodes[1].text_type, TextType.IMAGES)
        self.assertEqual(nodes[1].url, "http://example.com/image.jpg")
        

    def test_markdown_link(self):
        text = "This is a link: [link text](http://example.com)"
        nodes = text_to_textnodes(text)
        self.assertEqual(len(nodes), 2)
        self.assertEqual(nodes[0].text, "This is a link: ")
        self.assertEqual(nodes[0].text_type, TextType.PLAIN)
        self.assertEqual(nodes[1].text, "link text")
        self.assertEqual(nodes[1].text_type, TextType.LINKS)
        self.assertEqual(nodes[1].url, "http://example.com")
        

    def test_mixed_content(self):
        text = "Here is a link [link text](http://example.com) and an image ![alt text](http://example.com/image.jpg)"
        nodes = text_to_textnodes(text)
        self.assertEqual(len(nodes), 4)
        self.assertEqual(nodes[0].text, "Here is a link ")
        self.assertEqual(nodes[0].text_type, TextType.PLAIN)
        self.assertEqual(nodes[1].text, "link text")
        self.assertEqual(nodes[1].text_type, TextType.LINKS)
        self.assertEqual(nodes[1].url, "http://example.com")
        self.assertEqual(nodes[2].text, " and an image ")
        self.assertEqual(nodes[2].text_type, TextType.PLAIN)
        self.assertEqual(nodes[3].text, "alt text")
        self.assertEqual(nodes[3].text_type, TextType.IMAGES)
        self.assertEqual(nodes[3].url, "http://example.com/image.jpg")
        

    def test_bold_and_italic(self):
        text = "This is **bold** and *italic* text and a `code block`"
        nodes = text_to_textnodes(text)
        self.assertEqual(len(nodes), 6)
        self.assertEqual(nodes[0].text, "This is ")
        self.assertEqual(nodes[0].text_type, TextType.PLAIN)
        self.assertEqual(nodes[1].text, "bold")
        self.assertEqual(nodes[1].text_type, TextType.BOLD)
        self.assertEqual(nodes[2].text, " and ")
        self.assertEqual(nodes[2].text_type, TextType.PLAIN)
        self.assertEqual(nodes[3].text, "italic")
        self.assertEqual(nodes[3].text_type, TextType.ITALIC)
        self.assertEqual(nodes[4].text, " text and a ")
        self.assertEqual(nodes[4].text_type, TextType.PLAIN)
        self.assertEqual(nodes[5].text, "code block")
        self.assertEqual(nodes[5].text_type, TextType.CODE)