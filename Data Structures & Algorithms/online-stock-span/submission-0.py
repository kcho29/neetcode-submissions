class StockSpanner:

    def __init__(self):
        self.priceList = []

    def next(self, price: int) -> int:
        out = 0
        self.priceList.append(price)
        for p in self.priceList[::-1]:
            if p <= price:
                out += 1
            else:
                break
        return out


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)