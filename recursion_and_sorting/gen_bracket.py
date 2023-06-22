def gen_binary(n: int, prefix: str = '', balance: int = 0):
    if n == 0 and balance == 0:
        print(prefix)
    if n > 0:
        gen_binary(n - 1, prefix + '(', balance + 1)
    if balance > 0:
        gen_binary(n, prefix + ')', balance - 1)


gen_binary(int(input()), '')
