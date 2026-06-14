import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

def deterministic_signal(hist):
    """
    Generate trading signal using SMA crossover + volatility.
    """
    sma_7 = hist["Close"].rolling(7).mean().iloc[-1]
    sma_30 = hist["Close"].rolling(30).mean().iloc[-1]
    volatility = hist["Close"].pct_change().std()

    if sma_7 > sma_30 and volatility < 0.03:
        return "BUY"
    elif sma_7 < sma_30 and volatility > 0.02:
        return "SELL"
    else:
        return "HOLD"



def plot_results(df, stock_symbol):

    # ----- Equity Curve -----
    plt.figure(figsize=(10,5))
    plt.plot(df["date"], df["equity"])
    plt.title(f"{stock_symbol} Equity Curve")
    plt.xlabel("Date")
    plt.ylabel("Portfolio Value")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("equity_curve.png")
    plt.close()

    # ----- Drawdown -----
    rolling_max = df["equity"].cummax()
    drawdown = (df["equity"] - rolling_max) / rolling_max

    plt.figure(figsize=(10,5))
    plt.plot(df["date"], drawdown)
    plt.title(f"{stock_symbol} Drawdown")
    plt.xlabel("Date")
    plt.ylabel("Drawdown")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("drawdown.png")
    plt.close()

    # ----- Trading Signals -----
    plt.figure(figsize=(12,6))
    plt.plot(df["date"], df["current_price"], label="Price")

    buy = df[df["decision"] == "BUY"]
    sell = df[df["decision"] == "SELL"]

    plt.scatter(buy["date"], buy["current_price"], marker="^", label="BUY")
    plt.scatter(sell["date"], sell["current_price"], marker="v", label="SELL")

    plt.legend()
    plt.title(f"{stock_symbol} Trading Signals")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("trading_signals.png")
    plt.close()




def backtest(stock_symbol="TSLA", days=30):
    stock = yf.Ticker(stock_symbol)
    hist = stock.history(period="6mo")

    hist = hist.tail(days + 5)

    results = []

    for i in range(days):
        current_date = hist.index[i]
        future_date = hist.index[i + 5]

        hist_until_today = hist.iloc[:i+1]

        if len(hist_until_today) < 30:
            continue

        decision = deterministic_signal(hist_until_today)

        current_price = hist["Close"].iloc[i]
        future_price = hist["Close"].iloc[i + 5]

        pct_change = (future_price - current_price) / current_price

        if decision == "BUY":
            strategy_return = pct_change
        elif decision == "SELL":
            strategy_return = -pct_change
        else:
            strategy_return = 0

        results.append({
            "date": current_date,
            "decision": decision,
            "current_price": current_price,
            "future_price": future_price,
            "return": strategy_return
        })

    df = pd.DataFrame(results)

    # ----- METRICS -----

    accuracy = (df["return"] > 0).mean()
    avg_return = df["return"].mean()
    win_rate = (df["return"] > 0).sum() / len(df)
    sharpe = df["return"].mean() / df["return"].std()

    df["equity"] = (1 + df["return"]).cumprod()

    print("------ BACKTEST RESULTS ------")
    print(f"Accuracy: {round(accuracy*100,2)}%")
    print(f"Average Return: {round(avg_return*100,2)}%")
    print(f"Win Rate: {round(win_rate*100,2)}%")
    print(f"Sharpe Ratio: {round(sharpe,2)}")

    plot_results(df, stock_symbol)

    return df

if __name__ == "__main__":
    backtest("TSLA", days=60)

