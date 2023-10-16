#!/usr/bin/python3

"""A module containig Square class that inherit from rectangle"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class the inherit from rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """instantiation of square class, calling the supper class"""

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns a customezed __str__ method string"""

        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
