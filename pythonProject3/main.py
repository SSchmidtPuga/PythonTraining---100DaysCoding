def solution(s):
    split_strings = []
    n  = 2
    for index in range(0, len(s), n):
        split_strings.append(s[index : index + n])
    if (len(split_strings[-1]) == 1):
        last_number = (split_strings[-1] +  "_")
        split_strings[-1] = last_number
        print(split_strings)
    else:
        print(split_strings)


solution("asdfads")