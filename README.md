# Envelope
This is an implementation of a simple compiler for a templating engine for my Blog. It uses a JSON inspired syntax

### Grammar Rules
```python
"""
[
    layout:post,
    title: "Two Sum Problem in LeetCode",
    slug:"two-sum",
    heading:"Two Sum",
    body:
    [
        para:"This is an (bold:"implementation") of the popular (link: https://leetcode.com/problems/two-sum "Two-Sum") Problem in LeetCode",
        code:(
            def two_sum(self , nums , target):
                map = {}
                for index , num in enumerate(nums):
                    complement = target - nums
                    if map.get(complement , -1) != -1:
                        return [index , map.get(complement)]
                    map[num] = index
        ),
        subheading:"Explanation of the Code",
        image: backgorund.png "This is the alternate text", 
        list:[
            "This is a list item",
            "This is another list item",
        ],     
        task-list:[
            (done:False "This is the task"), 
            (done:True "This is the task")
        ],
        para: "This is some (highlight: "random explanation") for the code that has been written for more information you (image: "image.jpeg" "alternate-text")",
    ]
]
"""
```