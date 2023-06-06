def pr1():
    class IceCreamStand:

        def __init__(self, flavors):
            self.flavors = flavors

        def spisok_mor(self):
            self.flavors = ['Апельсиновое', 'Арбузное', 'Банановое', 'Шоколадное']
            print(self.flavors)

    IceCreamStand1 = IceCreamStand("dawda")
    IceCreamStand1.spisok_mor()


def pr2():
    class IceCreamStand:

        def __init__(self, flavors, location, time):
            self.flavors = flavors
            self.location = location
            self.time = time

        def loc_time(self):
            print('Местонахождение:', self.location, 'Время работы:', self.time)

        def spisok_mor(self):
            self.flavors = ['Апельсиновое', 'Арбузное', 'Банановое', 'Шоколадное']
            print(self.flavors)

        def spisok_mor1(self):
            self.flavors.append('Абрикосовое')
            self.flavors.remove('Апельсиновое')
            print(self.flavors)

        def spisok_mor2(self):
            for i in range(len(self.flavors)):
                if self.flavors[i] == "Арбузное":
                    print('Арбузное мороженое в наличии')
                    break
                else:
                    print('Арбузное мороженое не в наличии')

        def tip_mor1(self):
            alph = {'Арбузное': '', 'Банановое': '', 'Шоколадное': '', 'Абрикосовое': ''}
            for i in alph:
                if i == 'Арбузное' or i == 'Абрикосовое':
                    alph[i] = 'Мороженое на палочке'
                    print(alph[i])
                else:
                    alph[i] = 'Мягкое мороженое'
                    print(alph[i])

    IceCreamStand1 = IceCreamStand("awdad", "adwad", "dwadaw")
    IceCreamStand1.spisok_mor()
    IceCreamStand1.spisok_mor1()
    IceCreamStand1.spisok_mor2()
    IceCreamStand1.tip_mor1()


def pr3():
    class IceCreamStand:

        def __init__(self, flavors, location, time):
            self.flavors = flavors
            self.location = location
            self.time = time

        def loc_time(self):
            print('Местонахождение:', self.location, 'Время работы:', self.time)

        def spisok_mor(self):
            self.flavors = ['Апельсиновое', 'Арбузное', 'Банановое', 'Шоколадное']
            print(self.flavors)

        def spisok_mor1(self):
            self.flavors.append('Абрикосовое')
            self.flavors.remove('Апельсиновое')
            print(self.flavors)

        def spisok_mor2(self):
            for i in range(len(self.flavors)):
                if self.flavors[i] == "Арбузное":
                    print('Арбузное мороженое в наличии')
                    break
                else:
                    print('Арбузное мороженое не в наличии')

        def tip_mor1(self):
            alph = {'Арбузное': '', 'Банановое': '', 'Шоколадное': '', 'Абрикосовое': ''}
            for i in alph:
                if i == 'Арбузное' or i == 'Абрикосовое':
                    alph[i] = 'Мороженое на палочке'
                    print(alph[i])
                else:
                    alph[i] = 'Мягкое мороженое'
                    print(alph[i])

    IceCreamStand1 = IceCreamStand("awdad", "adwad", "dwadaw")

    IceCreamStand1.spisok_mor()
    IceCreamStand1.spisok_mor1()
    IceCreamStand1.spisok_mor2()
    IceCreamStand1.tip_mor1()

    import tkinter as tk

    window = tk.Tk()
    pr1 = tk.Label(window, text='dadaw')
    pr2 = tk.Label(window, text='adada')
    pr3 = tk.Label(window, text='dawdaw')
    pr4 = tk.Label(window, text='dwada')
    pr1.pack()
    pr2.pack()
    pr3.pack()
    pr4.pack()

    window.mainloop()


pr3()
