import pickle

filename = 'betalinger.pk'

fodboldtur ={}

def afslut():
    outfile = open(filename, 'wb')
    pickle.dump(fodboldtur, outfile)
    outfile.close()
    print("Programmet er afsluttet!")

def printliste():
    for item in fodboldtur.items():
        print(item)
    menu()

def menu():
    print("MENU")
    print("1: Print liste")
    print("2: Afslut program")
    print("betal")
    valg = input("Indtast dit valg:")
    if
    if (valg == '1'):
        printliste()
    if (valg == '2'):
        afslut()

infile = open(filename,'rb')
fodboldtur = pickle.load(infile)
infile.close()
menu()