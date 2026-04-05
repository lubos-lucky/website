from textnode import TextNode
from textnode import TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.PLAIN:
            new_nodes.append(node)
            continue
        parts = node.text.split(delimiter)
        if len(parts) % 2 == 0:
            raise Exception(f"No closing delimiter found for {delimiter} in text: {node.text}")
        for i, part in enumerate(parts):
            if part:
                if i == 0 or i % 2 == 0:
                    new_nodes.append(TextNode(part, TextType.PLAIN))
                else:
                    new_nodes.append(TextNode(part, text_type))
    return new_nodes