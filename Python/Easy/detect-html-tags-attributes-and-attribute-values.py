from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for attr, value in attrs:
            print(f"-> {attr} > {value}")

def main():
    n = int(input())
    html = "".join(input() for _ in range(n))

    parser = MyHTMLParser()
    parser.feed(html)

if __name__ == "__main__":
    main()