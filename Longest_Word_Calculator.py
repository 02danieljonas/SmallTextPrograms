Words=open("words.txt", "r")
List=[]
long=""
Letters = ("b","B","L","l","g","G","s", "S","h","h", "E", "e","Z", "z","I", "i", "O", "o")
for line in Words:
    for word in line.split():
        if all(elem in Letters for elem in word):
            if len(word) > len(long):
                long = word
                print(long)

#if the word has all the letters in "Letters" and it is the longest, it prints

# 9=b
# 8=B
# 7=L
# 6=G
# 5=S
# 4=h
# 3=E
# 2=Z
# 1=I
# 0=O