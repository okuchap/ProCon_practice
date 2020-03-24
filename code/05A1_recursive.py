length = 3
n_bit = 3
S = [n_bit - 1] * length


def bit_enum(i, n_bit=3):
    if i == length:
        print(S)
        return None
    for k in range(n_bit):
        bit_enum(i + 1, n_bit)
        S[i] = k


bit_enum(0)
