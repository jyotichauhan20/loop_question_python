def pangram(string):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    i=0
    while i<len(alphabet):
        if alphabet[i] not in string:
            return "not pangrams"
        i=i+1
    else:
        return "pangrams"
string=input("some string=")
print(pangram(string))

    