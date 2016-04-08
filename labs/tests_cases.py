from main import Paginator

generated_pages = [
    {
        "result": Paginator(current_page=4, count_pages=10, pattern_url="/page{{number}}/", max_pages=5),
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
        "result": Paginator(current_page=1, count_pages=10, pattern_url="/page{{number}}/", max_pages=5),
        "expected": [
            {"number": 1, "link": "/page1/", "active": True},
            {"number": 2, "link": "/page2/", "active": False},
            {"number": "...", "link": None, "active": False},
            {"number": 10, "link": "/page10/", "active": False},
        ]
    },
    {
        "result": Paginator(current_page=10, count_pages=10, pattern_url="/page{{number}}/", max_pages=5),
        "expected": [
            {"number": 1, "link": "/page1/", "active": False},
            {"number": "...", "link": None, "active": False},
            {"number": 9, "link": "/page9/", "active": False},
            {"number": 10, "link": "/page10/", "active": True},
        ]
    },
    {
        "result": Paginator(current_page=2, count_pages=10, pattern_url="/page{{number}}/", max_pages=5),
        "expected": [
            {"number": 1, "link": "/page1/", "active": False},
            {"number": 2, "link": "/page2/", "active": True},
            {"number": 3, "link": "/page3/", "active": False},
            {"number": "...", "link": None, "active": False},
            {"number": 10, "link": "/page10/", "active": False},
        ]
    },
    {
        "result": Paginator(current_page=3, count_pages=5, pattern_url="/page{{number}}/", max_pages=5),
        "expected": [
            {"number": 1, "link": "/page1/", "active": False},
            {"number": 2, "link": "/page2/", "active": False},
            {"number": 3, "link": "/page3/", "active": True},
            {"number": 4, "link": "/page4/", "active": False},
            {"number": 5, "link": "/page5/", "active": False},
        ]
    },
]
