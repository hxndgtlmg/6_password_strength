import math
import string


def entropy(line):
    entropy = 0
    if not line:
        return entropy
    for x in (ord(c) for c in string.printable):
        p_x = float(line.count(chr(x)))/len(line)
        if p_x > 0:
            entropy += - p_x*math.log(p_x, 2)
    return int(entropy)


def get_password_strength(password):
    special_characters = list(' !"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~')
    worst_pattern = ['1234', 'password', 'qwer', 'abc',
                     '1111', '1qaz', 'login']
    password_strength = 1

    if any(pattern in password for pattern in worst_pattern):
        return password_strength
    else:
        password_strength += 1

    entropy_strength = entropy(password) - 2
    if entropy_strength <= 2:
        if entropy_strength < 0:
            entropy_strength = 0
        password_strength += entropy_strength
    else:
        password_strength += 2

    if len(password) >= 8:
        password_strength += 1
    if any(char in password for char in string.ascii_lowercase):
        password_strength += 1
    if any(char in password for char in string.ascii_uppercase):
        password_strength += 1
    if any(char in password for char in string.digits):
        password_strength += 1
    if any(char in password for char in special_characters):
        password_strength += 2

    return password_strength

if __name__ == '__main__':
    print('Сложность пароля: {0}/10'.format(get_password_strength(
        input('Введите свой пароль: '))))
