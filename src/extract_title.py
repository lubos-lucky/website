

def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        line = line.strip()
        if line.startswith("# "):
            return line[2:].strip()
        else:
            raise Exception("Title not found in markdown. Title should be the first line and start with '# '")
    