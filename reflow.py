import textwrap


def reflow(content: str, width: int = 80, indent: int = 0, comments: str = "") -> str:
    content_lines = []
    for line in content.splitlines():
        if line.isspace():
            content_lines.append(line)
            continue
        if comments != "":
            # don't use replace(),
            # as that will remove non-leading characters in this string
            line = line.lstrip().lstrip(comments).lstrip()
        content_lines.append(line.strip() + " ")
    text = "".join(content_lines)
    comment_width = 0 if comments == "" else len(comments) + 1
    preceeding_width = indent + comment_width
    # text = " ".join(l.strip() for l in content.splitlines() if l.isspace())
    text_lines = textwrap.wrap(text, width - preceeding_width)
    if comments != "":
        text_lines = [f"{comments} {line}" for line in text_lines]
    text = "\n".join(text_lines)
    if indent > 0:
        text = textwrap.indent(text, " " * indent)
    return text
