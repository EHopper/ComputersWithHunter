import numpy as np

def find_longest(max_num):
    """ Find longest collatz sequence for any number up to and including n
    """

    seq_len = dict()
    seq = []
    for n in range(1, max_num + 1):
        #print('Sequence starting {:.0f}'.format(n + 1))
        seq += [rec_f2(n, seq_len)]
    return seq.index(max(seq)) + 1
    #
    # v = list(seq_len.values())
    # k = list(seq_len.keys())
    # return k[v.index(max(v))]


def rec_f(n, seq_len):
    if n == 1:
        seq_len[1] = 1
        return
    #elif n in seq_len:
    #    return seq_len
    else:
        if n % 2 == 0:
            #print('{:.0f}'.format(n/2))
            rec_f(n / 2, seq_len)
            seq_len[n] = 1 + seq_len[n / 2]
            return
        else:
            #print('{:.0f}'.format(n * 3 + 1))
            rec_f(n * 3 + 1, seq_len)
            seq_len[n] = 1 + seq_len[n * 3 + 1]
            return

def rec_f2(n, seq_len):
    if n == 1:
        return 1

    if n in seq_len:
        return seq_len[n]

    if n % 2:
        result = 1 + rec_f2(n * 3 + 1, seq_len)
    else:
        result = 1 + rec_f2(n / 2, seq_len)
    seq_len[n] = result
    return result
