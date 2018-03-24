import account

usd = 57
euro = 69
pound = 78
jpy = 0.52

def main():
    rate = int(input('Введите процентную ставку:'))
    money= int(input('Введите сумму в рублях:'))
    period= int(input('Введите период ведения счёта в месяцах:'))
    currency=int(input('Укажите код валюты (доллары - 400, евро - 401, фунт - 402, йена - 403):'))

    if currency==400:
        money=round(money/usd,2)
        print('Валюта: доллары сша')
    elif currency==401:
        money=round(money/euro,2)
        print('Валюта: евро')
    elif currency==402:
        money=round(money/pound,2)
        print('Валюта: фунт')
    elif currency==403:
        money=round(money/jpy,2)
        print('Валюта: йена')
    else:
        money=0
        print('Неизвестная валюта')

    result=account.calculate_income(rate,money,period)
    print('Параметры счёта:\n','Сумма:', money, '\n', 'Ставка:', rate, '\n', 'Период:', period,'\n', 'Сумма на счёте в конце периода:',result,)

if __name__ == '__main__':
    main()