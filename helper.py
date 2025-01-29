def getPositiveInt(prompt):
    ret_val = 0 
    while True:
        num = getint(prompt) # -18
        if num >= 0:
            print("Bu bir pozitif integer sayıdır")
            ret_val = num
            break
        else:
            print("Bu bir pozitif int değildir!")
           
        
    return ret_val

def getNegativeInt(prompt):
    ret_val = 0
    while True:
        num = getint(prompt) # -18
        if num < 0:
            print("Bu bir negatif integer sayıdır")
            ret_val = num
            break
        else:
            print("Bu bir negatif int değildir!") 
    return ret_val
def getint(prompt):
    ret_val = 0

    while True:
        num = input(prompt)
        if num[0] == "-" or num[0] == "+":
            if num[1:].isdigit():
                print("Bu bir tam sayıdır")
                ret_val = int(num)
                break
            else:
                print("Lütfen bir integer sayı girin")
                
        else:
            if num[0].isdigit():
                print("Bu bir tam sayıdır")
                ret_val = int(num)
                break
    return ret_val

def isHarshad(num):
    ret_val = True

    if num != 0:
        str_num = str(num)
        sum = 0
        for i in str_num:
            sum += int(i)

        if num % sum != 0:
            ret_val = False
    else:
        ret_val = False
    return ret_val
