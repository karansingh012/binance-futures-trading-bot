# Binance Futures Testnet Trading Bot

A Python-based trading bot that places Market and Limit orders on the Binance Futures Testnet (USDT-M).  
The application supports BUY/SELL operations through a command-line interface with proper validation, logging, and error handling.

---

## Project Structure

```
binance-futures-trading-bot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   └── logging_config.py
│
├── logs/
│   └── trading_bot.log
│
├── cli.py
├── .env.example
├── requirements.txt
└── README.md
```

---

## Features

- Place MARKET and LIMIT orders
- Supports BUY and SELL sides
- Binance Futures Testnet integration
- CLI-based user interaction
- Input validation
- Structured logging
- Error handling for API and network failures

---

## Setup Instructions

### Step 1: Clone Repository

```bash
git clone https://github.com/yourusername/binance-futures-trading-bot.git
cd binance-futures-trading-bot
```

### Step 2: Create virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Step 3: Install dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Setup environment variables

```bash
cp .env.example .env
```

Edit `.env` and add your Testnet API keys:

```
BINANCE_API_KEY=your_api_key
BINANCE_API_SECRET=your_api_secret
```

---

## How to Get Binance Testnet API Keys

1. Go to https://testnet.binancefuture.com
2. Click "Login with GitHub"
3. Click "Generate HMAC_SHA256 Key" button
4. Copy the API Key and Secret Key
5. Paste them in your `.env` file

> These are Testnet keys only — no real money involved!

---

## How to Run

### Market Order (BUY)

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01
```

### Market Order (SELL)

```bash
python cli.py --symbol BTCUSDT --side SELL --type MARKET --quantity 0.01
```

### Limit Order (BUY)

```bash
python cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.01 --price 60000
```

### Limit Order (SELL)

```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.01 --price 85000
```

---

## CLI Options

| Option | Required | Description | Example |
|--------|----------|-------------|---------|
| `--symbol` | Yes | Trading pair | `BTCUSDT` |
| `--side` | Yes | BUY or SELL | `BUY` |
| `--type` | Yes | MARKET or LIMIT | `MARKET` |
| `--quantity` | Yes | Amount to trade | `0.01` |
| `--price` | LIMIT only | Order price | `60000` |

---

## Sample Output

```
Order summary:
  Symbol:   BTCUSDT
  Side:     BUY
  Type:     MARKET
  Quantity: 0.01

Order placed successfully!
  orderId:     13119943659
  status:      NEW
  executedQty: 0.0000
  avgPrice:    0.00
```

---

## Logging

All activity is automatically saved to `trading_bot.log`:

- Every order request
- Every order response
- All errors and exceptions

---

## Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.x | Core language |
| requests | REST API calls |
| Typer | CLI interface |
| python-dotenv | Environment variables |
| logging | Log to file and console |

---

## Assumptions

- This bot only works with Binance Futures Testnet
- No real money is used at any point
- Testnet may have limited liquidity so orders may show NEW status
- API keys from real Binance will not work here

---

## Author

Made as part of Primetrade.ai Python Developer Internship Assignment.