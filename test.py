from reflow import reflow
from textwrap import dedent

def test_reflow():
    text = """
    # This is a test of the reflow function. It should be able to reflow this text to a width of 80 characters, given a 4 character indent.
    #
    # This is a test of the reflow function. It should be able to reflow this text to a width of 80 characters, given a 4 character indent.
    """
    expected = """
# This is a test of the reflow function. It should be able to reflow this text
# to a width of 80 characters, given a 4 character indent.
#
# This is a test of the reflow function. It should be able to reflow this text
# to a width of 80 characters, given a 4 character indent.
    """.strip()
    assert reflow(text, 80, 0, "#") == dedent(expected)


if __name__ == "__main__":
    test_reflow()
