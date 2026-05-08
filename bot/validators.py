"""Validation helpers for orders and inputs."""


def validate_symbol(symbol: str) -> str:
    """Validate that the symbol is a non-empty uppercase string."""
    if not isinstance(symbol, str) or not symbol.strip():
        raise ValueError("Symbol must be a non-empty string.")
    if symbol != symbol.upper():
        raise ValueError("Symbol must be uppercase, for example BTCUSDT.")
    return symbol


def validate_side(side: str) -> str:
    """Validate that side is BUY or SELL."""
    if side not in {"BUY", "SELL"}:
        raise ValueError("Side must be BUY or SELL.")
    return side


def validate_order_type(order_type: str) -> str:
    """Validate that order type is MARKET or LIMIT."""
    if order_type not in {"MARKET", "LIMIT"}:
        raise ValueError("Order type must be MARKET or LIMIT.")
    return order_type


def validate_quantity(quantity: float) -> float:
    """Validate that quantity is a positive number."""
    try:
        qty = float(quantity)
    except (TypeError, ValueError) as exc:
        raise ValueError("Quantity must be a positive number.") from exc

    if qty <= 0:
        raise ValueError("Quantity must be a positive number.")
    return qty


def validate_price(price: float | None, order_type: str) -> float | None:
    """Validate price for LIMIT orders and allow None for MARKET."""
    if order_type == "LIMIT":
        if price is None:
            raise ValueError("Price is required for LIMIT orders.")
        try:
            parsed_price = float(price)
        except (TypeError, ValueError) as exc:
            raise ValueError("Price must be a positive number.") from exc
        if parsed_price <= 0:
            raise ValueError("Price must be a positive number.")
        return parsed_price

    return None
