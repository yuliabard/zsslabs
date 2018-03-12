usd=57
euro=69
pound=78
jpy=0.52

money=int(input('Введите сумму, которую вы хотите обменять): '))
currency=int(input('Укажите код валюты (доллары - 400, евро - 401, фунт - 402, йена - 403): '))

if currency==400:
    cache=round(money/usd,2)
    print('Валюта: доллары сша')
elif currency==401:
    cache=round(money/euro,2)
    print('Валюта: евро')
elif currency==402:
    cache=round(money/pound,2)
    print('Валюта: фунт')
elif currency==403:
    cache=round(money/jpy,2)
    print('Валюта: йена')
else:
    cache=0
    print('Неизвестная валюта')
print('К получению ',cache)