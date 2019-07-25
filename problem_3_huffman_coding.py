import sys


def huffman_encoding(data):
    """
    Build tree of tuples and find codes by traversing tuple.
    Build output string from codes.
    """
    if not data:
        return '0', ''

    print(f"length of sentence is {len(data)}")
    codes = {}
    tree = build_tree(frequency(data))
    trimmed_tree = trim_tree(tree)

    set_codes(trimmed_tree, codes)
    output = ""
    for s in data:
        output += codes[s]
    return output, trimmed_tree


def huffman_decoding(data, tree):
    """
    Receive a bitstring and a tuple tree.

    Traverse the tree to find the character codes in the global code.
    """
    if tree == '':
        return ''
    output = ''
    sub_tree = tree
    for bit in data:
        if bit == "0":
            sub_tree = sub_tree[0]
        else:
            sub_tree = sub_tree[1]

        if isinstance(sub_tree, str):
            output += sub_tree
            sub_tree = tree
    return output


def frequency(str):
    """
    Frequency as sorted tuples.

    Get the frequency distribution for the string's characters as
    sorted tuples.
    """
    frequency_dict = {}
    for c in str:
        frequency_dict[c] = frequency_dict.get(c, 0) + 1

    letters = frequency_dict.keys()
    tuples = []
    for l in letters:
        tuples.append((frequency_dict[l], l))
    tuples.sort()
    return tuples


def build_tree(tuples):
    """
    Create a tree from nested tuples (left is always t[0], right t[1]).

    Input: list of tuples
    return 1 tuple of nested tuples
    Value of join nodes is the sum of the frequency of their children.
    Join nodes needed for creation but not needed for encoding/decoding.
    """
    while len(tuples) > 1:
        least_two = tuple(tuples[0:2])
        combined_freq = least_two[0][0] + least_two[1][0]
        rest = tuples[2:]
        tuples = rest + [(combined_freq, least_two)]
        tuples.sort(key=lambda t: t[0])
    return tuples[0]


def trim_tree(tree):
    """Remove branch nodes and frequency counts from tuple tree recursively."""
    sub_tree = tree[1] # ignore frequency count
    if isinstance(sub_tree, str):
        return sub_tree
    else:
        return(trim_tree(sub_tree[0]), trim_tree(sub_tree[1]))

def set_codes(tree, codes, code=""):
    if isinstance(tree, str):
        codes[tree] = code
    else:
        set_codes(tree[0], codes, code+"0")
        set_codes(tree[1], codes, code+"1")

if __name__ == "__main__":

    a_great_sentence = "The bird is the word"
    an_okay_sentence = "2019 Can it do special characters? ıÍ´‰Œ˚•˚£££ß´ßßßßåççÇç"
    a_bad_sentence = ''

    def print_test(sentence):
        print("The size of the data is: {}\n".format(sys.getsizeof(sentence)))
        print("The content of the data is: {}\n".format(sentence))

        encoded_data, tree = huffman_encoding(sentence)

        print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
        print("The content of the encoded data is: {}\n".format(encoded_data))

        decoded_data = huffman_decoding(encoded_data, tree)

        print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
        print("The content of the decoded data is: {}\n".format(decoded_data))
        print("\n-----------------------------\n")

    # normal case
    print_test(a_great_sentence)

    # edge case 1 special characters
    print_test(an_okay_sentence)

    # edge case 2 no characters
    print_test(a_bad_sentence)
