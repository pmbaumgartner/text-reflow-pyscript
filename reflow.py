import textwrap


def reflow(content: str, width: int = 80, indent: int = 0, comments: str = "") -> str:
    if comments.strip() != "":
        content = "\n".join(
            [line.lstrip().lstrip(comments) for line in content.splitlines()]
        )
    chunks = [block.strip() for block in content.split("\n\n")]
    result = []
    for chunk in chunks:
        content_lines = [line.strip() + " " for line in chunk.splitlines() if line != ""]
        text = "".join(content_lines)
        comment_width = 0 if comments == "" else len(comments) + 1
        preceeding_width = indent + comment_width
        text_lines = textwrap.wrap(text, width - preceeding_width)
        if comments != "":
            text_lines = [f"{comments} {line}" for line in text_lines]
        text = "\n".join(text_lines)
        if indent > 0:
            text = textwrap.indent(text, " " * indent)
        result.append(text)
    return f"\n{' ' * indent}{comments}\n".join(result)
