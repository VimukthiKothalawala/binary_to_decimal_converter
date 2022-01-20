def nBinDec(num,len):
    c = 0
    decimal = 0
    while (c < len):
        place_value = 2 ** c
        value = int(num[c])
        final = value * place_value
        decimal = decimal + final
        c = c + 1
    return decimal

def aBinDec(num):
    slice = num.split('.')
    main = list(slice[0])
    main.reverse()
    sub = list(slice[1])
    main_val = nBinDec(main,len(main))
    sub_val = 0
    c=0
    len_sub = len(sub)
    while(c<len_sub):
        sub_place_value = 1/(2 ** (c+1))
        sub_value = int(sub[c])
        sub_final = sub_value*sub_place_value
        sub_val = sub_val+sub_final
        c=c+1
    FINAL = main_val+sub_val
    return FINAL


binary = input("Enter binary number - ")
binaryIn = binary
binary = list(binary)
binary.reverse()
if('.' in binary):
    print(binaryIn,' ---> ',aBinDec(binaryIn))
else:
    len = len(binary)
    print(binaryIn,' ---> ',nBinDec(binary,len))
input()