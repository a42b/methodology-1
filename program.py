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

def main_logic():
    """Placeholder for the main function logic."""
    return "This is a sample formatted text."

def process_text(format, output):
    text = main_logic()
    if format == "console" or (format is None and output == "stdout"):
        formatted_text = format_console(text)
        if output == "stdout":
            print(formatted_text)
        else:
            with open(output, "w") as file:
                file.write(formatted_text)
    elif format == "html" or (format is None and output != "stdout"):
        formatted_text = format_html(text)
        with open(output, "w") as file:
            file.write(formatted_text)
    else:
        print("Invalid format or output option. Use --help for more information.", file=sys.stderr)

def main():
    parser = argparse.ArgumentParser(description="Process some text.")
    parser.add_argument("--format", choices=["console", "html"], help="Specify the output format.")
    parser.add_argument("output", help="Specify the output file or 'stdout' for console output.")
    args = parser.parse_args()
    process_text(args.format, args.output)

if __name__ == "__main__":
    main()
