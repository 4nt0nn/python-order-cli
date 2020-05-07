import sys
import argparse
import orderrunner.funcmodule as fm


def main():
    """Main method that takes the parser argument.
    """
    parser = argparse.ArgumentParser(
        prog='Ordercli', description='Analyzes an order file.')
    parser.add_argument(
        'filepath', help='Type the path (including extension) of the file')
    args = parser.parse_args()
    fm.get_content(args.filepath)


if __name__ == '__main__':
    main()
