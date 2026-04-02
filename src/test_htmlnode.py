from htmlnode import HTMLNode
import unittest

class TestHTMLNode(unittest.TestCase):
    def test_init(self):
        node = HTMLNode(tag="div", value="Hello", children=[], props={"class": "my-div"})
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.value, "Hello")
        self.assertEqual(node.children, [])
        self.assertEqual(node.props, {"class": "my-div"})
    def test_props_to_html(self):
        node = HTMLNode(props={"class": "my-div", "id": "main"})
        self.assertEqual(node.props_to_html(), ' class="my-div" id="main"')
    def test_repr(self):
        node = HTMLNode(tag="p", value="Paragraph", children=[], props={"style": "color: red;"})
        expected_repr = "HTMLNode(tag=p, value=Paragraph, children=[], props={'style': 'color: red;'})"
        self.assertEqual(repr(node), expected_repr)