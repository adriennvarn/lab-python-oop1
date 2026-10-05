#!/usr/bin/env python3

class Coffee:
    def __init__(self, size, price):
        self._size = size
        self.price = price
    
    # initialize size as property to make sure it's valid
    def _get_size(self):
        return self._size
    def _set_size(self, value):
        if value.lower() in ["small", "medium", "large"]:
            self._size = value
        else:
            print("size must be Small, Medium, or Large")
    size = property(_get_size, _set_size)
    
    def tip(self):
        print("This coffee is great, here’s a tip!")
        self.price += 1