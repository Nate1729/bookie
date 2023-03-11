from typing import Any
from dataclasses import dataclass
from datetime import datetime

import models, currency

@dataclass
class Receipt:
    date: datetime
    vendor: str
    amount_in_cents: int

def receipt_from_dict(data: dict[str, Any]) -> models.Receipt:
    DATE_FMT = '%Y-%m-%d %H:%M:%S';
    return Receipt(
        date=datetime.strptime(data['date'], DATE_FMT),
        vendor=data['vendor'],
        amount_in_cents=currency.convert_str_to_cents(data['amount'])
    )


