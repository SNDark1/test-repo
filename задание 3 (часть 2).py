def is_valid_password(password):
    if len(password) < 8:
        return False
    has_lowercase = any(char.islower()for char in password)
    has_uppercase = any(char.isupper()for char in password)
    return has_lowercase and has_uppercase
while True:
    password = input('Введите пароль')
    if is_valid_password(password):
        print('Пароль принят')
        break
    else:
        print('Недопустимый пароль')