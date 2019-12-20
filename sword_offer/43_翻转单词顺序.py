"""
例如，“student. a am I”。正确的句子应该是“I am a student.”
"""


def reverse_word(sentence):
    if not sentence or not len(sentence):
        return ""
    lst = sentence.split()
    lst.reverse()
    return " ".join(lst)


def reverse_word2(sentence):
    if not sentence or not len(sentence):
        return ""
    return " ".join(sentence.split()[::-1])


if __name__ == '__main__':
    print(reverse_word("student. a am I"))
    print(reverse_word2("student. a am I"))
