import requests
import sys
import random

"""
    Class Name: RandomRequest
    Purpose:
            Receives a type of word request then gets a random value
            from https://www.randomlists.com/data/.
            Returns total number of random words/phrases requested
            back to user.
"""


class RandomStringRequest:
    MAIN_SITE = "https://www.randomlists.com/data/"
    COMPOUND_WORDS = MAIN_SITE + "compound-words.json"
    NOUNS = MAIN_SITE + "nouns.json"
    PREPOSITIONS = MAIN_SITE + "prepositions.json"
    SPANISH_WORDS = MAIN_SITE + "spanish-words.json"
    VERBS = MAIN_SITE + "verbs.json"
    VOCAB_WORDS = MAIN_SITE + "vocabulary-words.json"
    ADVERBS = MAIN_SITE + "adverbs.json"

    def __init__(self, random_type):
        request_type = self.determine_type(random_type)
        response = requests.get(request_type)
        self.data = response.json()

    def determine_type(self, request_type):
        if request_type == "cw":
            return self.COMPOUND_WORDS
        elif request_type == "n":
            return self.NOUNS
        elif request_type == "p":
            return self.PREPOSITIONS
        elif request_type == "s":
            return self.PANISH_WORDS
        elif request_type == "v":
            return self.VERBS
        elif request_type == "vw":
            return self.VOCAB_WORDS
        elif request_type == "a":
            return self.ADVERBS
        else:
            sys.exit("Invalid request type. Given: %s" % request_type)

    def get_word_list(self, num_words):
        word_list = []
        for i in range(int(num_words)):
            word_list.append(random.choice(self.data['data']))
        return word_list
