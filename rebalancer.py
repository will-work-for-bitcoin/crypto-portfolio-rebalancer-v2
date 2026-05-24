#!/usr/bin/env python3
"""
Crypto Portfolio Rebalancer - Track and rebalance crypto portfolios
Supports multiple assets and rebalancing strategies

BTC Tips: 1KPUa9Njq86NJwmwqVmdjZ4oC8eHrXKqf9
"""
import json
import urllib.request
import sys
from datetime import datetime

def get_portfolio(prices):
    """Calculate current portfolio allocation"""
    portfolio = {
        'BTC': 0.5,
        'ETH': 0.2,
        'SOL': 0.1,
        'XRP': 0.1,
        'USDC': 0.1,
    }
    
    total_value = sum(amt * prices.get(coin.lower(), {}).get('usd', 0) for coin, amt in portfolio.items())
    
    print("=" * 70)
    print("CRYPTO PORTFOLIO REBALANCER")
    print(f"Updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 70)
    
    print(f"\n{'Asset':<8} {'Amount':>10} {'Value':>12} {'Allocation':>12} {'Target':>10} {'Action':>10}")
    print("-" * 65)
    
    for coin, amount in portfolio.items():
        price = prices.get(coin.lower(), {}).get('usd', 0)
        value = amount * price
        allocation = (value / total_value * 100) if total_value > 0 else 0
        target = portfolio[coin] * 100
        
        if allocation > target * 1.1:
            action = "SELL"
        elif allocation < target * 0.9:
            action = "BUY"
        else:
            action = "HOLD"
        
        print(f"{coin:<8} {amount:>10.4f} ${value:>10.2f} {allocation:>10.1f}% {target:>8.1f}% {action:>10}")
    
    print(f"\nTotal Portfolio Value: ${total_value:,.2f}")
    print(f"\nBTC Tips: 1KPUa9Njq86NJwmwqVmdjZ4oC8eHrXKqf9")

def main():
    try:
        url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin%2Cethereum%2Csolana%2Cripple%2Cusd-coin&vs_currencies=usd"
        req = urllib.request.Request(url, headers={'Accept': 'application/json'})
        with urllib.request.urlopen(req, timeout=10) as response:
            prices = json.loads(response.read())
        get_portfolio(prices)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()
