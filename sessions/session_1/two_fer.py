def two_fer_basic() -> str:
    '''The basic two-fer functionality.

    Input:
        name : str [optional]
            The name of the person to share with, e.g. Tony

    Returns:
        str
            If name given return: One for {name}, one for me.
            If no name is given, return: One for you, one for me.
    '''
    pass


def two_fer_multiple():
    '''The functionality of two-fer extended to return more than one.

    Input:
        name : str [optional]
            The name of the person to share with, e.g. Bruce

        amount : str [optional]
            The amount of pieces to share, e.g. fifty

    Returns:
        str
            The sentence: {amount} for {name}, {amount} for me.
            If no name is given, return: {amount} for you, {amount} for me.
            If no amount is given, return: One for {name}, one for me.
            If none of the values are passed, return: One for you, one for me.
    '''
    pass


def two_fer_multiple_assign():
    '''The functionality of two-fer extended to return more than one.

    Input:
        name : str [optional]
            The name of the person to share with, e.g. Steve

        share : (str, str) [optional]
            A tuple of the shared amount, e.g. (one, three)

    Returns:
        str
            The sentence: {share[0]} for {name}, {share[1]} for me.
            If no name is given, return: {share[0]} for you, {share[1]} for me.
            If no amount is given, return: One for {name}, one for me.
            If none of the values are passed, return: One for you, one for me.
    '''
    pass
