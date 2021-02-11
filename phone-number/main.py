def phone_number(self, digits):
    if len(digits) == 0:
        return []
    digitsMap = {
        2: "abc",
        3: "def",
        4: "ghi",
        5: "jkl",
        6: "mno",
        7: "pqrs",
        8: "tuv",
        9: "wxyz",
    }
    result = []
    self.combine(digits, digitsMap, result)
    return result


def combine(self, digits, digitsMap, result, current_string="", current_level=0):
    if current_level == len(digits):
        result.append(current_string)
        return
    for i in digitsMap[int(digits[current_level])]:
        self.combine(digits, digitsMap, result, current_string + i, current_level + 1)
