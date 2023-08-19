
def first_func():
    sec_func()
    print('Im the first method')
def sec_func():
    third_func()
    print('Im the second method')
def third_func():
    fourth_func()
    print('Im the third method')
def fourth_func():
    fifth_func()
    print('Im the fourth method')
def fifth_func():
    print('Im the fifth method')



first_func()