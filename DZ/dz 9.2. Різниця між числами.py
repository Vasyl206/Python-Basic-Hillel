
#Вычитаем большое от малого
#Если в numb нчего нет то выдает 0

def difference(*numb):
    if not  numb:
        return 0
    numb_good = round(max(numb) - min(numb), 2) #round округляет с 12.399999 до 12.4
    return numb_good

assert difference(1, 2, 3) == 2, 'Test1'
assert difference(5, -5) == 10, 'Test2'
assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4, 'Test3'
assert difference() == 0, 'Test4'
print('OK')
