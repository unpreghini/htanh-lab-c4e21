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


def get_shapes():
    return shapes


def generate_quiz():
    text = choice([shape['text'].upper() for shape in shapes])
    color = choice([shape['color'] for shape in shapes])
    quiz_type = randint(0, 1)
    return [
                text,
                color,
                quiz_type  # randint(0, 1) # 0 : meaning, 1: color
            ]


def mouse_press(x, y, text, color, quiz_type):
    point = [x, y]
    text = text.lower()
    if quiz_type == 0:
        rect = [shape['rect'] for shape in shapes if shape['text'] == text][0]
    else:
        rect = [shape['rect'] for shape in shapes if shape['color'] == color][0]

    if is_inside(point, rect):
        return True
    else:
        return False
