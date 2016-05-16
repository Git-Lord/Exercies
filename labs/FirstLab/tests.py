# -*- coding: utf-8 -*-

import unittest
from tests_cases import *


class PaginatorTest(unittest.TestCase):

    # Test a generation of paginator:
    def test_generate_page(self):
        for page in generated_pages:
            self.assertEqual(page["result"].create_paginator(), page["expected"])

    # Test a generation of html:
    def test_generate_html(self):
        for html in generated_html:
            self.assertEqual(str(html["result"]).replace("\t", "").replace("\n", ""), html["expected"])
            
    # Test a length of paginator:
    def test_length(self):
      for count_pages in range(1,100):
        for max_pages in range(3,count_pages+1):
          for current_page in range(1,count_pages+1):
            paginator = Paginator(current_page=current_page, count_pages=count_pages, pattern_url="/page{{number}}/", max_pages = max_pages)
            pages = paginator.create_paginator()
            count = 0
            for page in pages:
              if page["link"] is not None:
                count += 1
            self.assertEqual(count, max_pages)

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

