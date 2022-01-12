def paly():
    name = input('enter your name : ')
    print('Your name is : ' + reverse_name(name))

def reverse_name(name):
    return name[::-1]

paly()