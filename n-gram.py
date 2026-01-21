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

def generate_sentence(bigram, start):
    sentence = [start]
    key = start
    while len(sentence) < 20:
        if key in bigram:
            next_word = max(bigram[key], key=bigram[key].get)
            sentence.append(next_word)
            key = next_word
        else:
            break
    return ' '.join(sentence)


def main():
    lines = read_file('toy-corpus.txt')
    bigram = create_bigram(lines)
    prediction = generate_sentence(bigram, "Technology")
    print(prediction)

main()