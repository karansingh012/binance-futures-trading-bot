"""Command line interface for placing orders."""

import typer

from bot import BinanceClient, OrderManager
from bot.logging_config import setup_logging
from bot.validators import (
    validate_order_type,
    validate_price,
    validate_quantity,
    validate_side,
    validate_symbol,
)

app = typer.Typer(help="Binance Futures Testnet trading bot CLI.")
logger = setup_logging()


@app.command()
def place_order(
    symbol: str = typer.Option(..., "--symbol", help="Trading symbol, e.g. BTCUSDT."),
    side: str = typer.Option(..., "--side", help="Order side: BUY or SELL."),
    order_type: str = typer.Option(
        ..., "--type", help="Order type: MARKET or LIMIT."
    ),
    quantity: float = typer.Option(..., "--quantity", help="Order quantity."),
    price: float | None = typer.Option(None, "--price", help="Limit price."),
) -> None:
    """Validate inputs, place the order, and display results."""
    try:
        symbol = validate_symbol(symbol)
        side = validate_side(side)
        order_type = validate_order_type(order_type)
        quantity = validate_quantity(quantity)
        price = validate_price(price, order_type)

        typer.echo("Order summary:")
        typer.echo(f"  Symbol: {symbol}")
        typer.echo(f"  Side: {side}")
        typer.echo(f"  Type: {order_type}")
        typer.echo(f"  Quantity: {quantity}")
        if price is not None:
            typer.echo(f"  Price: {price}")

        client = BinanceClient()
        manager = OrderManager(client)

        if order_type == "MARKET":
            result = manager.place_market_order(symbol, side, quantity)
        else:
            result = manager.place_limit_order(symbol, side, quantity, price)

        typer.echo("Order placed successfully.")
        typer.echo("Order response:")
        typer.echo(f"  orderId: {result.get('orderId')}")
        typer.echo(f"  status: {result.get('status')}")
        typer.echo(f"  executedQty: {result.get('executedQty')}")
        typer.echo(f"  avgPrice: {result.get('avgPrice')}")
    except Exception as exc:
        logger.error("CLI order failed: %s", exc)
        typer.echo(f"Order failed: {exc}")
        raise typer.Exit(code=1)


if __name__ == "__main__":
    app()
