from argparse import ArgumentParser
from os import chdir

from githubwikipageindex import insert_page_index, generate_page_index

if __name__ == "__main__":

    parser = ArgumentParser(description="Generate a Page Index for a GitHub Wiki. ")
    parser.add_argument("wiki_dir", help="Path to the clone of your GitHub Wiki")
    parser.add_argument("-i", "--insert",
                        help="Automatically insert the Page Index into your Home.md file",
                        action="store_true")
    args = parser.parse_args()

    chdir(args.wiki_dir)

    if args.insert:
        print("Generating Page Index and inserting into Home.md")
        insert_page_index()
    else:
        print("Generating Page Index and printing to stdout")
        print(generate_page_index())
