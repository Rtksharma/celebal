def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        substr = []  
        for j in range(i, i+k):
            if string[j] not in substr:
                substr.append(string[j])
        print(''.join(substr))
