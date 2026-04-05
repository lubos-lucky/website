from textnode import TextNode
from leafnode import LeafNode
from textnode import TextType

def text_node_to_html_node(text_node):
    if text_node.text_type == TextType.PLAIN:
        return LeafNode(value=text_node.text)
    elif text_node.text_type == TextType.BOLD:
        return LeafNode(tag="b", value=text_node.text)
    elif text_node.text_type == TextType.ITALIC:
        return LeafNode(tag="i", value=text_node.text)
    elif text_node.text_type == TextType.CODE:
        return LeafNode(tag="code", value=text_node.text)
    elif text_node.text_type == TextType.LINKS:
        return LeafNode(tag="a", value=text_node.text, props=f' href="{text_node.url}"')
    elif text_node.text_type == TextType.IMAGES:
        return LeafNode(tag="img", props=f' src="{text_node.url}" alt="{text_node.text}"')
    else:
        raise Exception(f"Unsupported TextType: {text_node.text_type}")