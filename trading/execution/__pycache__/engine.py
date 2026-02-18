from hashing.modules.hash_utils import generate_hash


def execute_trade(signal):

    trade_event = {
        "event": "trade",
        "symbol": "EURUSD",
        "side": signal,
        "qty": 1,
        "price": 1.0850
    }

    trade_hash = generate_hash(trade_event)

    print("Trade ejecutado:")
    print(trade_event)

    print("\nHash del trade:")
    print(trade_hash)

    return trade_event, trade_hash
