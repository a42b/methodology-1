import re
import sys

def convert_markdown_to_html(markdown):
    def convert_bold(match):
        return "<b>" + match.group(1) + "</b>"
    
    def convert_italic(match):
        return "<i>" + match.group(1) + "</i>"
    
    def convert_monospaced(match):
        return "<tt>" + match.group(1) + "</tt>"
    
    def convert_preformatted(match):
        return "<pre>" + match.group(1) + "</pre>"
    
    paragraphs = markdown.strip().split('\n\n')
    html_paragraphs = []
    
    for paragraph in paragraphs:
        paragraph = re.sub(r'```([^`]*)```', convert_preformatted, paragraph)
        paragraph = re.sub(r'\*\*([^*]+)\*\*', convert_bold, paragraph)
        paragraph = re.sub(r'_([^_]+)_', convert_italic, paragraph)
        paragraph = re.sub(r'`([^`]+)`', convert_monospaced, paragraph)
        
        html_paragraphs.append('<p>' + paragraph.replace('\n', ' ') + '</p>')
    
    return '\n'.join(html_paragraphs)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python app.py /path/to/markdown", file=sys.stderr)
        sys.exit(1)
    
    input_path = sys.argv[1]
    
    try:
        with open(input_path, 'r', encoding='utf-8') as file:
            markdown_content = file.read()
        
        html_content = convert_markdown_to_html(markdown_content)
        print(html_content)
    
    except Exception as e:
        print(str(e), file=sys.stderr)
        sys.exit(1)
