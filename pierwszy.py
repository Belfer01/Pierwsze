x=20
y=10
input("podaj watosc ")
if x>y:
    print("wartossc wieksza")
elif x<y:
    print ("wartpsc mniejsza")
elif x == 10:
    print ("wartpsc równa")
pass

i= 0
#petla
while i< 5:
    print(i)
    if i>=4:


       print("mkonies")


# program kuwa


from random import  randint
los = randint(1,5)
odp = -1
i= 0

while odp != los:
    i += 1
    odp = int(input("podaj wartosc "))
    if odp > los:
        while odp >= los:
            print("niestiety hjij zad mało")

    elif odp < los:
        while los > odp:
            print("niestiety hjij zad duzo")

print("Brawo klurw za ", i, "razme")


#222222

krotka_wartosc =( 2,4,5,6)
print(krotka_wartosc)

print("wycinak")
print(krotka_wartosc[1::4])