import urllib.request


with open("scraping.txt", "r") as a_file:
    for line in a_file:
        stripped_line = line.strip()
        filename = stripped_line[52:]
        urllib.request.urlretrieve(stripped_line, "images/" +filename)
        print(filename)