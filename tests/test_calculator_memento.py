from datetime import datetime
from decimal import Decimal

from app.calculation import Calculation
from app.calculator_memento import CalculatorMemento


def test_memento_serialization_round_trip():
    calculation = Calculation(
        operation="Addition",
        operand1=Decimal("2"),
        operand2=Decimal("3"),
        timestamp=datetime(2025, 1, 2, 3, 4, 5),
    )
    memento = CalculatorMemento(
        history=[calculation],
        timestamp=datetime(2025, 1, 2, 4, 5, 6),
    )

    serialized = memento.to_dict()
    restored = CalculatorMemento.from_dict(serialized)

    assert restored.timestamp == memento.timestamp
    assert restored.to_dict() == serialized
