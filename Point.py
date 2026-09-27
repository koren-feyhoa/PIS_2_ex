from dataclasses import dataclass


@dataclass
class Point:
    x:float
    y:float

@dataclass
class Circle:
    point:Point
    z:float

@dataclass
class Line:
    point_1: Point
    point_2: Point