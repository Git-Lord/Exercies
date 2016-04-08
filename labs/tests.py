import unittest
from tests_cases import generated_pages


class PaginatorTest(unittest.TestCase):

    # Test a generation of paginator:
    def test_generate_page(self):
        for page in generated_pages:
            self.assertEqual(page["result"].create_paginator(), page["expected"])


if __name__ == '__main__':
    unittest.main()

