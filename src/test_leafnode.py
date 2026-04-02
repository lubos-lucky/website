from leafnode import LeafNode
import unittest

class TestLeafNode(unittest.TestCase):
    def test_to_html_with_tag(self):
        node = LeafNode(tag="p", value="Hello, World!")
        self.assertEqual(node.to_html(), "<p>Hello, World!</p>")
    def test_to_html_without_tag(self):
        node = LeafNode(value="Just some text")
        self.assertEqual(node.to_html(), "Just some text")
    def test_to_html_missing_value(self):
        node = LeafNode(tag="p")
        with self.assertRaises(ValueError):
            node.to_html()
    def test_repr(self):
        node = LeafNode(tag="span", value="Test", props={"class": "highlight"})
        self.assertEqual(repr(node), "LeafNode(tag=span, value=Test, props={'class': 'highlight'})")