"""Binance Futures Testnet client wrapper using direct REST API."""

import hashlib
import hmac
import os
import time
from typing import Any
from urllib.parse import urlencode

import requests
from dotenv import load_dotenv

from .logging_config import setup_logging

BASE_URL = "https://testnet.binancefuture.com"

class BinanceClient:
    """Manage Binance Futures Testnet connection via direct REST API."""

    def __init__(self) -> None:
        self.logger = setup_logging()
        load_dotenv()

        self.api_key = os.getenv("BINANCE_API_KEY")
        self.api_secret = os.getenv("BINANCE_API_SECRET")

        if not self.api_key or not self.api_secret:
            self.logger.error("Missing BINANCE_API_KEY or BINANCE_API_SECRET.")
            raise ValueError("Missing BINANCE_API_KEY or BINANCE_API_SECRET.")

        self._test_connection()

    def _sign(self, params: dict) -> str:
        """Generate HMAC SHA256 signature."""
        query = urlencode(params)
        signature = hmac.new(
            self.api_secret.encode("utf-8"),
            query.encode("utf-8"),
            hashlib.sha256
        ).hexdigest()
        return signature

    def _headers(self) -> dict:
        return {"X-MBX-APIKEY": self.api_key}

    def _test_connection(self) -> None:
        """Ping testnet to verify connectivity."""
        try:
            r = requests.get(f"{BASE_URL}/fapi/v1/ping", timeout=10)
            r.raise_for_status()
            self.logger.info("Connected to Binance Futures Testnet.")
        except Exception as exc:
            self.logger.error("Connection test failed: %s", exc)
            raise

    def place_order(self, **params: Any) -> dict:
        """Place a futures order with signed request."""
        try:
            params["timestamp"] = int(time.time() * 1000)
            params["signature"] = self._sign(params)

            self.logger.info("Sending order request: %s", params)

            r = requests.post(
                f"{BASE_URL}/fapi/v1/order",
                headers=self._headers(),
                params=params,
                timeout=10
            )

            response = r.json()
            self.logger.info("Order response: %s", response)

            if "code" in response and response["code"] != 200:
                raise Exception(f"API Error {response['code']}: {response.get('msg')}")

            return response

        except Exception as exc:
            self.logger.error("Order failed: %s", exc)
            raise