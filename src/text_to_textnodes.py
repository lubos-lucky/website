from textnode import TextNode, TextType
from split_nodes import split_nodes_image, split_nodes_link
from extract import extract_markdown_images, extract_markdown_links
from split_node_delimiter import split_nodes_delimiter

def text_to_textnodes(text):
    initial_node = TextNode(text, TextType.PLAIN)
    nodes = []
    nodes = split_nodes_image([initial_node])
    nodes = split_nodes_link(nodes)
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    return nodes