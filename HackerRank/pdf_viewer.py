# https://www.hackerrank.com/challenges/designer-pdf-viewer/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

LETTERS = "abcdefghijklmnopqrstuvwxyz"


def designerPdfViewer(h, word):
    # Write your code here
    heights = [h[LETTERS.index(letter)] for letter in word]
    return max(heights) * len(word)


test = designerPdfViewer(
    [1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 7],
    "zaba",
)
print(test)
assert 28 == test
