def decode(message_file):
    with open(message_file) as file:
        code_dictionary = {}
        for line in file:
            code_dictionary[int(line.split()[0])] = line.split()[1]
        key_list = list(code_dictionary.keys())
        key_list.sort()
        i = 0
        j = 2
        decode_string = ""
        while i < len(key_list):
            decode_string = decode_string + code_dictionary.get(key_list[i]) + " "
            i = i + j
            j = j + 1
        return decode_string

print(decode('coding_qual_input.txt'))
