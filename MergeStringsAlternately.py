def mergeAlternately(self, word1: str, word2: str) -> str:
    al = len(word1)
    bl = len(word2)
    output = ''
    for i in range(min(al, bl)):
        output += word1[i] + word2[i]
    return output + word1[bl:] + word2[al:]