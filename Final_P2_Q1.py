# Q1

def dec_to_binary(number):
    if number == 0:
        return "0"
    elif number == 1:
        return "1"
    else:
        return dec_to_binary(number // 2) + str(number % 2)


print(dec_to_binary(7))
print(dec_to_binary(10))

