from urllib.request import urlopen


story = urlopen('http://sixty-north.com/c/t.txt')
story_words = []
for line in story:
        line_words = line.decode('utf-8').split()
        for word in line_words:
            story_words.append(word)
story.close()

for word in story_words:
    print(word)


def display_nth_root(radicand, n):
    root = nth_root(radicand, n)
    message = "The " + ordinal(n) + " root of " \
        +str(radicand) + " is " +str(root)
    print(message)