import re

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
