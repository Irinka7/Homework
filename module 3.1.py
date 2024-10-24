calls = 0
def count_calls ():
    global calls
    calls += 1


def string_info (string):
    count_calls()
    return len(string) , string.upper() , string.lower()


flag_ = 0

def is_contains (str , lst):
    count_calls()
    global flag_
    for i in range(len(lst)):
        if str.lower() == lst[i].lower():
            flag_ = 1
        else:
            continue
    if flag_ == 1:
        flag_ = 0
        return True
    else:
        return False


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)