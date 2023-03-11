import models, currency

def calculate_total(receipts: list[models.Receipt]) -> int:
    """Sum the amounts over all reciepts"""
    return sum((r.amount_in_cents for r in receipts))

def find_purchases(receipts: list[models.Receipt]) -> list[models.Receipt]:
    return [r for r in receipts if r.amount_in_cents > 0]

def find_returns(receipts: list[models.Receipt]) -> list[models.Receipt]:
    return [r for r in receipts if r.amount_in_cents < 0]

def summarize(receipts: list[models.Receipt]) -> None:
    purchases = find_purchases(receipts)
    returns = find_returns(receipts)
    purchase_total = calculate_total(purchases)
    return_total = calculate_total(returns)
    

    print('----------------')
    print(f'Purchases {len(purchases):>8}')
    print(f'Total    {currency.convert_cents_to_str(purchase_total):>8}\n')

    print(f'Returns   {len(returns):>8}')
    print(f'Total     {currency.convert_cents_to_str(return_total):>8}')
