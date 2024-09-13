import inflect
p=inflect.engine()
names=[]
while True:
    try:
        names.append(input("Name: "))
    except EOFError:
        print(f"Adieu, adieu, to {p.join(names)}")
        print('\n')
        break
