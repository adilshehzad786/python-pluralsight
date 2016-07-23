from urllib.request import urlopen

def fetch_words():
    with urlopen('http://sixty-north.com/c/t.txt') as story:
        story_words = []
        for line in story:
            # divide line into words based on whitespace boundaries
            # http request transfers raw bytes over the network.
            line_words = line.decode('utf-8').split()
            for word in line_words:
                story_words.append(word)

    for word in story_words:
        print(word)

# print(__name__)

# If this module is being run as a script, then execute
if __name__ == '__main__':
    fetch_words()
