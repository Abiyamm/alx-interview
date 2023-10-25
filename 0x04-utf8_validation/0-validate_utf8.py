#!/usr/bin/python3
"""UTF-8 validation module.
"""


def validUTF8(data):
    def get_num_of_bytes(num):
        if num >> 3 == 0b11110:
            return 4
        elif num >> 4 == 0b1110:
            return 3
        elif num >> 5 == 0b110:
            return 2
        elif num >> 7 == 0:
            return 1
        return 0

    def check_continuation(index, data):
        for i in range(index + 1, index + num_bytes):
            if i >= len(data) or data[i] >> 6 != 0b10:
                return False
        return True

    index = 0
    while index < len(data):
        num_bytes = get_num_of_bytes(data[index])

        if num_bytes == 0:
            return False

        if not check_continuation(index, data):
            return False

        index += num_bytes

    return True

