def gcdOfStrings(self, str1: str, str2: str) -> str:
    if len(str1) < len(str2):
        str1, str2 = str2, str1
    while str1!='':
        str1.replace(str2)
        if len(str1) < len(str2):
            str1, str2 = str2, str1
