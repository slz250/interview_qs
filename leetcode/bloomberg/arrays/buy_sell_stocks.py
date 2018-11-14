class StockUtils(object):
    def __init__(self):
        self.final_max = 0

    def best_buy_sell(self, prices):
        #reduce unnecessary computations that lead to negative profits
        def driver(prev_cut, curr_max):
            if dp_mem[prev_cut]:
                return dp_mem[prev_cut]

            if prev_cut == len(prices):
                self.final_max = curr_max if curr_max > self.final_max else self.final_max
                dp_mem[prev_cut] = curr_max
                return curr_max

            for i in range(prev_cut+1, len(prices)):
                buy = prices[i]
                local_max = 0
                sell_cut = i
                for j in range(i+1, len(prices)):
                    sell = prices[j]
                    profit = buy - sell
                    if profit > local_max:
                        local_max = profit
                        sell_cut = j
                temp_max = driver(sell_cut, curr_max+local_max)
                func_max = 0
                func_max = temp_max if temp_max > func_max else func_max

            return func_max

        dp_mem = [None for i in range(len(prices))]
        return driver(0, 0)

    """
    b/c it is only one stock
    we buy and hold as long as the price increases
    sell just before it starts decreasing
    we never buy if the next price is smaller
    
    four cases:
    inc dec //sell before dec
    inc //sell @ end
    dec inc //buy just before inc
    dec  //never buy
    
    -think big picture --> try to not get too stressed over
    logic hiccups
    -notice patterns
    """
    def maxProfit(self, prices):
        total = 0
        for i in range(len(prices)-1):
            if prices[i+1] > prices[i]:
                total += prices[i+1]-prices[i]
        return total