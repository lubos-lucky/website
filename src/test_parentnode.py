from parentnode import ParentNode
import unittest

from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
        parent_node.to_html(),
        "<div><span><b>grandchild</b></span></div>",
        )
    def test_to_html_without_tag(self):
        parent_node = ParentNode(children=[LeafNode("span", "child")])
        with self.assertRaises(ValueError):
            parent_node.to_html()
    def test_to_html_without_children(self):
        parent_node = ParentNode(tag="div")
        with self.assertRaises(ValueError):
            parent_node.to_html()