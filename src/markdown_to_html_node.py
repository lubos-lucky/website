from split_node_delimiter import split_nodes_delimiter
from textnode import TextNode
from textnode import TextType
from htmlnode import HTMLNode
from markdown_to_blocks import markdown_to_blocks, BlockType, block_to_block_type
from split_nodes import split_nodes_image, split_nodes_link
from parentnode import ParentNode
from leafnode import LeafNode
from text_to_textnodes import text_to_textnodes
from text_to_html import text_node_to_html_node

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    final_children = []
    for block in blocks:
        block_type = block_to_block_type(block)

        if block_type == BlockType.heading:
            heading_level = 0
            for char in block:
                if char == "#":
                    heading_level += 1
                else:
                    break
            children = text_to_childen(block[heading_level + 1:].strip())
            block_html_node = ParentNode(tag=f"h{heading_level}", children=children)   
            final_children.append(block_html_node)
        elif block_type == BlockType.paragraph:
            block = block.replace("\n", " ")
            children = text_to_childen(block)
            block_html_node = ParentNode(tag="p", children=children)
            final_children.append(block_html_node)
        elif block_type == BlockType.quote:
            new_lines = []
            for line in block.split("\n"):
                line = line.strip()
                if line.startswith(">"):
                    line = line[1:].strip()
                new_lines.append(line)
            lines = " ".join(new_lines)
            children = text_to_childen(lines)
            block_html_node = ParentNode(tag="blockquote", children=children)
            final_children.append(block_html_node)
        elif block_type == BlockType.code:
            textnode = TextNode(block[4:-3], TextType.PLAIN)
            
            leaf_nodes = [text_node_to_html_node(textnode)]
            code_nodes = ParentNode(tag="code", children=leaf_nodes)
            block_html_node = ParentNode(tag="pre", children=[code_nodes])
            final_children.append(block_html_node)
        elif block_type == BlockType.ordered_list:
            children = []
            for line in block.split("\n"):
                line = line.split(". ", 1)
                
                line_children = text_to_childen(line[1].strip())
                children.append(ParentNode(tag="li", children=line_children))
            block_html_node = ParentNode(tag="ol", children=children)
            final_children.append(block_html_node)
        elif block_type == BlockType.unordered_list:
            children = []
            for line in block.split("\n"):
                line = line.strip()
                if line and line.startswith("- "):
                    line = line[2:].strip()
                    line_children = text_to_childen(line)
                    children.append(ParentNode(tag="li", children=line_children))
            block_html_node = ParentNode(tag="ul", children=children)
            final_children.append(block_html_node)
    final_html_node = ParentNode(tag="div", children=final_children)
    return final_html_node

def text_to_childen(text):
    nodes  = text_to_textnodes(text)
    html_nodes = [text_node_to_html_node(node) for node in nodes]
    return html_nodes
