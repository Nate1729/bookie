from typing import Any
from dataclasses import dataclass
from datetime import datetime

from bookie import currency

DATE_FMT = '%Y-%m-%d %H:%M:%S'

class MissingDataException(Exception):
    pass

@dataclass
class Receipt:
    date: datetime
    vendor: str
    amount_in_cents: int

def receipt_from_dict(data: dict[str, Any]) -> Receipt:
    """From a dictionary construct the
    Receipt dataclass.
    """
    # Data Validation
    if (date := data.get("date")) is None:
        raise MissingDataException("date not found!")
    if (vendor := data.get("vendor")) is None:
        raise MissingDataException("vendor not found!")
    if (amount := data.get("amount")) is None:
        raise MissingDataException("amount not found!")
    

    return Receipt(
        date=datetime.strptime(date, DATE_FMT),
        vendor=vendor,
        amount_in_cents=currency.convert_str_to_cents(amount)
    )


