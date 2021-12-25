# Envelope
Building a Templating Engine inspired by steve kinney's course on DropBear 

### What is a compiler?
Something that turns a higher-level language to a lower-language language
The stages of a compiler are
- Parsing: Take the source code and turn it into a repesentation of that code
- Transformation: Take the source code and transforms it to do whatever the compiler wants it to do.
- Generation: Take the transformed representation and turns it into a new string of code 


### Grammar Rules
```python
"""
layout:post;
title:Two Sum Problem in LeetCode;
slug:two-sum;
heading:Two Sum;
para:This is an [bold(implementation)] of the popular [link(https://leetcode.com/problems/two-sum Two-Sum)] Problem in LeetCode;
subheading:Explanation of the Code;
image:[path(backgorund.png This is the alternate text)];
list:This is a list item,This is another list item;
task-list:[False(This is the task)],[True(This is another task)];
para:This is some [highlight(random explanation)] for the code that has been written for more information;
"""
```