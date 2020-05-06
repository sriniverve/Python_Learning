'''
This is to return prime numbers upto the range
'''

def prime_numbers(number_range):
    prime_list = []
    for number in range(2,number_range):
        prime_list.append(number)
        for num in range(2,number_range):
            if num != number:
                if number % num == 0:
                    prime_list.remove(number)
                    break

    return prime_list

print(prime_numbers(100))