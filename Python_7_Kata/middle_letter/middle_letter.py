def middle_letter(str):
    if (len(str) % 2 == 0):
        s = int(len(str)/2)
        return str[s-1] + str[s]
    else:
       s = int(len(str)/2)
       return str[s]