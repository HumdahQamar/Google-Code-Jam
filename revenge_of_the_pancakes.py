import re


def straighten_sequence(sequence):
    flip_count = 0
    if '-' in sequence:
        for tup in zip(sequence[1:]+'+', sequence):
            if tup[0] is not tup[1]:
                flip_count += 1
    return flip_count


def parse_input_file():
    with open('input.txt', 'r') as in_file:
        contents = in_file.read()
        case_count = int(re.search(r"\d+", contents).group())
        cases = contents.split()[1:]

    output = [straighten_sequence(sequence) for sequence in cases]

    with open('output.txt', 'w') as out_file:
        while len(output) > 0:
            result = output.pop(0)
            out_file.write("Case #%d: %s\n" % (case_count-len(output), result))


if __name__ == '__main__':
    parse_input_file()
