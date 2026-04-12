from enum import Enum


class BlockType(Enum):
    paragraph = "paragraph"
    heading = "heading"
    code = "code"
    quote = "quote"
    unordered_list = "unordered_list"
    ordered_list = "ordered_list"


def markdown_to_blocks(markdown):
    if markdown == "":
        return []
    lines = markdown.split("\n\n")
    lines = [line.strip() for line in lines if line.strip() != ""]
    
    return lines
    
def block_to_block_type(block):
    if block.startswith("#"):
        return BlockType.heading
    elif block.startswith("```\n\n") and block.endswith("```"):
        return BlockType.code
    elif block.startswith(">"):
        return BlockType.quote
    elif block.startswith("- "):
        return BlockType.unordered_list
    elif block[0].isdigit() and block[1:3] == ". ":
        return BlockType.ordered_list
    else:
        return BlockType.paragraph