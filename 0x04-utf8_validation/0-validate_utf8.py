"""
393. UTF-8 Validation - #Medium
checks whether a list of integers
represents a valid UTF-8 encoding.
"""


def zeros(text):
    """
    Converts an integer to its binary representation and
    pads it with leading zeros to make it 8 characters long.
    """
    return ('0' * (8 - len(str(bin(text)[2:])))) + str(bin(text)[2:])


def validUtf8(self, data: List[int]) -> bool:
    """
    Validates if the given list of
    integers is a valid UTF-8 encoding.
    """
    data = iter(data)
    for dt in data:
        dt = zeros(dt)
        if dt[0] == '1':
            count = 0
            for c in dt:
                if c != '1' or count > 4:
                    break
                count += 1
            if count in range(2, 5):
                for _ in range(1, count):
                    try:
                        nxtdt = zeros(next(data))
                        if not nxtdt or nxtdt[0] != '1' or nxtdt[1] != '0':
                            return False
                    except Exception:
                        return False
            else:
                return False
        elif dt[0] == '0':
            pass
        else:
            return False
    return True
