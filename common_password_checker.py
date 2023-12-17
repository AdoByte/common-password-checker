def check_password(password):
    with open('passwords.text', 'r') as file:
        common_passwords = file.read().splitlines()
        for i, common_password in enumerate(common_passwords, start=1):
            if password == common_password():
                print(f'❌  (#{i})')
                return
        print('✅  (Unique)')
