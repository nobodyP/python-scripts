import sys
import re

def process_line(line):
    # Split the line by tabs to get the filename and content
    parts = line.split('\t')
    if len(parts) == 2:
        filename = parts[0]
        content = parts[1]

        # Remove text within parentheses and the space before them using regular expressions
        content = re.sub(r' \([^)]*\)', '', content)

        # Save the content to a file with the name before the tab
        with open(filename + ".txt", "a") as output_file:
            output_file.write(content + '\n')

def main(input_file):
    with open(input_file, 'r') as file:
        for line in file:
            process_line(line)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py input_file")
    else:
        input_file = sys.argv[1]
        main(input_file)
