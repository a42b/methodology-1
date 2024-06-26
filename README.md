# methodology lab 1 
# Markdown to HTML Converter

## Description
This console application converts a subset of Markdown to HTML. It supports bold, italic, monospaced, and preformatted text, as well as paragraph formatting.

## Build and Run Instructions

### Prerequisites
- Python 3.x

### Steps to Build and Run
1. Clone the repository:
    ```sh
    git clone <repository_url>
    cd markdown_to_html
    ```

2. Run the application:
    ```sh
    python app.py /path/to/markdown [--out /path/to/output.html]
    ```

## Usage

### Input
The application accepts a Markdown file as input. It can process the following Markdown elements:
- **Bold text**: `**text**`
- _Italic text_: `_text_`
- `Monospaced text`: `` `text` ``
- ``` Preformatted text ```: ```` ```text``` ````

### Output
The application outputs the corresponding HTML. By default, the output is printed to the console (stdout). If the `--out` argument is provided, the output will be written to the specified file.

### Examples

1. **Output to stdout:**
    ```sh
    python app.py /path/to/valid/markdown
    ```

2. **Output to a file:**
    ```sh
    python app.py /path/to/valid/markdown --out /path/to/output.html
    ```

3. **Handle invalid markdown:**
    ```sh
    python app.py /path/to/invalid/markdown
    ```
    This will print an error message to stderr and exit with a non-zero status.

## Error Handling
If the Markdown file is invalid (e.g., unclosed tags or unsupported syntax), the application will output an error message to stderr and exit with a non-zero status code.

## Contribution
Feel free to fork this repository and contribute by submitting pull requests.


Link to the revert commit: https://github.com/a42b/methodology-1/commit/fdd725013bbb25f893778187acacd6bbde3025b8
