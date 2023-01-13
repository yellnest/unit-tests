import math


def correct_symbol(string):
    """
    Задача 1:
    Заменяет определенные цифры которые похожи на буквы(этими же буквами)
    """
    mistake = {"0": "O", "5": "S", "1": "I"}
    for item in string:
        if item in mistake:
            string = string.replace(item, mistake[item])
    return string


def correct_symbol2(string):
    """1 тест ч2"""
    return string.replace('1', 'I').replace('0', 'O').replace('5', 'S')


# if __name__ == '__main__':
#     print(correct_symbol('PAR15'))
#     print(correct_symbol2('PAR15'))


def final_grade(exam, projects):
    """
    Задача 2:
    Возвращает число баллов студента в зависимости от кол-во его экзаменов и проектов
    """
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
    """
    Задача 3:
    Возвращает сумму чисел в квадрате
    """
    answer = 0
    for i in numbers:
        if i < 0:
            raise ValueError('Число должно быть положительным')
        else:
            answer += i ** 2
    return answer


"""2 тест ч2"""
square_sum2 = lambda num: num ** 2


def square_sum3(numbers):
    """2 тест ч3"""
    return sum(number ** 2 for number in numbers)


# if __name__ == '__main__':
#     print(square_sum([0, 3, 4, 5]))
#     print(square_sum2(4))
#     print(square_sum3([0, 3, 4, 5]))


def solution_gaps(s):
    """
    Задача 4:
    Разделяет слипшийся текст пробелами
    """
    s = s.split()
    repeated_letter = ''
    res = []
    for i in s:
        for j in i:
            if j.isupper():
                if j != repeated_letter:
                    repeated_letter = j
                    i = i.replace(repeated_letter, ' ' + repeated_letter)
        res.append(i)
    return ''.join(res)


# if __name__ == '__main__':
#     print(solution_gaps('companyOtherChildCallGet'))


def likes(names):
    """
    Задача 5:
    Возвращает разный текст в зависимости от количества отправленных имён
    """
    if len(names) == 0:
        return 'no one likes this'
    elif len(names) == 1:
        return f'{names[0]} likes this'
    elif len(names) == 2:
        return f'{names[0]} and {names[1]} like this'
    elif len(names) == 3:
        return f'{names[0]}, {names[1]} and {names[2]} like this'
    else:
        return f'{names[0]}, {names[1]} and {len(names) - 2} others like this'


# if __name__ == '__main__':
#     print(likes(['Nene Romanova', 'Galatea', 'Anri', 'Largo', 'Linna Yamazaki', 'Brian J. Mason', 'Sylvie']))


def alphabet_position(text):
    """
    Задача 6:
    Возвращает нумерацию(в алфавите) каждой буквы из строки
    """
    alp = "abcdefghijklmnopqrstuvwxyz"
    return " ".join(str(alp.find(c) + 1) for c in text.lower() if c in alp)


def alphabet_position2(text):
    """6 тест ч2"""
    alp = "abcdefghijklmnopqrstuvwxyz"
    a = []
    for c in text.lower():
        if c in alp:
            a.append(str(alp.find(c) + 1))
    return ' '.join(a)


# if __name__ == '__main__':
#     print(alphabet_position('"The sunset sets at twelve o'))
#     print(alphabet_position2('"The sunset sets at twelve o'))


def scramble(s1, s2):
    """
    Задача 9, но не проходит из-за скорости:
    Проверяет можно ли из случайных букв s1 собрать слово из s2
    """
    a = []
    c = list(s1)
    for i in s2:
        if i in c:
            a.append(i)
            c.pop(c.index(i))
    if ''.join(a) == s2:
        return True
    return False


def scramble2(s1, s2):
    """
    Задача 7 ч2 :
    """
    for c in set(s2):
        print(c)
        if s1.count(c) < s2.count(c):
            return False
    return True


# if __name__ == '__main__':
#     print(scramble('cowdarfewqss', 'codewars'))
# print(scramble2('miahailmnqrbwbfuyl', 'wlmmrmluf'))


def cakes(recipe, available):
    """
    Задача 8:
    Проверяет сколько можно сделать тортов из доступных
    возвращает число
    """
    return min([available[i] // recipe[i] if i in available else 0 for i in recipe])


def cake(recipe, available):
    """
    Это написал потому что не понимал как делать такие циклы через else
    """
    return min([available[i] // recipe[i] for i in recipe if i in available])


# if __name__ == '__main__':
#     print(cakes({"flour": 500, "sugar": 200, "eggs": 1}, {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}))
#     print (cake({"flour": 500, "sugar": 200, "eggs": 1}, {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}))


def generate_hashtag(s):
    """
    Задача 9:
    Добавление # и удаление пробелов
    Если больше 140 или пустой то False
    """
    if not s or len(s) > 140:
        return False
    return f"#{s.title().replace(' ', '')}"


def generate_hashtag2(s):
    """
    Задача 9 ч2:
    """
    ans = '#' + str(s.title().replace(' ', ''))
    a = False
    return a if not s or len(s) > 140 else ans


# if __name__ == '__main__':
#     print(generate_hashtag('Codewars Is Nice'))
#     print(generate_hashtag2('Codewars Is Nice'))


def first_non_repeating_letter(string):
    """
    Задача 10:
    находит первый неповторяющиеся символ
    """
    for i in string:
        if string.count(i) == 1:
            return i
    return ''


# if __name__ == '__main__':
#     print(first_non_repeating_letter('stress'))


def strip_comments(string, markers):
    """
    Задача 11:
    Разделяет на словарь после одного markers
    strip удаляет определённые символы из заданной строки
    """
    s_list = string.split('\n')
    for marker in markers:
        s_list = [item.split(marker)[0].strip() for item in s_list]
    return '\n'.join(s_list)


# if __name__ == '__main__':
#     print(strip_comments('apples, pears # and bananas\ngrapes\nbananas !apples', ["#", "!"]))

""" ВОТ пример разделения после встречи определённого символа"""


# text = 'some string... this part will be removed.'
# sep = '...'
# stripped = text.split(sep)
# print(stripped)


def make_readable(s):
    """
    Задача 12:
    Секунды переводит в минуты и часы
    Без знания %02d:%02d:%02d подобных конструкций сложно оказывается, надо не забыть разобраться в этой движухе
    divmod делит и возвращает число и остаток от него результат такой же, как (a // b, a % b)
    """
    minutes, seconds = divmod(s, 60)
    hours, minutes = divmod(minutes, 60)
    return '%02d:%02d:%02d' % (hours, minutes, seconds)


# if __name__ == '__main__':
#     print(make_readable(129))


def increment_string(strng):
    """
    Задача 13:
    Ищет число в строке и прибавляет +1 к числу возвращая туже строку только с числом +1
    Если strng = foobar001 должно вернуть foobar002 если foobar то foobar1 и.д
    Не проходит из-за того что в середине строки встречаются цифры
    Плохо читается тем не менее это решение
    isdigit находит числа в строке и возвращает True если они там есть
    """
    string = ''
    numbers = ''
    if strng == '':
        return '1'
    for i in strng:
        if i.isdigit():
            numbers += i
        else:
            string += i
    if numbers == '':
        numbers = '0'
    length = len(numbers)
    return f'{string}{int(numbers) + 1:{0}{length}}'


def increment_string2(strng):
    """
    Задача 13 2 часть:
    rstrip возвращает копию строки с удаленными завершающими символами
    zfill вернет копию строки, у которой начало строки будет заполнено цифрой ASCII 0, до указанной длины width.
    """
    head = strng.rstrip('0123456789')
    tail = strng[len(head):]
    if tail == "":
        return strng + "1"
    return head + str(int(tail) + 1).zfill(len(tail))


# if __name__ == '__main__':
# print(increment_string('foo'))
# print(increment_string2('foof0879'))

# a = '0f2f3f0'
# l = ''
# for i in a:
#     if i.isdigit():
#         l += i
# g = 4
# # Вот пример как можно выводить цифры с 0 впереди если изначально был 0
# print(f'Answer: {int(l):{0}{g}}')


def domain_name(url):
    """
    Задача 14:
    Из url выводит только доменное имя
    Но не работает если точек много, как исправить пока хз
    Но в общем работает
    """
    dot = '.'
    slash = '//'
    # Конструкция как к примеру answer[0:3]
    answer = url[url.find(dot) + len(dot):url.rfind(dot)]
    if answer == '':
        answer = url[url.find(slash) + len(slash):url.rfind(dot)]
    return answer


def domain_name_2(url):
    """
    Задача 14 часть 2:
    Подсмотрел и понял, что замудрил, а всё было под носом.
    Захватывайте только ту часть, которая не является http
    А дальше по накатанной
    """
    return url.split("//")[-1].split("www.")[-1].split(".")[0]


# if __name__ == '__main__':
#     print(domain_name('www.xakep.ru'))
#     print(domain_name('http://vk.com'))
#     print(domain_name('http://www.google.com'))
#     print(domain_name('https://translated.turbopages.org'))
#     # но тут кстати неправильно выводит 2-я часть хоть за это горд
#     print(domain_name_2('https://translated.turbopages.org'))


def find_outlier(integers):
    """
    Задача 15:
    Дается список с числами и только одно из них четное или нет.
    Возвращает то единственное число которое не похоже на остальные если судить по чётности
    """
    evens = [i for i in integers if i % 2 == 0]
    odds = [i for i in integers if i % 2 != 0]
    return odds[0] if len(evens) > len(odds) else evens[0]


# if __name__ == '__main__':
#     print(find_outlier([2, 4, 6, 8, 10, 3]))
#     print(find_outlier([160, 3, 1719, 19, 11, 13, -21]))


def xo(s):
    """
    Задача 16:
    Возвращает True если одинаковое количество x и o в тексте иначе False
    """
    x = 0
    o = 0
    for i in s.lower():
        if 'x' in i:
            x += 1
        elif 'o' in i:
            o += 1
    return x == o


# if __name__ == '__main__':
#     print(xo('zpzpzppx'))


def friend(x):
    """
    Задача 17 lite:
    Ну тут даже объяснять не надо
    """
    l = [i for i in x if len(i) == 4]
    return [s for s in l if not s.isdigit()]


# if __name__ == '__main__':
#     print(friend(["Ryan", "Jimmy", "1234", "4", "Cool Man"]))


def century(year):
    """
    Задача 18:
    Возвращает в каком веке определённый год
    """
    return year // 100 if year % 100 == 0 else year // 100 + 1


# if __name__ == '__main__':
#     print(century(1701))


def spin_words(sentence):
    """
    Задача 19:
    Если длинна слова в тексте >= 5 возвращает reverse этого слова
    """
    return ' '.join([i[::-1] if len(i) >= 5 else i for i in sentence.split(' ')])


# if __name__ == '__main__':
#     print(spin_words('hi koe Welcome toes'))

class Isogram:
    """
    Первый класс
    Задача 20:
    Если строке нет повторяющихся символов, то True else False
    """

    def __init__(self, string):
        self.string = string

    def is_isogram(self):
        return len(self.string) == len(set(self.string.lower()))


# if __name__ == '__main__':
#     dermat = Isogram('Dermatoglyphicss')
#     print(dermat.is_isogram())
#     print(Isogram.is_isogram(dermat))


def solution_multiples(number):
    """
    Задача 21:
    Возвращает сумму всех чисел кратных 3 или 5
    """
    return sum(i for i in range(number) if i % 3 == 0 or i % 5 == 0)


# if __name__ == '__main__':
#     print(solution_multiples(10))

def high_and_low(numbers):
    """
    Задача 22:
    Возвращает самое мин и макс число из строки
    """
    a = [int(i) for i in numbers.split()]
    return f'{max(a)} {min(a)}'


if __name__ == '__main__':
    print(high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4"))
