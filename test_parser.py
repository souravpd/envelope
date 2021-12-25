import unittest

from parser import parse


class TestParser(unittest.TestCase):

    def test_tokenize(self):
        test_input = """
        layout:post;
        title:Two Sum Problem in LeetCode;
        slug:two-sum;
        heading:Two Sum;
        para:This is an [bold(implementation)] of the popular [link(leetcode.com/problems/two-sum Two-Sum)] Problem in LeetCode;
        subheading:Explanation of the Code;
        image:[path(backgorund.png This is the alternate text)];
        list:This is a list item,This is another list item;
        task-list:[False(This is the task)],[True(This is another task)];
        para:This is some [highlight(random explanation)] for the code that has been written for more information;
        """
        test_answer = [['layout', 'post'], ['title', 'Two Sum Problem in LeetCode'], ['slug', 'two-sum'], ['heading', 'Two Sum'], ['para', 'This is an [bold(implementation)] of the popular [link(leetcode.com/problems/two-sum Two-Sum)] Problem in LeetCode'], ['subheading', 'Explanation of the Code'], [
            'image', '[path(backgorund.png This is the alternate text)]'], ['list', 'This is a list item,This is another list item'], ['task-list', '[False(This is the task)],[True(This is another task)]'], ['para', 'This is some [highlight(random explanation)] for the code that has been written for more information']]
            
        self.assertListEqual(parse(test_input), test_answer,
                             "There is an error in the tokenizer")


if __name__ == "__main__":
    unittest.main()
