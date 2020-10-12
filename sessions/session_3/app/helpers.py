def __get_factor_list(number):
    '''
    Takes an pos integer number and returns its factors as a list.

    Hint: This is a private method that helps with calculating the
          aliquot sum.
    '''
    factor_list = []
    for dividend in range(1, number):
        if number % dividend == 0:
            factor_list.append(dividend)
    return factor_list


def get_aliquot_sum(number):
    '''
    Takes an pos integer number and returns its aliquot sum.
    More info: https://en.wikipedia.org/wiki/Aliquot_sum
    '''
    factor_list = __get_factor_list(number)
    aliquot_sum = sum(factor_list)

    return aliquot_sum
