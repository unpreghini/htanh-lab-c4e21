def is_inside(point, rectangle):
    [x_point, y_point] = point
    [x_rect, y_rect, width, height] = rectangle

    test_1 = x_rect <= x_point <= (x_rect + width)
    test_2 = y_rect <= y_point <= (y_rect + height)

    if test_1 and test_2:
        return True

    else:
        return False


# Code check

point = [200, 120]
rectangle = [140, 60, 100, 200]

if is_inside(point, rectangle):
    print('Your function is correct!')

else:
    print('Bugs detected!')
