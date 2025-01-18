from elem import Elem


class Html(Elem):
    def __init__(self, content=None, attributes=None):
        super().__init__(tag="html", content=content, attr=attributes)


class Head(Elem):
    def __init__(self, content=None, attributes=None):
        super().__init__(tag="head", content=content, attr=attributes)


class Body(Elem):
    def __init__(self, content=None, attributes=None):
        super().__init__(tag="body", content=content, attr=attributes)


class Title(Elem):
    def __init__(self, content=None, attributes=None):
        super().__init__(tag="title", content=content, attr=attributes)


class Meta(Elem):
    def __init__(self, attributes=None):
        super().__init__(
            tag="meta", content=None, attr=attributes, tag_type="simple"
        )


class Img(Elem):
    def __init__(self, attributes=None):
        super().__init__(
            tag="img", content=None, attr=attributes, tag_type="simple"
        )


class Table(Elem):
    def __init__(self, content=None, attributes=None):
        super().__init__(tag="table", content=content, attr=attributes)


class Th(Elem):
    def __init__(self, content=None, attributes=None):
        super().__init__(tag="th", content=content, attr=attributes)


class Tr(Elem):
    def __init__(self, content=None, attributes=None):
        super().__init__(tag="tr", content=content, attr=attributes)


class Td(Elem):
    def __init__(self, content=None, attributes=None):
        super().__init__(tag="td", content=content, attr=attributes)


class Ul(Elem):
    def __init__(self, content=None, attributes=None):
        super().__init__(tag="ul", content=content, attr=attributes)


class Ol(Elem):
    def __init__(self, content=None, attributes=None):
        super().__init__(tag="ol", content=content, attr=attributes)


class Li(Elem):
    def __init__(self, content=None, attributes=None):
        super().__init__(tag="li", content=content, attr=attributes)


class H1(Elem):
    def __init__(self, content=None, attributes=None):
        super().__init__(tag="h1", content=content, attr=attributes)


class H2(Elem):
    def __init__(self, content=None, attributes=None):
        super().__init__(tag="h2", content=content, attr=attributes)


class P(Elem):
    def __init__(self, content=None, attributes=None):
        super().__init__(tag="p", content=content, attr=attributes)


class Div(Elem):
    def __init__(self, content=None, attributes=None):
        super().__init__(tag="div", content=content, attr=attributes)


class Span(Elem):
    def __init__(self, content=None, attributes=None):
        super().__init__(tag="span", content=content, attr=attributes)


class Hr(Elem):
    def __init__(self, attributes=None):
        super().__init__(
            tag="hr", content=None, attr=attributes, tag_type="simple"
        )


class Br(Elem):
    def __init__(self, attributes=None):
        super().__init__(
            tag="br", content=None, attr=attributes, tag_type="simple"
        )
