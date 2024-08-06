punctuation = [',', '.', '=', '!', '?', ';', ':', ' - ']
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
                for j in line:
                    if j in punctuation:
                        line = line.replace(j, " ")
                line = line.lower()
                line = line.split()
                all_words[i] = line
                return all_words

    def find(self, word):
        for name, words in self.get_all_words().items():
            if word in words:
                print(name, words.index(word) + 1)

    def count(self, word):
        for name, words in self.get_all_words().items():
                print(name, words.count(word))

# find1 = WordsFinder('Module_7_3.txt')
# a = find1.get_all_words()
# find1.find("text")
# find1.count("text")
# finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt')
# print(finder1.get_all_words())
# print(finder1.find('captain'))
# print(finder1.count('captain'))
finder1 = WordsFinder('Rudyard Kipling - If.txt',)

print(finder1.get_all_words())
print(finder1.find('if'))
print(finder1.count('if'))