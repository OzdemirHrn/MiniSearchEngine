import os


class listnode:

    def __init__(self, word, filename):
        self.word = word
        self.filename = filename


class Node:

    def __init__(self, char):
        self.char = char
        # 36 alphanum character
        self.children = [None] * 36
        self.isEndOfWord = False
        self.includingfiles = list()
        self.patternfiles = list()


class Trie:

    def __init__(self):
        self.root = Node("")

    # a=0. index
    # z=25. index
    # 0=26. index
    # 9=35. index
    def charToIndex(self, char):
        if str.isalpha(char):
            return ord(char) - ord('a')
        if str.isdigit(char):
            return ord(char) - 22

    # her kelimenin file'ını tutma
    # case 1: Listte node objectleri ve filelarını tutarım
    # case 2: Her file'ın ağacı farklı olur

    def insert(self, word, filename):
        temp = self.root
        for char in word:

            childIndex = self.charToIndex(char)

            if temp.children[childIndex] is None:
                temp.children[childIndex] = Node(char)
            self.onlyifnotinthelist(temp.patternfiles, filename[0])
            # temp.patterfiles.append(filename[0])
            temp = temp.children[childIndex]
        self.onlyifnotinthelist(temp.includingfiles, filename[0])
        # temp.includingfiles.add(filename[0])
        temp.isEndOfWord = True

    def search(self, word):
        word = word.lower()
        temp = self.root
        for char in word:
            childIndex = self.charToIndex(char)
            if temp.children[childIndex] is None:
                return False
            else:
                temp = temp.children[childIndex]
        # print(temp.includingfiles)
        return temp.isEndOfWord

    def startingwith(self, pattern):
        pattern = pattern.lower()
        temp = self.root
        for char in pattern:
            childIndex = self.charToIndex(char)
            if temp.children[childIndex] is None:
                print("There is no such a word in these files!")
                return False
            else:
                temp = temp.children[childIndex]
        print(temp.patternfiles)
        return True
        # sadece isEndOfWord şeysi kalkıcak

    def commonwords(self, files):
        return

    def onlyifnotinthelist(self, list, element):
        if element not in list:
            list.append(element)


# Tüm alphanumericler mi kaldırılacak? Mesela "Harun'un" kelimesini nasıl store edicem
def read_file(wordlist):
    for root, dirs, files in os.walk('sampleTextFiles'):
        for file in files:
            # wordlist += list(
            # map(re.sub, "[^0-9a-zA-Z]+", "", open(root + "/" + file, 'r').read().lower().split()))
            # wordlist += list(
            #   map(str, ''.join(filter(str.isnumeric or str.isspace or str.isalpha,
            #                          open(root + "/" + file, 'r').read())).lower().split()))

            wordlist.append(listnode(
                list(open(root + "/" + file, 'r').read().replace(',', '').replace('.', "").replace("'", "")
                     .replace('-', "").replace(';', "").lower().split()), file.split()))
            # çok saçma oldu ama kelimelerden bunları ayırmam lazım mı değil mi ona göre uğraşcam


if __name__ == '__main__':

    wordlist = list()
    read_file(wordlist)

    trie = Trie()
    for obje in wordlist:
        for key in obje.word:
            trie.insert(key, obje.filename)

    print(trie.search("x"))

    print(trie.startingwith("primi"))
