import time
n = 0
fizz=False
buzz=False

while True:
    n+=1
    output=""
    if not n%3:
        output="Fizz"
    if not n%5:
        output+="Buzz"
    if output=="":
        output=n
    print(output)

    time.sleep(.5)


