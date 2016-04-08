import unittest
from tests_cases import generated_pages, generated_html, generated_examples


class PaginatorTest(unittest.TestCase):

    # Test a generation of paginator:
    def test_generate_page(self):
        for page in generated_pages:
            self.assertEqual(page["result"].create_paginator(), page["expected"])

    # Test a generation of html:
    def test_generate_html(self):
        for html in generated_html:
            self.assertEqual(str(html["result"]).replace("\t", "").replace("\n", ""), html["expected"])

    # Save a html file:
    def test_save_html(self):
        content = '<html>'\
                  '\n<head>'\
                  '\n\t<link rel="stylesheet" href="bootstrap.min.css">\n\t<meta charset="UTF-8">' \
                  '\n</head>' \
                  '\n<body>\n{0}\n</body>\n' \
                  '</html>'
        body = ""
        for example in generated_examples:
            body += "<div> {0} </div>\n".format(str(example))
        file = open("html/main.html", "w", encoding="utf8")
        file.write(content.format(body))
        file.close()


if __name__ == '__main__':
    unittest.main()

