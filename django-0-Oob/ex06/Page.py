from elem import Elem, Text
from elements import (
    Html, Head, Body, Title, H1, H2, P, Div, Span, Ul, Ol, Li,
    Table, Tr, Th, Td, Img, Meta, Br, Hr
)


class Page:
    def __init__(self, root):
        if not isinstance(root, Elem):
            raise TypeError("Root must be an instance of Elem or a subclass.")
        self.root = root

    def is_valid(self):
        """Validate the entire HTML structure."""
        return self.__validate(self.root)

    def __validate(self, elem):
        """Recursive validation for each element."""
        if isinstance(elem, Text):
            return True

        # Validate allowed tag types
        if not isinstance(elem, (
            Html, Head, Body, Title, Meta, Img, Table, Th, Tr, Td, Ul, Ol, Li,
            H1, H2, P, Div, Span, Hr, Br
        )):
            return False

        # Specific rules for each tag type
        if isinstance(elem, Html):
            return (
                len(elem.content) == 2
                and isinstance(elem.content[0], Head)
                and isinstance(elem.content[1], Body)
                and all(self.__validate(child) for child in elem.content)
            )
        if isinstance(elem, Head):
            titles = [
                child for child in elem.content if isinstance(child, Title)
            ]
            return (
                1 <= len(titles) <= 1
                and all(self.__validate(child) for child in elem.content)
            )
        if isinstance(elem, (Body, Div)):
            return all(
                isinstance(child, (H1, H2, Div, Table, Ul, Ol, Span, Text, P,
                                   Img))
                and self.__validate(child)
                for child in elem.content
            )
        if isinstance(elem, (Title, H1, H2, Li, Th, Td)):
            return all(
                isinstance(child, (Text, str)) for child in elem.content
            )
        if isinstance(elem, P):
            return all(
                isinstance(child, (Text, str)) for child in elem.content
            )
        if isinstance(elem, Span):
            return all(
                isinstance(child, (Text, str))
                for child in elem.content
            )
        if isinstance(elem, (Ul, Ol)):
            return all(
                isinstance(child, Li) and self.__validate(child)
                for child in elem.content
            )
        if isinstance(elem, Tr):
            if len(elem.content) == 0:
                return False
            tag_type = type(elem.content[0])
            return all(isinstance(child, tag_type) for child in elem.content)
        if isinstance(elem, Table):
            return all(
                isinstance(child, Tr) and self.__validate(child)
                for child in elem.content
            )

        return True

    def __str__(self):
        """Return the HTML document as a string."""
        doc_type = "<!DOCTYPE html>\n" if isinstance(self.root, Html) else ""
        return f"{doc_type}{self.root}"

    def write_to_file(self, file_name):
        """Write the HTML document to a file."""
        with open(file_name, "w") as file:
            file.write(str(self))
