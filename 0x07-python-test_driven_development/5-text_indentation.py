#!/usr/bin/python3
def text_indentation(text):
    text_list = list(text)

    for i in range(len(text_list)):
        if text_list[i] in ['.', '?', ':']:
            text_list[i + 1] = '\n'
            i += 1
            text_list.insert(i + 1, '\n')

    for i in text_list:
        print(i, end="")
