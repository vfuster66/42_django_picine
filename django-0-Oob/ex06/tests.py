from elements import (
    Html, Head, Body, Title, H1, P, Div, Ul, Li, Img, Tr, Th, Td, Table, Br,
    Meta,
)
from Page import Page
from elem import Text


def run_tests():
    print("\n--- Tests supplémentaires ---\n")

    # Test 1: Structure complète et valide
    html_valid = Html([
        Head([
            Meta(attributes={"charset": "utf-8"}),
            Title(Text("Hello ground!"))
        ]),
        Body([
            H1(Text("Oh no, not again!")),
            Img(attributes={"src": "http://i.imgur.com/pfp3T.jpg"}),
            Div([
                P(Text("Some text here.")),
                Table([
                    Tr([Th(Text("Header 1")), Th(Text("Header 2"))]),
                    Tr([Td(Text("Data 1")), Td(Text("Data 2"))])
                ])
            ]),
            Ul([Li(Text("Item 1")), Li(Text("Item 2"))])
        ])
    ])
    page_valid = Page(html_valid)
    print("Test 1 - Structure valide :", page_valid.is_valid())

    # Test 2: Body avec un élément invalide
    html_invalid_body = Html([
        Head(Title(Text("Hello ground!"))),
        Body([
            H1(Text("Invalid content")),
            Br()  # Élément invalide dans Body
        ])
    ])
    page_invalid_body = Page(html_invalid_body)
    print("Test 2 - Body avec élément invalide :",
          page_invalid_body.is_valid())

    # Test 3: Head sans Title
    html_no_title = Html([
        Head([Meta(attributes={"charset": "utf-8"})]),
        Body([H1(Text("Valid content"))])
    ])
    page_no_title = Page(html_no_title)
    print("Test 3 - Head sans Title :", page_no_title.is_valid())

    # Test 4: Title contenant autre chose qu'un Text
    html_invalid_title = Html([
        Head(Title(H1(Text("Nested header")))),
        Body([H1(Text("Valid content"))])
    ])
    page_invalid_title = Page(html_invalid_title)
    print("Test 4 - Title avec contenu invalide :",
          page_invalid_title.is_valid())

    # Test 5: Div contenant des éléments valides
    html_valid_div = Html([
        Head(Title(Text("Hello ground!"))),
        Body([
            Div([H1(Text("Valid Header")), P(Text("Valid paragraph"))])
        ])
    ])
    page_valid_div = Page(html_valid_div)
    print("Test 5 - Div avec éléments valides :", page_valid_div.is_valid())

    # Test 6: Ul avec éléments invalides
    html_invalid_ul = Html([
        Head(Title(Text("Hello ground!"))),
        Body([
            Ul([Li(Text("Valid item")), H1(Text("Invalid item"))])
        ])
    ])
    page_invalid_ul = Page(html_invalid_ul)
    print("Test 6 - Ul avec éléments invalides :", page_invalid_ul.is_valid())

    # Test 7: Table avec Tr invalide
    html_invalid_table = Html([
        Head(Title(Text("Hello ground!"))),
        Body([
            Table([
                Tr([Th(Text("Header 1")), Td(Text("Invalid mix"))]),
                Tr([Td(Text("Data 1")), Td(Text("Data 2"))])
            ])
        ])
    ])
    page_invalid_table = Page(html_invalid_table)
    print("Test 7 - Table avec Tr invalide :", page_invalid_table.is_valid())

    # Test 8: P avec contenu invalide
    html_invalid_p = Html([
        Head(Title(Text("Hello ground!"))),
        Body([
            P([Text("Valid text"), H1(Text("Invalid header"))])
        ])
    ])
    page_invalid_p = Page(html_invalid_p)
    print("Test 8 - P avec contenu invalide :", page_invalid_p.is_valid())

    # Test 9: Écriture dans un fichier
    page_valid.write_to_file("valid_output.html")
    print("Test 9 - Fichier écrit : valid_output.html")

    print("\n--- Tests terminés ---\n")


if __name__ == "__main__":
    run_tests()
