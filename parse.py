"""
Takes in HTML document
returns text file
"""

import sys, HTMLParser
from bs4 import BeautifulSoup

def convert(some_HTML):
    HTML_text = BeautifulSoup(some_HTML)
    just_text = HTML_text.get_text()
    return just_text


def main():
    script, input_text, output_text = sys.argv

    open_file = open(input_text, 'rb')
    input_text = open_file.read()
    open_file.close()

    just_text = convert(input_text)

    text_file = open(output_text, 'wb')
    text_file.write(just_text.encode("utf-8"))
    text_file.close()

main()