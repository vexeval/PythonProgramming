def fprint(text):
    c = 0
    line = ""
    while (c < (len(text)+2)):
        line += '*'
        c += 1
    print(line)
    print ('*', text)
    print(line)


# TODO
def make_palindrome(text): # returns a palindrome by appending its reverse ("abc" -> "abccba")
    print("")