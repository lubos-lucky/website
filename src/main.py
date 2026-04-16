
from copystatic import copy_static_to_public
import os
import shutil
from generate_page import generate_page, generate_pages_recursive

def main():
    shutil.rmtree(os.path.join("./public"), ignore_errors=True)
    copy_static_to_public()
    generate_pages_recursive("./content", "./template.html", "./public")
    
    
    
if __name__ == "__main__":    main()