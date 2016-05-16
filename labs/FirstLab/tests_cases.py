# -*- coding: utf-8 -*-

from main import Paginator

generated_examples = [
    Paginator(current_page=4, count_pages=10, pattern_url="/page{{number}}/", max_pages = 5),
    Paginator(current_page=10, count_pages=10, pattern_url="/page{{number}}/", max_pages = 3),
    Paginator(current_page=4, count_pages=10, pattern_url="/page{{number}}/", max_pages = 6),
    Paginator(current_page=1, max_pages = 10, count_pages=4, pattern_url="/page_{{number}}/"),
    Paginator(current_page=8, max_pages = 5, count_pages=8, pattern_url="/page_{{number}}/"),
    Paginator(current_page=41, max_pages = 10, count_pages=50, pattern_url="/page_{{number}}/"),
    Paginator(current_page=42, max_pages = 10, count_pages=50, pattern_url="/page_{{number}}/"),
    Paginator(current_page=500, max_pages = 10, count_pages=500, pattern_url="/page_{{number}}/"),
    Paginator(current_page=1, max_pages = 10, count_pages=50, pattern_url="/page_{{number}}/"),
    Paginator(current_page=2, max_pages = 10, count_pages=50, pattern_url="/page_{{number}}/"),
    Paginator(current_page=3, max_pages = 10, count_pages=50, pattern_url="/page_{{number}}/"),
    Paginator(current_page=7, max_pages = 10, count_pages=50, pattern_url="/page_{{number}}/"),
    Paginator(current_page=8, max_pages = 10, count_pages=50, pattern_url="/page_{{number}}/"),
    Paginator(current_page=9, max_pages = 10, count_pages=50, pattern_url="/page_{{number}}/"),
    Paginator(current_page=4, max_pages = 10, count_pages=50, pattern_url="/page_{{number}}/"),
    Paginator(current_page=45, max_pages = 10, count_pages=50, pattern_url="/page_{{number}}/"),
    Paginator(current_page=46, max_pages = 10, count_pages=50, pattern_url="/page_{{number}}/"),
    Paginator(current_page=47, max_pages = 10, count_pages=50, pattern_url="/page_{{number}}/"),
    Paginator(current_page=48, max_pages = 10, count_pages=50, pattern_url="/page_{{number}}/"),
    Paginator(current_page=49, max_pages = 10, count_pages=50, pattern_url="/page_{{number}}/"),
    Paginator(current_page=50, max_pages = 10, count_pages=50, pattern_url="/page_{{number}}/")
]

generated_html = [
    {
        "result": Paginator(current_page=4, count_pages=10, pattern_url="/page{{number}}/", max_pages = 5),
        "expected": '<ul class = "pagination">'
                    '<li><a href="/page3/">←</a></li>'
                    '<li><a href="/page1/">1</a></li>'
                    '<li class="disabled"><a href="#">...</a></li>'
                    '<li><a href="/page3/">3</a></li>'
                    '<li class="active"><a href="/page4/">4</a></li>'
                    '<li><a href="/page5/">5</a></li>'
                    '<li class="disabled"><a href="#">...</a></li>'
                    '<li><a href="/page10/">10</a></li>'
                    '<li><a href="/page5/">→</a></li>'
                    '</ul> '
    }
]

generated_pages = [
    {
        "result": Paginator(current_page=4, count_pages=10, pattern_url="/page{{number}}/", max_pages = 5),
        "expected":
        [
            {"number": 1, "link": "/page1/", "active": False},
            {"number": "...", "link": None, "active": False},
            {"number": 3, "link": "/page3/", "active": False},
            {"number": 4, "link": "/page4/", "active": True},
            {"number": 5, "link": "/page5/", "active": False},
            {"number": "...", "link": None, "active": False},
            {"number": 10, "link": "/page10/", "active": False}
        ]
    },
    {
        "result": Paginator(current_page=1, count_pages=10, pattern_url="/page{{number}}/", max_pages = 3),
        "expected": [
            {"number": 1, "link": "/page1/", "active": True},
            {"number": 2, "link": "/page2/", "active": False},
            {"number": "...", "link": None, "active": False},
            {"number": 10, "link": "/page10/", "active": False},
        ]
    },
    {
        "result": Paginator(current_page=10, count_pages=10, pattern_url="/page{{number}}/", max_pages = 3),
        "expected": [
            {"number": 1, "link": "/page1/", "active": False},
            {"number": "...", "link": None, "active": False},
            {"number": 9, "link": "/page9/", "active": False},
            {"number": 10, "link": "/page10/", "active": True},
        ]
    },
    {
        "result": Paginator(current_page=2, count_pages=10, pattern_url="/page{{number}}/", max_pages = 4),
        "expected": [
            {"number": 1, "link": "/page1/", "active": False},
            {"number": 2, "link": "/page2/", "active": True},
            {"number": 3, "link": "/page3/", "active": False},
            {"number": "...", "link": None, "active": False},
            {"number": 10, "link": "/page10/", "active": False},
        ]
    },
    {
        "result": Paginator(current_page=3, count_pages=5, pattern_url="/page{{number}}/", max_pages = 5),
        "expected": [
            {"number": 1, "link": "/page1/", "active": False},
            {"number": 2, "link": "/page2/", "active": False},
            {"number": 3, "link": "/page3/", "active": True},
            {"number": 4, "link": "/page4/", "active": False},
            {"number": 5, "link": "/page5/", "active": False},
        ]
    },
]
