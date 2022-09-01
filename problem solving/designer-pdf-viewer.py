def designerPdfViewer(h, word):
    word = word.lower()
    letters = []
    for i in word:
        letters.append(ord(i)-97)
    letters = set(letters)
    print(letters)
    heights = []
    for i in letters:
        heights.append(h[i])
    maxHeight = max(heights)
    width = len(word)
    area = maxHeight * width
    return area

designerPdfViewer("aaaa")