def middle_letter(str):
    if len(str) == 1:
        return str
    if (len(str) % 2 == 0):
        return "it"
    else:
       s = len(str)/2
       s = round(s) 
       return str[s-1]