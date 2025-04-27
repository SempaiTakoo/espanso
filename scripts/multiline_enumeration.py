from pyperclip import paste

def smart_split(s: str):
    result = []
    current = []
    in_quotes = False
    quote_char = ''
    brackets = {
        '(': 0,
        '{': 0,
        '[': 0
    }

    for char in s.strip():
        if char in ('"', "'"):
            if not in_quotes:
                in_quotes = True
                quote_char = char
            elif quote_char == char:
                in_quotes = False
        elif char in brackets and not in_quotes:
            brackets[char] += 1
        elif char in (')', '}', ']') and not in_quotes:
            matching = {'}': '{', ')': '(', ']': '['}[char]
            if brackets[matching] > 0:
                brackets[matching] -= 1

        if char == ',' and not in_quotes and all(v == 0 for v in brackets.values()):
            result.append(''.join(current).strip())
            current = []
        else:
            current.append(char)

    if current:
        result.append(''.join(current).strip())

    return result

def multiline_format(input_str: str) -> None:
    cleaned = input_str.strip()
    items = smart_split(cleaned)
    res = ','.join([f'\n    {item}' for item in items])
    print(res)

if __name__ == "__main__":
    input_data = paste()
    multiline_format(input_data)
