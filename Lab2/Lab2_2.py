def count_char_in_string(x,c):
    return [i.count(c) for i in x]

print(count_char_in_string(input().split(),input()))