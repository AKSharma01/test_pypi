from app import my

urls = [
    ('/', ['GET'], my.as_view=my('my'))
]
