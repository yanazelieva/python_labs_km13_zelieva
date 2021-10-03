print('Hello!')
minutes = int(input("Введіть кількість бажаних хвилин: "))
cost = 0
nothing = False
if minutes < 0:
    print("Неможлива кількість!")
elif minutes <= 50:
    cost = 100
elif minutes <= 100:
    cost = 150
elif minutes > 100:
    cost = 150 + (minutes - 100) * 2
if nothing == False:
    print("Вартість буде складати " + str(cost) + " UAH")
    if input('Enter "stop" to exit or any key: ').lower() == 'stop':
        print("Have a nice day!")
