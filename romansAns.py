def roman_to_int(s: str) -> int:
    values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    total = 0
    for i in range(len(s)):
        current = values[s[i]]
        result = str(i) + " " + str(current) + " "
        print(result)
        if i < len(s) - 1 and current < values[s[i+1]]:
            print('In')
            total -= current
        else:
            total += current
    return total


print(roman_to_int('DCXC'))
