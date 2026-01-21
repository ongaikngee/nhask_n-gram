# read from corpus
def get_lines():
    print('Will get line here and return an list of list')
    return [["This is an example"], ["This is another example"]]

# create bigram
def create_bigram(lines):
    print('This is create biagram and will return a dict of dict')
    return [{"this":{"is":1, "will":2}}, {"is": {"create":1}}]


def generate_predication(bigram, start):
    print('THis will generate the predition')
    return "This is it!"


def main():
    lines = get_lines()
    bigram = create_bigram(lines)
    prediction = generate_predication(bigram, "Technlogy")
    print(prediction)

main()