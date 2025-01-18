class Text(str):
    """
    A class that represents text content for HTML elements.
    Validates that the text is a valid string for HTML content.
    """

    def __str__(self):
        return (super().__str__()
                .replace("<", "&lt;")
                .replace(">", "&gt;")
                .replace('"', "&quot;")
                .replace("&", "&amp;"))


class Elem:
    """A class that represents an HTML element."""

    class ValidationError(Exception):
        """Exception raised when the content is invalid for an Elem."""
        def __init__(self, message="Invalid content"):
            super().__init__(message)

    def __init__(self, tag='div', attr=None, content=None, tag_type='double'):
        """
        Initializes an HTML element.
        :param tag: Name of the HTML tag.
        :param attr: Dictionary of HTML attributes.
        :param content: Content inside the HTML element.
        :param tag_type: Type of tag ('double' or 'simple').
        """
        if attr is None:
            attr = {}
        if content is None:
            content = []
        elif not isinstance(content, list):
            content = [content]

        self.tag = tag
        self.attr = attr
        self.content = []
        self.tag_type = tag_type
        self.add_content(content)

    def __str__(self):
        """
        Returns the HTML representation of the element.
        """
        attr = self.__make_attr()
        if self.tag_type == 'simple':
            return f"<{self.tag}{attr} />"
        content = self.__make_content()
        return f"<{self.tag}{attr}>{content}</{self.tag}>"

    def __make_attr(self):
        """
        Converts attributes dictionary to HTML string.
        """
        if not self.attr:
            return ''
        return ' ' + ' '.join(
            f'{key}="{value}"' for key, value in self.attr.items()
        )

    def __make_content(self):
        """
        Converts content list to HTML string.
        """
        if not self.content:
            return ''
        return '\n'.join(str(elem) for elem in self.content)

    def add_content(self, content):
        """
        Adds content to the element.
        :param content: A string or list of Elem instances.
        """
        if isinstance(content, list):
            for elem in content:
                if not self.__is_valid_content(elem):
                    raise Elem.ValidationError("Invalid content type")
                self.content.append(elem)
        elif self.__is_valid_content(content):
            self.content.append(content)
        else:
            raise Elem.ValidationError("Invalid content type")

    @staticmethod
    def __is_valid_content(content):
        """
        Validates content type (string or Elem instance).
        """
        return isinstance(content, (Elem, Text, str))
