import sys
import argparse
import enum

# error messages
ERR_ARG = "ERROR: Incorrect program argument format. Use -h to see correct argument format." # 10
ERR_CSS = "ERROR: Unknown css parser state." # 20
ERR_MD = "ERROR: Unknown markdown parser state." # 30

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
    # TODO: Run program with sample inputs
    # exit(10)

markdown_path = arguments.source
css_path = arguments.css
# TODO: Output path
# output_path = 

# contains methods for parsing markdown and manages markdown source file state
class MarkdownParser:
    a = 1

# contains methods for parsing css and manages stylesheet state
class CSSParser:
    class Parser_State(enum.Enum):
        Ready = 0
        Enter = 1
        Attribute = 2
        AttributeValue = 3
        Leave = 4

    css_file = None
    state = Parser_State.Ready

    def __init__(self):
        self.css_file = open(css_path, "r")

    def getNextClass(self):
        line = None
        className = None
        attributes = {}

        if self.state == self.Parser_State.Ready:
            line = self.css_file.readline()

        elif self.state == self.Parser_State.Enter:
            pass
        
        else:
            self.css_file.close()
            print(ERR_CSS)
            exit(20)

        return (className, attributes)

# contains methods for generating html and manages output file state
class Generator:
    c = 1

# controlls the whole process, instanciates Parsers and Generator and uses them
def Main():
    markdownParser = MarkdownParser()
    cssParser = CSSParser()
    generator = Generator()

    classDictionary = {}

    print("Hello world!")

Main()