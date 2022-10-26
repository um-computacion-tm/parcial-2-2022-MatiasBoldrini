class Compress():
    def __init__(self):
        pass

    def compress(self, text):
        dictionary = {}
        text = text.split(' ')
        list = []
        counter = 1
        for word in text:
            if word not in dictionary:
                dictionary[word] = counter
                counter += 1
            list.append(dictionary[word])
        return list, dictionary

    def uncompress(self, list, dictionary):
        text = ''
        for i in list:
            text += text.join([f'{key} ' for key,
                              value in dictionary.items() if i == value])
        return text.rstrip()


if __name__ == '__main__':
    pass
