rom tkinter import *

class chemistryapp:
    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")

        self.label = Label(master, text="Welcome to my app")
        self.label.pack()

        self.greet_button = Button(master, text="Option 1", command=self.opt1)
        self.greet_button.pack()

        self.greet_button = Button(master, text="Option 2", command=self.opt2)
        self.greet_button.pack()



        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    # Συναρτήσεις
    def calcpne(self):
        print('')
        A = int(input('Insert Mass Number:'))
        Z = int(input('Insert Atomic Number:'))
        # Υπολογισμοί
        N = A - Z  # Αριθμός Νετρονίων
        P = A - N  # Αριθμός Πρωτονίων
        e = P  # Αριθμός Ηλεκτρονίων
        print('')
        print('The number of Neutrons is:', N)
        print('The number of Protons is:', P)
        print('The number of Electrons is:', e)
        return Z, A

    def calcaz(self):
        print('')
        P = int(input('Insert number of Protons:'))
        n = int(input('Insert number of Neutrons:'))
        # Υπολογισμοί
        A = P + n  # Μαζικός Αριθμός
        Z = A - n  # Ατομικός Αριθμός
        print('')
        print('The Nucleon Number is:', A)
        print('The Atomic Number is:', Z)
        return Z, A

    def periodictable(self, Z, A):
        N = 13  # N = Πλήθος στοιχείων της λίστας znumb (και της elname, βεβαίως)
        znumb = [1, 3, 4, 11, 12, 19, 20, 37, 38, 55, 56, 87, 88]
        mnumb = [1, 6, 10, 23, 24, 39, 40, 85, 88, 133, 137, 223, 226]
        elname = ['(H)Hydrogen', '(Li)Lithium', '(Be)Beryllium', '(Na)Sodium', '(Mg)Magnesium', '(K)Potassium',
                  '(Ca)Calcium', '(Rb)Rubidium', '(Sr)Strontium', '(Cs)Caesium', '(Ba)Barium', '(Fr)Francium',
                  '(Ra)Radium']

        flag1 = False
        flag2 = False

        for i in range(0, N - 1):
            if znumb[i] == Z:
                pos = i
                flag1 = True
                break

        for i in range(0, N - 1):
            if mnumb[i] == A:
                pos = i
                flag2 = True
                break

        if flag1 and flag2:
            print('The element you searched for is', elname[pos])
        else:
            print('The element you searched for is not indexed yet or simply it does not exist!')

    def opt1(self):
        input('Press ENTER to start')
        print('')
        print('Option 1: Number of Neutrons, Protons and Electrons calculation')
        print('')
        Z, A = calcpne()
        periodictable(Z, A)
        print('')

    def opt2(self):
        input('Press ENTER to start')
        print('')
        print('Option 2: Atomic and Mass number calculation')
        print('')
        Z, A = calcaz(self)
        periodictable(Z, A)
        print('')

root = Tk()
my_gui = chemistryapp(root)
root.mainloop()