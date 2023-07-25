#!/usr/bin/env python3


class Shoe:
    def __init__(self, brand, size, condition="used"):
        self.brand = brand
        self.size = size
        self.condition = condition

    def cobble(self):
        self.condition = "New"
        print("Your shoe is as good as new!")

    def get_size(self):
        return self._size

    def set_page_count(self, size):
        if type(size) is int:
            self._size = size
        else:
            print("size must be an integer")

    size = property(get_size, set_page_count)
    pass
