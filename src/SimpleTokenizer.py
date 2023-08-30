class SimpleTokenizer:

    def encode(self, mapping, sentence):
        return [mapping[key]
                for key in sentence]

    def decode(self, mapping, sentence):
        return ''.join([mapping[key]
                        for key in sentence])
