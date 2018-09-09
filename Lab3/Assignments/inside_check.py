def is_inside(point, rectangle):
    x_point = point[0]
    y_point = point[1]
    x_rect = rectangle[0]
    y_rect = rectangle[1]
    width = rectangle[2]
    height = rectangle[3]
    x_rect_1 = x_rect + width
    y_rect_1 = y_rect + height

    flag_1 = abs(x_point - x_rect)
    flag_2 = abs(x_point - x_rect_1)
    flag_3 = abs(y_point - y_rect)
    flag_4 = abs(y_point - y_rect_1)

    if flag_1 + flag_2 == width and flag_3 + flag_4 == height:
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
