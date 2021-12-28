import os
from transpiler import Transpiler

dirname = os.path.dirname(__file__)


def make_website():
    for dirpath, dirnames, files in os.walk('posts'):
        for file_name in files:
            text = ""
            with open(os.path.join(dirname, f'posts/{file_name}'), 'r') as reader:
                text = reader.read()
            T = Transpiler(text)
            category, title, slug, document = T.get_result()
            with open(os.path.join(dirname, f'dst/{slug}.html'), 'w') as writer:
                writer.write(document)


if __name__ == "__main__":
    make_website()
