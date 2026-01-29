def sum_even_numbers():
    return sum((i for i in range(1, 11) if i % 2 == 0))
if __name__ == '__main__':
    print('Sum of even numbers from 1 to 10:', sum_even_numbers())