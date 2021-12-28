# The Transpiler Generates the body of each Post
from code_generator import CodeGenerator
from parser import Parser


class Transpiler:
    def __init__(self, text):
        self.text = text
        self.p = Parser()
        self.tokens = self.p.parse(self.text)
        self.cg = CodeGenerator(self.tokens)

    def get_result(self):
        return self.cg.get_document()
