"""2.8.4 Crypt Kicker"""

import sys


n = int(input())
out_words = set(input() for _ in range(0, n))

for sentence in sys.stdin.read().splitlines():
    in_words = list(set(sentence.split()))
    len_in_words = len(in_words)

    backtrack_queue = [(0, {})]
    result_decryption_table = None

    while backtrack_queue:
        in_i, decryption_table = backtrack_queue.pop()

        if in_i == len_in_words:
            result_decryption_table = decryption_table
            break

        in_word = in_words[in_i]
        len_in_word = len(in_word)

        for out_word in out_words:
            if len_in_word != len(out_word):
                continue

            decryption_table_update = decryption_table.copy()
            decryption_failed = False

            for in_c, out_c in zip(in_word, out_word):
                if in_c in decryption_table_update:
                    if decryption_table_update[in_c] != out_c:
                        decryption_failed = True
                        break

                elif out_c in decryption_table_update.values():
                    decryption_failed = True
                    break

                else:
                    decryption_table_update[in_c] = out_c

            if not decryption_failed:
                backtrack_queue.append((in_i + 1, decryption_table_update))

    if result_decryption_table is None:
        result_decryption_table = {c: '*' for c in 'abcdefghijklmnopqrstuvwxyz'}

    print(sentence.translate(''.maketrans(result_decryption_table)))
