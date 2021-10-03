while True:
        try:
            a = float(input("Введіть значення магнітуди: "))

            if 0 < a < 2:
                print("Micro")
            elif 2 <= a < 3:
                print("Very minor")
            elif 3 <= a < 4:
                print("Minor")
            elif 4 <= a < 5:
                print("Light")
            elif 5 <= a < 6:
                print("Moderate")
            elif 6 <= a < 7:
                print("Strong")
            elif 7 <= a < 8:
                print("Major")
            elif 8 <= a < 10:
                print("Great")
            elif a>10:
                print("Meteoric!")
        except: # ???
            if a<0:
                print("Спробуйте ще раз!")
                continue
            if input('Enter "stop" to exit or any key to continue: ').lower() == 'stop':
                print("Have a nice day!")
                break

