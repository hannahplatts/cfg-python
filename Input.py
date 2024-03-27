email = input('Email:')
email_true = email == 'hannahplatts@gmail.com'

password = input('Password:')
password_true = password == 'hellokitty'

if password_true and email_true:
    print('Welcome!')
else:
    print('Wrong username or password.')


