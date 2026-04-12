import re
from extract import extract_markdown_images, extract_markdown_links
from textnode import TextNode, TextType

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.PLAIN:
            new_nodes.append(node)
            continue
        image_urls = extract_markdown_images(node.text)
        if not image_urls:
            new_nodes.append(node)
            continue
        original_text = node.text
        for alt,url in image_urls:
            sections = original_text.split(f"![{alt}]({url})", 1)
            if sections[0]:
                new_nodes.append(TextNode(sections[0], TextType.PLAIN))
            new_nodes.append(TextNode(alt, TextType.IMAGES, url))
            
            original_text = sections[1]
        if original_text:
            new_nodes.append(TextNode(original_text, TextType.PLAIN))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.PLAIN:
            new_nodes.append(node)
            continue
        link_urls = extract_markdown_links(node.text)
        if not link_urls:
            new_nodes.append(node)
            continue
        original_text = node.text
        for alt,url in link_urls:
            sections = original_text.split(f"[{alt}]({url})", 1)
            if sections[0]:
                new_nodes.append(TextNode(sections[0], TextType.PLAIN))
            new_nodes.append(TextNode(alt, TextType.LINKS, url))
            
            original_text = sections[1]
        if original_text:
            new_nodes.append(TextNode(original_text, TextType.PLAIN))
    return new_nodes