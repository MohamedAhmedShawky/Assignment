import textwrap

def majority(a):
        if len(a) == 0:
            return 0
        if len(a) == 1:
            return a[0]
        half = len(a) // 2
        left = majority(a[0:half])
        right = majority(a[half:])
        if left == right:
            return left
        if a.count(left) > half:
            return left
        if a.count(right) > half:
            return right
        return 0

n=int(input("enther the n "))
if n>=1 and n<=(10**5):

    StrNumber = input("enter the number ")
    length = len(StrNumber)
    splitLenght = length % n
    if splitLenght == 0:
        l = int(length / n)
    else:
        l = n

    List = textwrap.wrap(StrNumber, l)

    ListIntger = []
    for i in List:
        ListIntger.append(int(i))

    x = majority(ListIntger)
    if x == 0:
        print(x)
        print("there is no majority element")
    else:
        print(1)
        print(x, "is the majority element")
