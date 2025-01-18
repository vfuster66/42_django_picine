from elem import Elem


def main():
    try:
        # Generate the HTML structure
        html = Elem('html', content=[
            Elem('head', content=[
                Elem('title', content="\"Hello ground!\"")
            ]),
            Elem('body', content=[
                Elem('h1', content="\"Oh no, not again!\""),
                Elem(
                    'img',
                    attr={'src': 'http://i.imgur.com/pfp3T.jpg'},
                    tag_type='simple'
                )
            ])
        ])

        # Display the HTML structure
        print(html)

        print("\nTests successful.")
    except Exception as e:
        print(f"Test failed with error: {e}")


if __name__ == "__main__":
    main()
