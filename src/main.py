from textnode import TextNode, TextType

def main():
    # Example usage of TextNode
    node1 = TextNode("Hello, World!", TextType.PLAIN)
    node2 = TextNode("This is bold text.", TextType.BOLD)
    node3 = TextNode("Visit OpenAI", TextType.LINKS, url="https://www.openai.com")
    
    print(node1)
    print(node2)
    print(node3)
    
if __name__ == "__main__":    main()