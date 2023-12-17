def check_password(password):
    with open('passwords.text', 'r') as file:
        common_passwords = file.read().splitlines()
        for i, common_password in enumerate(common_passwords, start=1):
            if password == common_password:
                print(f'❌  (#{i})')
                return
        print('✅  (Unique)')


def main_func():
    user_pass = input("Enter password: ")
    check_password(user_pass)


if __name__ == '__main__':
    main_func()
