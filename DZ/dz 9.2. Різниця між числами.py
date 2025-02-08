
#Вычитаем большое от малого
#Если в numb нчего нет то выдает 0

def difference(*numb):
    if not  numb:
        return 0
    numb_good = round(max(numb) - min(numb), 2) #round округляет с 12.399999 до 12.4
    return numb_good

print(difference())
