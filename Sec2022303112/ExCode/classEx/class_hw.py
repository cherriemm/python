#!/usr/bin/python
# -*- coding: UTF-8 -*-
import math

# 题目八：计算图形面积及周长
class Shape():
    def __init__(self,name, area=0, perimeter = 0):
        self.name = name
        self.area = area
        self.perimeter = perimeter

    def cal_area(self):
        return self.area

    def cal_perimeter(self):
        return self.perimeter

    def display(self):
        print("名称是 " + self.name)
        print("面积是 " + str(self.area))
        print("周长是 " + str(self.perimeter))



class Rectangle(Shape):
    def __init__(self, name, length, width):
        super().__init__(name)
        self.length = length
        self.width = width

    def cal_area(self):
        area = self.length * self.width
        self.area = "%.2f" % area
        return self.area

    def cal_perimeter(self):
        perimeter  = (self.length + self.width) * 2
        self.perimeter = "%.2f" % perimeter
        return self.perimeter


class Triangle(Shape):
    def __init__(self, name, a, b, c):
        super().__init__(name)
        self.a = a
        self.b = b
        self.c = c

    def cal_perimeter(self):
        perimeter = self.a + self.b + self.c
        self.perimeter = "%.2f" % perimeter

    def cal_area(self):
        p = (self.a + self.b + self.c) / 2
        area = math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
        self.area = "%.2f" % area


class Circle(Shape):
    def __init__(self, name, r):
        super().__init__(self, name)
        self.name = name
        self.r = r

    def cal_perimeter(self):
        perimeter = 2 * 3.14 * self.r
        self.perimeter = "%.2f" % perimeter

    def cal_area(self):
        area = 3.14 * self.r ** 2
        self.area = "%.2f" % area


if __name__ == '__main__':
    rect = Rectangle("rect",2,3)
    tri = Triangle("tri",3,4,5)
    c = Circle("c",5)
    rect.cal_area()
    rect.cal_perimeter()
    tri.cal_area()
    tri.cal_perimeter()
    c.cal_area()
    c.cal_perimeter()
    rect.display()
    tri.display()
    c.display()