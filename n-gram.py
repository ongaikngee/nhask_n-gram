# read from corpus
def read_file(path):
    with open(path, 'r') as f:
        lines = f.read().split('\n')
    lines = [x.split(' ') for x in lines]
    return lines

# create bigram
def create_bigram(lines):
    print('TODO: This is create biagram and will return a dict of dict')
    return [{"this":{"is":1, "will":2}}, {"is": {"create":1}}]


def generate_predication(bigram, start):
    print('TODO: THis will generate the predition')
    return "TODO: This is it!"


def main():
    lines = read_file('toy-corpus.txt')
    bigram = create_bigram(lines)
    prediction = generate_predication(bigram, "Technlogy")
    print(prediction)

main()