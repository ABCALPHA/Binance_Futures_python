class SymbolBookTickerEvent:

    def __init__(self):
        self.eventType = ""
        self.eventTime = 0
        self.transactionTime = 0
        self.orderBookUpdateId = None
        self.symbol = ""
        self.bestBidPrice = 0.0
        self.bestBidQty = 0.0
        self.bestAskPrice = 0.0
        self.bestAskQty = 0.0

    @staticmethod
    def json_parse(json_wrapper):
        ticker_event = SymbolBookTickerEvent()
        ticker_event.eventType = json_wrapper.get_string("e")
        ticker_event.eventTime = json_wrapper.get_int("E")
        ticker_event.transactionTime = json_wrapper.get_int("T")
        ticker_event.orderBookUpdateId = json_wrapper.get_int("u")
        ticker_event.symbol = json_wrapper.get_string("s")
        ticker_event.bestBidPrice = json_wrapper.get_float("b")
        ticker_event.bestBidQty = json_wrapper.get_float("B")
        ticker_event.bestAskPrice = json_wrapper.get_float("a")
        ticker_event.bestAskQty = json_wrapper.get_float("A")
        return ticker_event
    
    @staticmethod
    def to_json_wrapper(json_wrapper):
        return json_wrapper