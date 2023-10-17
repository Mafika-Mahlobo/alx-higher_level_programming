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

    @property
    def size(self):
        """getter for size attribute"""
        return self.width

    @size.setter
    def size(self, size):
        """setter for size attribute"""
        self.width = size

    def update(self, *args, **kwargs):
        """ovweridig update method from parent class - rectangle"""

        if args:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                if i == 1:
                    self.size = args[i]
                if i == 2:
                    self.x = args[i]
                if i == 3:
                    self.y = args[i]

        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """Overriding to_dictionary method from parent class - Rectangle"""
        return {
            "id": self.id,
            "x": self.x,
            "size": self.width,
            "y": self.y
        }
