from split_nodes import split_nodes_image, split_nodes_link
import unittest
from textnode import TextNode, TextType

class TestSplitNodes(unittest.TestCase):
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png) and some more text",
            TextType.PLAIN,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
            TextNode("This is text with an ", TextType.PLAIN),
            TextNode("image", TextType.IMAGES, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and another ", TextType.PLAIN),
            TextNode(
                "second image", TextType.IMAGES, "https://i.imgur.com/3elNhQu.png"
            ),
            TextNode(" and some more text", TextType.PLAIN),
            ],
        new_nodes,
        )
    def test_split_links(self):
        node = TextNode(
            "This is text with a [link](https://www.openai.com) and another [second link](https://www.google.com) and some more text",
            TextType.PLAIN,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
            TextNode("This is text with a ", TextType.PLAIN),
            TextNode("link", TextType.LINKS, "https://www.openai.com"),
            TextNode(" and another ", TextType.PLAIN),
            TextNode(
                "second link", TextType.LINKS, "https://www.google.com"
            ),
            TextNode(" and some more text", TextType.PLAIN),

            ],
        new_nodes,
        )
    