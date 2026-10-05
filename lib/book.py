#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
        self.title = title
        self._page_count = page_count
        
    #  Sets up page count as property to ensure non 0 int
    def _get_page_count(self):
        return self._page_count
    def _set_page_count(self, value):
        if type(value) is int and value > 0:
            self._page_count = value
        else:
            print("page_count must be an integer")
    page_count = property(_get_page_count, _set_page_count)
    
    def turn_page(self):
        print("Flipping the page...wow, you read fast!")