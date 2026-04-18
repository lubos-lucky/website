
from copystatic import copy_static_to_docs
import os
import shutil
from generate_page import generate_page, generate_pages_recursive
import sys

def main():
    basepath = sys.argv[1] if len(sys.argv) > 1 else "/"

    shutil.rmtree(os.path.join("./docs"), ignore_errors=True)
    copy_static_to_docs()
    generate_pages_recursive("./content", "./template.html", "./docs", basepath)

if __name__ == "__main__":    main()