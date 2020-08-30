import sys
import argparse

# error messages
ERR_ARG = "ERROR: Incorrect program argument format. Use -h to see correct argument format."

# reading command line arguments
argument_parser = argparse.ArgumentParser(description='Program loads a markdown file and a custom css file and converts into a compatible html representation of inline custom css wordpress file for FREE wordpress. Output file will be the same name and destination as the markdown source.')
argument_parser.add_argument('-s', '--source', action='store', dest='source', help="Path to the markdown source file.")
argument_parser.add_argument('-c', '--css', action='store', dest='css', help="Path to the css stylesheet.")
arguments = argument_parser.parse_args()

# file paths
markdown_path = None
css_path = None
output_path = None

# both arguments are required and have to be different
if arguments.source == None or arguments.css == None or arguments.source == arguments.css:
    print(ERR_ARG)
    exit(10)

markdown_path = arguments.source
css_path = arguments.css
# TODO: Output path
# output_path = 

# contains methods for parsing markdown and manages markdown source file state
class MarkdownParser:
    a = 1

# contains methods for parsing css and manages stylesheet state
class CSSParser:
    b = 1

# contains methods for generating html and manages output file state
class Generator:
    c = 1

# controlls the whole process, instanciates Parsers and Generator and uses them
def Main():
    print("Hello world!")

Main()