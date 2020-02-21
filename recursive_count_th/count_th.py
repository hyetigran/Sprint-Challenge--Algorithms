'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word, count=0):
    # base case: if there are characters in the array, return total count
    if not word:
        return count
    # if there are 2 characters in the array and t, h are the first and second element, respectively
    # then increment count and call function by passing word - 2 characters
    elif len(word) > 1 and "t" in word[0] and "h" in word[1]:
        count += 1
        return count_th(word[2:], count)
    # otherwise, return the function minus 1 character
    else:
        return count_th(word[1:], count)
