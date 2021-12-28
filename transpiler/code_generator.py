"""
code_generator.py 
Sourav Prasad
A very basic implementation of a generator to generate the body of each post
A Generator takes the list of tokens and transforms it into HTML
"""


class CodeGenerator:
    # Constructor takes in the array of tokens returned by the parser.parse
    def __init__(self, tokens):
        self.tokens = tokens
        # title of the document
        self.title = ""
        # slug for the links
        self.slug = ""
        # body of the entire html document
        self.body = ""
        # Category under which this post appears
        self.category = ""
        # navigation data
        """
        Heading
        1. SubHeading
            1.1 SubSubheading
            1.2 SubSubheading
            1.3 SubSubheading
        2. SubHeading
            2.1 SubSubHeading

        Representation
        [(subheading_id , subheading , [(subsubheading_id) , (subsubheading) , (subsubheading_id , subsubheading)])]
        """
        self.navigation = []
        self.subheading_id = 0
        self.subsubheading_id = 0

    def handle_category(self, text):
        self.category = text

    # store the title of the page
    def handle_title(self, text):
        self.title = text

    # store the slug for the page
    def handle_slug(self, text):
        self.slug = text

    # generate the heading
    def handle_heading(self, text):
        # handle the nested modifiers
        text = self.handle_modifiers(text)
        self.body = self.body + f"<h1>{text}</h1>"

    # generate the paragraphs
    def handle_para(self, text):
        # handle the nested modifiers
        text = self.handle_modifiers(text)
        self.body = self.body + f"<p>{text}</p>"

    # generate the subheadings
    def handle_subheading(self, text):
        # handle the nested modifiers
        text = self.handle_modifiers(text)
        # Generate Navigation Data
        self.navigation.append((self.subheading_id , text , []))
        self.subsubheading_id = 0
        self.body = self.body + f"<h3 id='{self.subheading_id}'>{text}</h3>"
        self.subheading_id = self.subheading_id + 1

     # generate the subsubheadings
    def handle_subsubheading(self, text):
        # handle the nested modifiers
        text = self.handle_modifiers(text)
        # Generate Navigation Data
        self.navigation[self.subheading_id-1][2].append((self.subsubheading_id , text))
        self.body = self.body + f"<h5 id='{self.subheading_id-1}.{self.subsubheading_id}'>{text}</h5>"
        self.subsubheading_id = self.subsubheading_id + 1

    # generate the images
    def handle_image(self, text):
        # handle the src and figcaption
        text = self.handle_modifiers(text)
        self.body = self.body + text

    # generate the list
    def handle_list(self, text):
        list_items = text.split(",")
        self.body = self.body + "<ul>"
        for item in list_items:
            self.body = self.body + f"<li>{self.handle_modifiers(item)}</li>"
        self.body = self.body + "</ul>"

    # generates checkboxes
    def handle_task_list(self, text):
        list_items = text.split(",")
        self.body = self.body + "<form>"
        for item in list_items:
            self.body = self.body + f"{self.handle_modifiers(item)}"
        self.body = self.body + "</form>"

    # handle "This is some [@bold(@italic(bold and italized))] text" "This is some <b><em> Bold and Italized</em></b>"
    # handle "This is some [@bold(bold and @italic(italized))] text" "This is some <b>Bold and <em>Italized</em></b>"

    """
    Current Modifier List
    - bold
    - italic
    - highlight
    - image
    - link
    - Task-List
        - True
        - False
    """

    # applies the modifier
    def apply_modifier(self, modifier, text):
        if modifier == "bold":
            return f"<b>{text}</b>"
        elif modifier == "italic":
            return f"<i>{text}</i>"
        elif modifier == "highlight":
            return f"<mark>{text}</mark>"
        elif modifier == "image":
            pos = text.index(" ")
            path = text[:pos]
            caption = text[pos+1:]
            return f"<figure><img src='{path}' alt='{caption}'><figcaption>{caption}</figcaption></figure>"
        elif modifier == "link":
            pos = text.index(" ")
            path = text[:pos]
            caption = text[pos+1:]
            return f"<a href='https://{path}'>{caption}</a>"
        elif modifier == "True":
            return f"<input type='checkbox' name='{text}' id='{text}' checked> {text}"
        elif modifier == "False":
            return f"<input type='checkbox' name='{text}' id='{text}'> {text}"

    # Recursive function to loop over the text and apply the modifiers
    # Base Case -> The string is over
    # text[i] == '@' -> Store the modifier and the reduce the indices of the enclosing brackets
    # else -> store the text
    def modify(self, text, i, j):
        if i > j:
            return ""
        if text[i] == '@':
            modifier = ""
            i = i+1
            while text[i] != '(':
                modifier = modifier + text[i]
                i = i + 1
            return self.apply_modifier(modifier, self.modify(text, i+1, j-1))
        else:
            return text[i] + self.modify(text, i + 1, j)

    # Function to identify the [] and send the data within them for further processing
    def handle_modifiers(self, text):
        final_text = ""
        cursor = 0
        while cursor < len(text):
            character = text[cursor]
            if character != '[':
                final_text = final_text + character
                cursor = cursor + 1
            else:
                cursor = cursor + 1
                text_to_modify = ""
                while text[cursor] != ']':
                    text_to_modify = text_to_modify + text[cursor]
                    cursor = cursor + 1
                modified_text = self.modify(
                    text_to_modify, 0, len(text_to_modify)-1)
                final_text = final_text + modified_text
                cursor = cursor + 1
        return final_text


    # Handle Internal Navigation
    def handle_internal_navigation(self):
        data = f"<details><summary>Internal Navigation for {self.title}</summary><ol>"
        for id,name,sections in self.navigation:
            data = data + f"<a href='#{id}'><li>{name}</li></a>"
            if len(sections) != 0:
                data = data + "<ol>"
                for sub_id , sub_name in sections:
                    data = data + f"<a href='#{id}.{sub_id}'><li>{sub_name}</li></a>"
                data = data + "</ol>"
        data = data + "</ol></details>"
        self.body = data + self.body
    
    # This is the entry point of this generator
    # We loop over the tokens array and generate the html elements depending upon the type
    def get_body(self):
        for token in self.tokens:
            # token[0] is the type
            # token[1] is the value
            if token[0] == "category":
                self.handle_category(token[1])
            elif token[0] == "title":
                self.handle_title(token[1])
            elif token[0] == "slug":
                self.handle_slug(token[1])
            elif token[0] == "heading":
                self.handle_heading(token[1])
            elif token[0] == "para":
                self.handle_para(token[1])
            elif token[0] == "subheading":
                self.handle_subheading(token[1])
            elif token[0] == "subsubheading":
                self.handle_subsubheading(token[1])
            elif token[0] == "image":
                self.handle_image(token[1])
            elif token[0] == "list":
                self.handle_list(token[1])
            elif token[0] == "task-list":
                self.handle_task_list(token[1])
            else:
                print("Undefined Type")

        # now the body has been generated next we need to add the head section and the headers and footers
        # Add the navigation
        self.handle_internal_navigation()
        return (self.category, self.title, self.slug, self.body)
