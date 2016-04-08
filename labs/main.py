#!/usr/local/bin/python
#
# -*- coding: utf-8 -*-

import math


class Paginator:
    """ The main class, that creates a paginator: """
    def __init__(self, current_page, count_pages, pattern_url="", max_pages=10):
        self.current_page = current_page
        self.count_pages = count_pages
        self.pattern_url = pattern_url
        self.max_pages = max_pages

    def generate_link(self, number):
        return self.pattern_url.replace("{{number}}", str(number))

    def previous_page(self):
        if self.current_page > 1:
            return self.current_page - 1
        else:
            return None

    def next_page(self):
        if self.current_page > self.count_pages:
            return None
        else:
            return self.current_page + 1

    def create_page(self, number):
        return {"number": number, "link": self.generate_link(number),
                "active": self.current_page == number}

    def create_divider(self):
        return {"number": "...", "link": None, "active": False}

    def create_paginator(self):
        """ Generates an array of pages like the following an array:
        [
            {"number": 1, "link": "/page1/", "active": False},
            {"number": "...", "link": None, "active": False},
            {"number": 3, "link": "/page3/", "active": False},
            {"number": 4, "link": "/page4/", "active": True},
            {"number": 5, "link": "/page5/", "active": False},
            {"number": "...", "link": None, "active": False},
            {"number": 10, "link": "/page10/", "active": False}
        ]
         """
        result = []
        neighbours_length = math.floor((self.max_pages - 2) / 2.0)
        start_neighbours = max(self.current_page - neighbours_length, 1)
        end_neighbours = min(self.current_page + neighbours_length, self.count_pages)
        if self.count_pages > 0:
            if start_neighbours != 1:
                result.append(self.create_page(1))
            if start_neighbours > 2:
                result.append(self.create_divider())
            for i in range(start_neighbours, end_neighbours+1):
                result.append(self.create_page(i))
            if end_neighbours < self.count_pages - 1:
                result.append(self.create_divider())
            if end_neighbours != self.count_pages:
                result.append(self.create_page(self.count_pages))
        return result