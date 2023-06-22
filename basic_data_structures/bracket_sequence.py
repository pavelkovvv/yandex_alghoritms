def is_correct_bracket_seq(seq: str):
    def one(sq:str):
        dict_val = {
            '(': ')',
            '{': '}',
            '[': ']',
        }
        first_half = sq[0:int(len(sq)/2)]
        second_half = sq[int(len(sq)/2):len(sq)]

        for key, value in dict_val.items():
            first_half = first_half.replace(key, value)
        if first_half[::-1] == second_half:
            return True
        return False

    if one(seq):
        return True
    elif len(seq) % 2 == 1:
        return False
    elif len(seq) == 2 and seq[0] != seq[1]:
        return False
    elif seq.count('(') == seq.count(')') and seq.count('[') == seq.count(']') and seq.count('{') == seq.count('}'):
        dict_vl = {
            '(': ')',
            '{': '}',
            '[': ']',
        }
        for key, value in dict_vl.items():
            seq = seq.replace(key, value)
        lst = list()
        for i in seq:
            lst.append(i)
        x = len(lst)
        i = 0
        while len(lst) != 0:

            for j in range(len(lst)):
                try:
                    if lst[j] == lst[j+1]:
                        del lst[j+1]
                        del lst[j]
                except IndexError:
                    break
                i += 1
            if i > 505:
                if len(lst) == x:
                    return False
                break

        if len(lst) == 0:
            return True
        return False
    return False


print(is_correct_bracket_seq(input()))
