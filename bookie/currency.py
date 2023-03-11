def convert_str_to_cents(amount: str, cent_separator: str='.') -> int:
    """Convert a string of currency into dollars.
    Does **NOT** support commas!!
    """

    if cent_separator not in amount:
        return int(amount)

    dollars, cents = amount.split(cent_separator)

    if len(cents) != 2:
        raise ValueError("cents should be a two digit number")

    return int(dollars + cents)

def _apply_sign(amount: str, is_negative: bool) -> str:
    """formats the amount a positive or negative.
    Negative values in accounting are denoted by
    wrapping () around the value, **NOT** with 
    a - sign.
    """
    return f'({amount})' if is_negative else amount

def convert_cents_to_str(cents: int, cent_separator: str='.', currency_marker: str='$') -> str:

    dollars = cents // 100 # integer division
    cents = cents % 100
    
    return currency_marker + _apply_sign(f'{dollars}{cent_separator}{cents}', cents < 0)

