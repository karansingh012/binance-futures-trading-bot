"""Order placement helpers."""

from typing import Any, Dict

from .client import BinanceClient
from .logging_config import setup_logging


class OrderManager:
    """Place and manage Binance Futures orders via the REST client."""

    def __init__(self, client: BinanceClient) -> None:
        """Store the client and prepare logging."""
        self.client = client
        self.logger = setup_logging()

    def place_market_order(self, symbol: str, side: str, quantity: float) -> Dict[str, Any]:
        """Place a MARKET order and return key order details."""
        try:
            params = {
                "symbol": symbol,
                "side": side,
                "type": "MARKET",
                "quantity": quantity,
            }
            self.logger.info("Placing MARKET order: %s", params)
            response = self.client.place_order(**params)
            self.logger.info("Order response: %s", response)
            return self._extract_order_details(response)
        except Exception as exc:
            self.logger.error("Market order failed: %s", exc)
            raise

    def place_limit_order(
        self, symbol: str, side: str, quantity: float, price: float
    ) -> Dict[str, Any]:
        """Place a LIMIT order and return key order details."""
        try:
            params = {
                "symbol": symbol,
                "side": side,
                "type": "LIMIT",
                "quantity": quantity,
                "price": price,
                "timeInForce": "GTC",
            }
            self.logger.info("Placing LIMIT order: %s", params)
            response = self.client.place_order(**params)
            self.logger.info("Order response: %s", response)
            return self._extract_order_details(response)
        except Exception as exc:
            self.logger.error("Limit order failed: %s", exc)
            raise

    def _extract_order_details(self, response: Dict[str, Any]) -> Dict[str, Any]:
        """Extract and normalize key fields from the order response."""
        return {
            "orderId": response.get("orderId"),
            "status": response.get("status"),
            "executedQty": response.get("executedQty"),
            "avgPrice": response.get("avgPrice"),
        }