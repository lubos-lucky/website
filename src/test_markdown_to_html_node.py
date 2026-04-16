import unittest
from markdown_to_html_node import markdown_to_html_node
from textnode import TextNode, TextType
from leafnode import LeafNode
from parentnode import ParentNode
from markdown_to_blocks import markdown_to_blocks, BlockType

class TestMarkdownToHtmlNode(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
        html,
        "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
    )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
        html,
        "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff</code></pre></div>",
    )
    def test_heading(self):
        md = """# Tolkien Fan Club

![JRR Tolkien sitting](/images/tolkien.png)

Here's the deal, **I like Tolkien**.

> "I am in fact a Hobbit in all but size."
>
> -- J.R.R. Tolkien

"""
        print(markdown_to_blocks(md))
        node = markdown_to_html_node(md)
        html = node.to_html()
        
        self.assertEqual(
        html,
        "<div><h1>Tolkien Fan Club</h1><p><img src=\"/images/tolkien.png\" alt=\"JRR Tolkien sitting\"></img></p><p>Here's the deal, <b>I like Tolkien</b>.</p><blockquote>\"I am in fact a Hobbit in all but size.\"  -- J.R.R. Tolkien</blockquote></div>,"
    )