def correct_symbol(string):
    """1 тест"""
    mistake = {"0": "O", "5": "S", "1": "I"}
    for item in string:
        if item in mistake:
            string = string.replace(item, mistake[item])
    return string


# if __name__ == '__main__':
#     print(correct_symbol('PAR15'))


def final_grade(exam, projects):
    """2 тест"""
    if exam <= 0:
        raise ValueError('Число экзаменов не может быть меньше 0')
    if projects <= 0:
        raise ValueError('Число проектов не может быть меньше 0')
    if exam >= 90 or projects >= 10:
        return 100
    elif exam > 75 and projects >= 5:
        return 90
    elif exam >= 50 and projects >= 2:
        return 75
    else:
        return 0


# if __name__ == '__main__':
#     print(final_grade(55, 2))


def square_sum(numbers):
    """3 тест"""
    answer = 0
    for i in numbers:
        if i < 0:
            raise ValueError('Число должно быть положительным')
        else:
            answer += i ** 2
    return answer


square_sum1 = lambda num: num**2

if __name__ == '__main__':
    print(square_sum([0, 3, 4, 5]))
    print(square_sum1(4))
