def compute_sum():
    result = 1
    for i in range(2, 11):
        result += i
    return result
if __name__ == '__main__':
    print('The sum of 1 to 10 is:', compute_sum())