from split_node_delimiter import split_nodes_delimiter
from textnode import TextNode
from textnode import TextType
from htmlnode import HTMLNode
from markdown_to_blocks import markdown_to_blocks, BlockType, block_to_block_type
from split_nodes import split_nodes_image, split_nodes_link
from parentnode import ParentNode

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        block_type = block_to_block_type(block)
        textnode = TextNode(block.text, TextType.PLAIN)
        textnodes = [textnode]
        textnodes = split_nodes_image(textnodes)
        textnodes = split_nodes_link(textnodes)
        if block_type == BlockType.heading:
            
            heading_level = block.count("#")
            block.text = block.text[heading_level:].strip()
            heading_html_node = HTMLNode(tag=f"h{heading_level}", value=block.text)
            block.html_node = heading_html_node
        elif block_type == BlockType.paragraph:
            block.text = block.text.strip()
            block.html_node = HTMLNode(tag="p", value=block.text)
        elif block_type == BlockType.quote:
            block.html_node = HTMLNode(tag="blockquote", value=block.text)
        elif block_type == BlockType.code:
            block.html_node = HTMLNode(tag="pre", value=block.text)
        elif block_type == BlockType.ordered_list:
            block.html_node = HTMLNode(tag="ol", value=block.text)
        elif block_type == BlockType.unordered_list:
            block.html_node = HTMLNode(tag="ul", value=block.text)
    return blocks