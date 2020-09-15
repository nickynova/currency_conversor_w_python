def foreign_exchange_calculator(amount):
    mexc_to_cop_rate = 145.97

    return mexc_to_cop_rate * amount


def run():
    print('welcome to the foreign exchange calculator! ')
    print('you can convert MXC to COP')
    print('')

    amount = float(input('insert the amount of MXC you want to convert: '))

    result = foreign_exchange_calculator(amount)

    print('${} mexican pesos is ${} colombian pesos'.format(amount, int(result)))


if __name__ == "__main__":
    run()