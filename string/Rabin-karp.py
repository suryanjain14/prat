def hash(string):
    value = 0
    for i in range(len(string)):
        value = (value + ord(string[i]) ** i)
    return value


def rabinKarp(pattern: str, txt: str):
    plen = len(pattern)
    tlen = len(txt)
    start = 0
    end = plen
    ans = []
    for i in range(plen - 1, tlen):
        if hash(pattern) == hash(txt[start:end]):
            print("pattern Found at index", start)
        start += 1
        end += 1


rabinKarp('TEST', "THIS IS A TEST TEXT")
rabinKarp("AABA", "AABAACAADAABAABA")
