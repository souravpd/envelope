from parser import parse

from code_generator import CodeGenerator


class Envelope:
    def __init__(self, text):
        self.text = text
        self.tokens = parse(text)
        self.cg = CodeGenerator(self.tokens)

    def get_html(self):
        return self.cg.get_document()


if __name__ == "__main__":
    test_input = """
        layout:post;
        title:Two Sum Problem in LeetCode;
        slug:two-sum;
        heading:Two Sum;
        para:This is an [@bold(implementation)] of the popular [@link(leetcode.com/problems/two-sum Two-Sum)] Problem in LeetCode;
        subheading:Explanation of the Code;
        image:[@image(backgorund.png This is the alternate text)];
        list:This is a list item,This is another list item;
        task-list:[@False(This is the task)],[@True(This is another task)];
        para:This is some [@highlight(random explanation)] for the code that has been written for more information;
        """
    ENV = Envelope(test_input)
    print(ENV.get_html())
