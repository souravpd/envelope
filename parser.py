"""
parser.py 
Sourav Prasad
A very basic implementation of a parser
A Parser breaks a long input code into individual tokens
"""

# Import Library to do Regular Expression matching
import re


class Parser:
    # takes in an input string and returns an array of tokens
    def parse(self, input):
        # remove the trailing whitespaces
        input = input.strip()
        # replace all newlines
        input = re.sub(r"[\n]*", "", input)
        # split the input string by semicolons
        input = input.split(";")
        # remove the last empty list object
        input = input[:len(input)-1]
        # declare an empty list of tokens to be returned
        tokens = []
        # loop thorugh each line of input
        for line in input:
            # split each line by colon
            components = line.split(":")
            # make a token list for that perticular line
            token = []
            # list comprehension to add the components of the line to token
            [token.append(component.strip()) for component in components]
            # append this token to tokens
            tokens.append(token)

        # return the tokens
        return tokens
