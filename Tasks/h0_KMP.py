from typing import Optional, List


def _prefix_fun(prefix_str: str) -> List[int]:
    """
    Prefix function for KMP

    :param prefix_str: substring for prefix function
    :return: prefix values table
    """
    P = [0] * len(prefix_str)
    j = 0
    i = 1

    while i < len(prefix_str):
        if prefix_str[j] != prefix_str[i]:
            if j > 0:
                j = P[j - 1]
            else:  # j == 0
                i += 1
        else:  # s[j] == s[i]
            P[i] = j + 1
            i += 1
            j += 1

    print(P)
    return P


def kmp_algo(inp_string: str, substr: str) -> Optional[int]:
    """
    Implementation of Knuth-Morrison-Pratt algorithm

    :param inp_string: String where substr is to be found (haystack)
    :param substr: substr to be found in inp_string (needle)
    :return: index where first occurrence of substr in inp_string started or None if not found
    """
    d = _prefix_fun(substr)
    i = 0
    j = 0
    while i < len(inp_string) and j < len(substr):
        if substr[j] == inp_string[i]:
            i += 1
            j += 1
        elif j == 0:
            i += 1
        else:
            j = d[j-1]
    else:
        if j == len(substr):
            return i-j
        return None

    print(inp_string, substr, _prefix_fun)
    #return entries
