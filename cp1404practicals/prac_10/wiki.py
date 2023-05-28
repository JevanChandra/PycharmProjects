import wikipedia


def main():
    keyword = input("Search something in wikipedia: ")
    while keyword != "":
        try:
            page = wikipedia.page(keyword)
            print(page.title)
            print(page.summary)
            print(page.url)
        except wikipedia.exceptions.DisambiguationError as e:
            print(e.options)
        keyword = input("Search something in wikipedia: ")


main()