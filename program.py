import re
import sys
import os

def convert_markdown_to_html(markdown):
    # Helper functions to convert markdown to HTML
    def convert_preformatted(match):
        return "<pre>\n" + match.group(1) + "\n</pre>"
    
    def convert_bold(match):
        return "<b>" + match.group(1) + "</b>"
    
    def convert_italic(match):
        return "<i>" + match.group(1) + "</i>"
    
    def convert_monospaced(match):
        return "<tt>" + match.group(1) + "</tt>"
    
    # Check for unclosed tags in the text
    def check_unclosed_tags(text):
        if re.search(r'(\*\*[^*]+$|_[^_]+$|`[^`]+$)', text):
            raise ValueError("Error: invalid markdown - unclosed tag detected")

    # Split text into paragraphs
    paragraphs = markdown.strip().split('\n\n')
    html_paragraphs = []
    
    for paragraph in paragraphs:
        check_unclosed_tags(paragraph)
        
        paragraph = re.sub(r'```([^`]*)```', convert_preformatted, paragraph)
        paragraph = re.sub(r'\*\*([^*]+)\*\*', convert_bold, paragraph)
        paragraph = re.sub(r'_([^_]+)_', convert_italic, paragraph)
        paragraph = re.sub(r'`([^`]+)`', convert_monospaced, paragraph)
        
        html_paragraphs.append('<p>' + paragraph.replace('\n', ' ') + '</p>')
    
    return '\n'.join(html_paragraphs)

def main(input_path, output_path=None):
    try:
        if not os.path.isfile(input_path):
            raise FileNotFoundError(f"Error: file '{input_path}' not found")

        with open(input_path, 'r', encoding='utf-8') as file:
            markdown_content = file.read()
        
        html_content = convert_markdown_to_html(markdown_content)
        
        if output_path:
            with open(output_path, 'w', encoding='utf-8') as file:
                file.write(html_content)
        else:
            print(html_content)
    
    except Exception as e:
        print(str(e), file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python app.py /path/to/markdown [--out /path/to/output.html]", file=sys.stderr)
        sys.exit(1)
    
    input_path = sys.argv[1]
    output_path = None
    
    if len(sys.argv) == 4 and sys.argv[2] == "--out":
        output_path = sys.argv[3]
    
    main(input_path, output_path)
