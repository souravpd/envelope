from code_generator import CodeGenerator
from parser import Parser

# The Transpiler Generates the body of each Post
class Transpiler:
    def __init__(self , text):
        self.text = text
        self.p = Parser()
        self.tokens = self.p.parse(self.text)
        self.cg = CodeGenerator(self.tokens)
    
    def get_result(self):
        return self.cg.get_body()

if __name__ == "__main__":
    text = """
    category:Mineral-Engineering;
    title:What is Mineral Engineering;
    slug:Mineral-Engineering-introduction;
    heading:What is [@highlight(@bold(Mineral Engineering?))];
    subheading:What is a Mineral?;
    para:A Mineral is an [@highlight(@bold(naturally occuring inorganic substance having fixed chemical composition and structure))];
    subheading:What is Mineral Engineering?;
    para:Mineral Engineering refers to the process of benefication of the ore using physical means to improve the grade of the ore;
    subsubheading: Why is Mineral Engineering Required?;
    list:To make the ore ready for subsequent metallurgical operation, To reduce [@italic(Handling)] costs;
    subheading:What are the mineral Engineering unit operations?;
    subsubheading:Comminution;
    para:Size Reduction;
    subsubheading:Classification;
    para:Size Separation;
    subsubheading:Benefication;
    para:Quality Improvement;
    subsubheading:Dewatering;
    para:Moisture Removal;
    """

    t = Transpiler(text)
    print(t.get_result())