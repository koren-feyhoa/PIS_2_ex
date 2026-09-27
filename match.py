import re

from Point import Line, Point, Circle

str=["Point(3.4, 5.5)","Line(Point(1.2, 3.4), Point(5, 6))","Circle(Point(5, 6), 7)"]

def list_str_to_list_obj(BigList:list):
    list_of_obj=list()
    pattern_for_point = r"Point\(\s*([-+]?\d*\.?\d+)\s*,\s*([-+]?\d*\.?\d+)\s*\)"
    for i in BigList:
        n=re.fullmatch(rf"Line\({pattern_for_point}, {pattern_for_point}\)", i)
        object=None
        if n:
            object=Line(Point(x=float(n[1]),y=float(n[2])),Point(x=float(n[3]),y=float(n[4])))
            list_of_obj.append(object)
            continue

        o=re.fullmatch(fr"Circle\({pattern_for_point}, \s*([-+]?\d*\.?\d+)\s*\)", i)
        if o:
            object=Circle(Point(x=float(o[1]),y=float(o[2])),float(o[3]))
            list_of_obj.append(object)
            continue

        m = re.fullmatch(pattern_for_point, i)
        if m:
            object=Point(x=float(m[1]),y=float(m[2]))
            list_of_obj.append(object)
            continue

        if object==None:
            print('string not right:', i)
    return list_of_obj



def list_obj_to_list_str(BigList:list):
    list_of_str=list()
    for i in BigList:
        if type(i) is Point:
            list_of_str.append(f"Point({i.x}, {i.y})")
        if type(i) is Circle:
            list_of_str.append(f"Circle(Point({i.point.x}, {i.point.y}), {i.z})")
        if type(i) is Line:
            list_of_str.append(f"Line(Point({i.point_1.x}, {i.point_1.y}), Point({i.point_2.x}, {i.point_2.y}))")
    return list_of_str



