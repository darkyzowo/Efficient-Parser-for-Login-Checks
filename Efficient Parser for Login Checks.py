# Efficient Parsing Algorithm

#Foundation of our Parsing Algorithm
with open('failed_logins', 'r') as file:
    file_text = file.read()
username = file_text.split()

def login_checker(login_list, current_user):
    login_counter = {}
    for username in login_list:
        if username in login_counter:
            login_counter[username] += 1
        else:
            login_counter[username] = 1

 # Check if the current user has 3 or more failed attempts
    if login_counter.get(current_user, 0) >= 3: #To get the count attempts for the failed user, defaults to zero if user not found
        return (
            'Your account has been locked, you cannot login for the next 24 hours.',
            f' > Login attempt failures = {login_counter[current_user]}'
        )
    else:
        remaining_attempts = 3 - login_counter.get(current_user, 0)
        return (
            f'You can still login. You have {remaining_attempts} attempts left.'
        )

print(login_checker(username, 'asmith'))
