from markdown_to_blocks import markdown_to_blocks, block_to_block_type, BlockType
from textnode import TextNode, TextType
import unittest

class TestMarkdownToBlocks(unittest.TestCase):
        def test_markdown_to_blocks(self):
            md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
            blocks = markdown_to_blocks(md)
            self.assertEqual(
                blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )
        
        def test_markdown_to_blocks_empty(self):
            md = ""
            blocks = markdown_to_blocks(md)
            self.assertEqual(blocks, [])
        
        def test_block_to_block_type(self):
            self.assertEqual(block_to_block_type("# Heading"), BlockType.heading)
            self.assertEqual(block_to_block_type("```\n\ncode block\n```"), BlockType.code)
            self.assertEqual(block_to_block_type("> Quote"), BlockType.quote)
            self.assertEqual(block_to_block_type("- List item"), BlockType.unordered_list)
            self.assertEqual(block_to_block_type("1. Ordered item"), BlockType.ordered_list)
            self.assertEqual(block_to_block_type("Just a paragraph"), BlockType.paragraph)