"""
code_generator.py 
Sourav Prasad
A very basic implementation of a generator
A Generator takes the list of tokens and transforms it into HTML
"""


class CodeGenerator:
    def __init__(self, tokens):
        self.tokens = tokens
        self.title = ""
        self.slug = ""
        self.body = ""

    def handle_layout(self, text):
        pass

    def handle_title(self, text):
        self.title = text

    def handle_slug(self, text):
        self.slug = text

    def handle_heading(self, text):
        text = self.handle_modifiers(text)
        self.body = self.body + f"<h1>{text}</h1>"

    def handle_para(self, text):
        text = self.handle_modifiers(text)
        self.body = self.body + f"<p>{text}</p>"

    def handle_subheading(self, text):
        text = self.handle_modifiers(text)
        self.body = self.body + f"<h3>{text}</h3>"

    def handle_image(self, text):
        text = self.handle_modifiers(text)
        self.body = self.body + text

    def handle_list(self, text):
        list_items = text.split(",")
        self.body = self.body + "<ul>"
        for item in list_items:
            self.body = self.body + f"<li>{self.handle_modifiers(item)}</li>"
        self.body = self.body + "</ul>"

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

    def apply_modifier(self, modifier, text):
        if modifier == "bold":
            return f"<strong>{text}</strong>"
        elif modifier == "italic":
            return f"<em>{text}</em>"
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

    def result(self):
        for token in self.tokens:
            if token[0] == "layout":
                self.handle_layout(token[1])
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
            elif token[0] == "image":
                self.handle_image(token[1])
            elif token[0] == "list":
                self.handle_list(token[1])
            elif token[0] == "task-list":
                self.handle_task_list(token[1])
            else:
                print("Undefined Type")

        return self.body
