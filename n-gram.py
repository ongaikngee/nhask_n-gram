# read from corpus
def read_file(path):
    with open(path, 'r') as f:
        lines = f.read().split('\n')
    lines = [x.split(' ') for x in lines]
    return lines

# create bigram
def create_bigram(lines):
    bigram = {}
    for line in lines:
        for i in range(len(line)-1):
            key = line[i]
            if key in bigram:
                if line[i+1] in bigram[key]:
                    bigram[key][line[i+1]] += 1
                else:
                    bigram[key][line[i+1]] = 1
            else:
                bigram[key] = {line[i+1]:1}
    return bigram

def generate_predication(bigram, start):
    print('TODO: THis will generate the predition')
    return "TODO: This is it!"


def main():
    lines = read_file('toy-corpus.txt')
    bigram = create_bigram(lines)
    prediction = generate_predication(bigram, "Technlogy")
    print(prediction)

main()