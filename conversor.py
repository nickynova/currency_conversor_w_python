def foreign_exchange_calculator(amount, main_currency, foreign_currency):
    mxn_to_cop_rate = 179.79
    mxn_to_usd_rate = 0.048
    cop_to_mxn_rate = 0.0057
    cop_to_usd_rate = 0.00027
    usd_to_cop_rate = 3676
    usd_to_mxn_rate = 21.01
    
    if main_currency == 'mxn' and foreign_currency == 'cop':
        return mxn_to_cop_rate * amount
    elif main_currency == 'mxn' and foreign_currency == 'usd':
        return mxn_to_usd_rate * amount
    elif main_currency == 'cop' and foreign_currency == 'mxn':
        return cop_to_mxn_rate * amount 
    elif main_currency == 'cop' and foreign_currency == 'usd':
        return cop_to_usd_rate * amount 
    elif main_currency == 'usd' and foreign_currency == 'mxn':
        return usd_to_mxn_rate * amount 
    elif main_currency == 'usd' and foreign_currency == 'cop':
        return usd_to_cop_rate * amount 
   

def run():
    print('welcome to the foreign exchange calculator! ')
    print('please insert the amount you want to convert and then the and the currency: ')
    print('insert the Currency as its short form ex: cop, usd, mxn')
    print('')

    amount = float(input('insert the amount: '))

    main_currency = input('insert your currency: ')

    foreign_currency = input('insert the currency you want to convert to: ')

    result = foreign_exchange_calculator(amount, main_currency, foreign_currency)

    print('${} ' + foreign_currency + ' is ' + '${} ' + main_currency.format(amount, result))


if __name__ == "__main__":
    run()