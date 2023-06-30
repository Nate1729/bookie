from bookie import models, currency


def calculate_total(receipts: list[models.Receipt]) -> int:
    """Sum the amounts over all reciepts"""
    return sum((r.amount_in_cents for r in receipts))


def find_purchases(receipts: list[models.Receipt]) -> list[models.Receipt]:
    return [r for r in receipts if r.amount_in_cents > 0]


def find_returns(receipts: list[models.Receipt]) -> list[models.Receipt]:
    return [r for r in receipts if r.amount_in_cents < 0]


def print_formatted_line(label: str, value: int | str) -> None:
    print(f"{label:<10}{value:>8}")


def summarize(receipts: list[models.Receipt]) -> None:
    purchases = find_purchases(receipts)
    purchase_total = calculate_total(purchases)

    returns = find_returns(receipts)
    return_total = calculate_total(returns)

    print("----------------")

    print_formatted_line("Purchases", len(purchases))
    print_formatted_line(
        "Total", currency.convert_cents_to_dollar_string(purchase_total)
    )

    print("\n")

    print_formatted_line("Returns", len(returns))
    print_formatted_line("Total", currency.convert_cents_to_dollar_string(return_total))
