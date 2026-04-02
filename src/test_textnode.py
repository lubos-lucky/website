import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    def test_neq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a different text node", TextType.BOLD)
        self.assertNotEqual(node, node2)
    def url_test(self):
        node = TextNode("Visit OpenAI", TextType.LINKS, url="https://www.openai.com")
        self.assertEqual(node.url, "https://www.openai.com")
    def test_repr(self):
        node = TextNode("Hello, World!", TextType.PLAIN)
        self.assertEqual(repr(node), "TextNode(Hello, World!,1,None)")


if __name__ == "__main__":
    unittest.main()