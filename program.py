import argparse
import sys

# ANSI Escape Codes
ANSI_RESET = "\u001b[0m"
ANSI_INVERSE = "\u001b[7m"

# HTML Formatting
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Formatted Output</title>
    <style>
        body {{
            font-family: monospace;
            white-space: pre;
            background-color: black;
            color: white;
        }}
        .inverse {{
            background-color: white;
            color: black;
        }}
    </style>
</head>
<body>
    <div class="inverse">
{content}
    </div>
</body>
</html>
"""

def format_console(text):
    """Formats text with ANSI escape codes for console output."""
    return f"{ANSI_INVERSE}{text}{ANSI_RESET}"

def format_html(text):
    """Formats text in an HTML template for file output."""
    return HTML_TEMPLATE.format(content=text)

def main():
    parser = argparse.ArgumentParser(description="Process some text.")
    parser.add_argument("--format", choices=["console", "html"], help="Specify the output format.")
    parser.add_argument("output", help="Specify the output file or 'stdout' for console output.")
    args = parser.parse_args()

    # Example text to be formatted
    text = "This is a sample formatted text."

    if args.format == "console" or (args.format is None and args.output == "stdout"):
        formatted_text = format_console(text)
        if args.output == "stdout":
            print(formatted_text)
        else:
            with open(args.output, "w") as file:
                file.write(formatted_text)
    elif args.format == "html" or (args.format is None and args.output != "stdout"):
        formatted_text = format_html(text)
        with open(args.output, "w") as file:
            file.write(formatted_text)
    else:
        print("Invalid format or output option. Use --help for more information.", file=sys.stderr)

if __name__ == "__main__":
    main()

