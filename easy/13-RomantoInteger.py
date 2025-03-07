def romanToInt(s: str) -> int:
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    output = 0
    i = 0
    while i < len(s) - 1:
        if ((s[i] == 'I' and (s[i + 1] == 'V' or s[i + 1] == 'X')) or
                (s[i] == 'X' and (s[i + 1] == 'L' or s[i + 1] == 'C')) or
                (s[i] == 'C' and (s[i + 1] == 'D' or s[i + 1] == 'M'))):
            output -= roman_dict[s[i]]
        else:
            output += roman_dict[s[i]]
        i += 1
    output += roman_dict[s[-1]]
    return output


print(romanToInt('CDL'))
