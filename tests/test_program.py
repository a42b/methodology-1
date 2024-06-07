import unittest
from program import format_console, format_html, main_logic

class TestProgram(unittest.TestCase):

    def test_format_console(self):
        text = "test"
        expected_output = "\u001b[7mtest\u001b[0m"
        self.assertEqual(format_console(text), expected_output)

    def test_format_html(self):
        text = "test"
        expected_output = """
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
test
    </div>
</body>
</html>
"""
        self.assertEqual(format_html(text).strip(), expected_output.strip())

    def test_main_logic(self):
        expected_output = "This is a sample formatted text."
        self.assertEqual(main_logic(), expected_output)

if __name__ == '__main__':
    unittest.main()
