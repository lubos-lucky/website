from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag = None, children=None, props=None):
        super().__init__(tag, children,props)
        self.children = children

    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode must have a tag to convert to HTML")
        if self.children is None:
            raise ValueError("ParentNode must have children to convert to HTML")
        return f"<{self.tag}{self.props_to_html()}>{''.join(child.to_html() for child in self.children)}</{self.tag}>"