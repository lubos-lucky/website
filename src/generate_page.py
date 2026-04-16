from markdown_to_html_node import markdown_to_html_node
from extract_title import extract_title
import os
from pathlib import Path

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using template {template_path}")
    with open(from_path, "r") as f:
        markdown_file = f.read()
    with open(template_path, "r") as f:
        template_file = f.read()
    html_string = markdown_to_html_node(markdown_file).to_html()
    title = extract_title(markdown_file)
    final_html = template_file.replace("{{ Content }}", html_string).replace("{{ Title }}", title)
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, "w") as f:
        f.write(final_html)
       
def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for content_file in os.listdir(dir_path_content):
        if os.path.isfile(os.path.join(dir_path_content, content_file)):
            from_path = os.path.join(dir_path_content, content_file)
            dest_path = os.path.join(dest_dir_path, content_file)
            html_dest_path = Path(dest_path).with_suffix(".html")
            generate_page(from_path, template_path, html_dest_path)
        if os.path.isdir(os.path.join(dir_path_content, content_file)):
            generate_pages_recursive(os.path.join(dir_path_content, content_file), template_path, os.path.join(dest_dir_path, content_file))
    