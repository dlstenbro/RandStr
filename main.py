"""
    Name: RandStr

    Purpose:
        Simple app that retrieves a list of words or phrases
        then randomly chooses x number of words out of the list.

    Usage:
        main.py x y
        x = request type
        y = words/phrases wanted
"""

from RandomRequest import RandomStringRequest
import sys


def main(args):
    data_type = args[1]
    num_of_words = args[2]

    words = RandomStringRequest(data_type).get_word_list(num_of_words)
    str = " ".join((word for word in words))
    print(str)


if __name__ == "__main__":
    main(sys.argv)
