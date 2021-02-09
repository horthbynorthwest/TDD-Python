# this solution has been taken from the best practices part of codewars. 
# the logic is similar to mine, but just a much easier solutiont to read
def likes(names):
    # make a dictionary d of all the possible answers. Keys are the respective number
    # of people who liked it.
    
    # {} indicate placeholders. They do not need any numbers but are simply replaced/formatted
    # in the order the arguments in names are given to format
    # {others} can be replaced by its name; below the argument "others = length - 2"
    # is passed to str.format()
    d = {
        0: "no one likes this",
        1: "{} likes this",
        2: "{} and {} like this",
        3: "{}, {} and {} like this",
        4: "{}, {} and {others} others like this"
        }
    length = len(names)
    # d[min(4, length)] insures that the appropriate string is called from the dictionary
    # and subsequently returned. Min will use whichever value is lower i.e. if the length is
    # 5 it will use 4, if length is 3 it will use that.
    
    # The * in *names ensures that the list names is blown up and that format is called
    # as if each item in names was passed to format individually, i. e.
    # format(names[0], names[1], .... , names[n], others = length - 2
    return d[min(4, length)].format(*names, others = length - 2)

    
# def likes(names):
#     if len(names) == 0:
#         return "no one likes this"
#     elif len(names) == 1:
#         return names[0] + " likes this"
#     elif len(names) == 2:
#         return names[0] + " and " + names[1] + " like this"
#     elif len(names) == 3:
#         return names[0] + ", " + names[1] + " and " + names[2] + " like this"
#     elif len(names) >= 4:
#         additional_likes = str(len(names) - 2)
#         return names[0] + ", " + names[1] + " and " + additional_likes + " others like this"