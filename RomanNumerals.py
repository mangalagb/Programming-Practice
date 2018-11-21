def get_mappings():
    values = {}
    values['I'] = 1
    values['V'] = 5
    values['X'] = 10
    values['L'] = 50
    values['C'] = 100
    values['D'] = 500
    values['M'] = 1000
    return values

def get_other_mapping():
    num_map = {(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'),
               (90, 'XC'),(50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'),
               (5, 'V'), (4, 'IV'), (1, 'I')}
    return num_map

def find_decimal(roman):
    decimal = 0
    prev = None
    mappings = get_mappings()

    for i in range(len(roman)-1, -1, -1):
        current = mappings[roman[i]]

        if prev is not None and prev > current:
            decimal -= current
        else:
            decimal += current

        prev = current
    print(decimal)











find_decimal("IV")
find_decimal("XCV")
find_decimal("LXXXVIII")
find_decimal("MDCLXVI")


# find_roman(4)
# find_roman(95)
# find_roman(88)
# find_roman(1666)


