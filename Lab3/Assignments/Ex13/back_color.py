from random import randint, choice
from inside_check import is_inside

shapes = [
    {
        'text': 'blue',
        'color': '#3F51B5',
        'rect': [20, 60, 100, 100]
    },
    {
        'text': 'red',
        'color': '#C62828',
        'rect': [140, 60, 100, 100]
    },
    {
        'text': 'yellow',
        'color': '#FFD600',
        'rect': [20, 180, 100, 100]
    },
    {
        'text': 'green',
        'color': '#4CAF50',
        'rect': [140, 180, 100, 100]
    }
]

names = []
colors = []
for shape in shapes:
    shape_name = shape['text'].upper()
    shape_color = shape['color']
    names.append(shape_name)
    colors.append(shape_color)


def get_shapes():
    return shapes


def generate_quiz():
    name = choice(names)
    color = choice(colors)
    quiz_type = randint(0, 1)
    return [
                name,
                color,
                quiz_type  # randint(0, 1) # 0 : meaning, 1: color
            ]


def mouse_press(x, y, name, color, quiz_type):
    point = [x, y]

    if quiz_type == 0:
        name_ = names.index(name)
        rectangle = shapes[name_]['rect']

    else:
        color_ = colors.index(color)
        rectangle = shapes[color_]['rect']
    result = is_inside(point, rectangle)
    return result
