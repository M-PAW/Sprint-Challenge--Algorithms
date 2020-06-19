'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    # TBC
    # Convert all to lowercase
    ## This isn't needed
    # word = word.lowercase()
    """
    Needs to count the number of appearances of the lowercase substring 'th' in the string var 'word'.
    """
    # Find the index location of the first 'th'
    idx = word.find('th')

    # If no substring found, exit stage right - return 0
    if idx == -1:
        return 0

    # recursively call, and iterate a count variable in place
    # within the return

    return 1 + count_th(word[idx + 2:])



    # pass
