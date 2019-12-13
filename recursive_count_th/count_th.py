'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    counter = 0

    def recur_count(counter, word):
        if len(word) < 2:
            return counter

        if word[0] == "t" and word[1] == "h":
            counter += 1
            return recur_count(counter, word[1:])
        else:
            return recur_count(counter, word[1:])

    return recur_count(counter, word)