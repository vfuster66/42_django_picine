from elements import Html, Head, Body, Title, H1, Img, Table, Tr, Th, Td
from elem import Text


def main():
    # Réplication de la structure HTML de l'exercice précédent
    html = Html([
        Head(Title(Text("Hello ground!"))),
        Body([
            H1(Text("Oh no, not again!")),
            Img(attributes={"src": "http://i.imgur.com/pfp3T.jpg"})
        ])
    ])

    print(html)

    # Tests supplémentaires
    print("\nTests supplémentaires :")
    table = Html([
        Body([
            Table([
                Tr([Th(Text("Header 1")), Th(Text("Header 2"))]),
                Tr([Td(Text("Data 1")), Td(Text("Data 2"))])
            ])
        ])
    ])
    print(table)


if __name__ == "__main__":
    main()
