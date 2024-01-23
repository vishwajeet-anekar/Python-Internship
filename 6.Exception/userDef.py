class NegativenumberException(Exception):
    pass

try:
    a = int(input('enter any nubmer '))
    if a <0:
        raise NegativenumberException('hh')
    
    print(a**3)
except NegativenumberException as e:
    print(e)
