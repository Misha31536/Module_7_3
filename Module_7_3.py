import string
class WordsFinder:

    def __init__(self, *file_names):
        self.file_names = []
        for i in file_names:
            self.file_names.append(i)


    def get_all_words(self):
        all_words ={}
        for i in self.file_names:
            with open(i, encoding='utf8') as file:
                # for line in file:
                line = file.read()
                line = line.lower()
                line = line.rstrip(string.punctuation + string.whitespace)
                line = line.split()
                print(line)
                all_words[i] = line
                print(all_words)

find1 = WordsFinder('Module_7_3.txt')
a = find1.get_all_words()