import argparse
import random
import re
from transliterate import translit, get_available_language_codes


def transliterate(name):
    return translit(name, reversed=True)

def canonise(name):
    return re.compile(r'[^a-zA-Z]').sub(u'', name)

def genPassword():
    return "".join([random.choice("123456abcd") for i in range(10)])


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', help='input file', default="names.txt")
    args = parser.parse_args()

    filename = args.i
    for name in open(filename, "r").readlines():
        name = name.strip().split()
        name, suranme = name[-1], " ".join(name[:-1])
        print("b-2019-" + canonise(transliterate(suranme.lower())), genPassword(), name + " " + suranme, sep = ",") 