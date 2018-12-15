class StockUtils(object):
    def __init__(self):
        self.final_max = 0

    def best_buy_sell(self, prices):
        # reduce unnecessary computations that lead to negative profits
        def driver(prev_cut, curr_max):
            if dp_mem[prev_cut]:
                return dp_mem[prev_cut]

            if prev_cut == len(prices):
                self.final_max = curr_max if curr_max > self.final_max else self.final_max
                dp_mem[prev_cut] = curr_max
                return curr_max

            for i in range(prev_cut + 1, len(prices)):
                buy = prices[i]
                local_max = 0
                sell_cut = i
                for j in range(i + 1, len(prices)):
                    sell = prices[j]
                    profit = buy - sell
                    if profit > local_max:
                        local_max = profit
                        sell_cut = j
                temp_max = driver(sell_cut, curr_max + local_max)
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
        for i in range(len(prices) - 1):
            if prices[i + 1] > prices[i]:
                total += prices[i + 1] - prices[i]
        return total

    def calculate(self, prices, s):
        if s >= len(prices):
            return 0
        max_ = 0
        for start in range(len(prices)):
            maxprofit = 0
            for i in range(start + 1, prices.length):
                if prices[start] < prices[i]:
                    profit = self.calculate(prices, i + 1) + prices[i] - \
                             prices[start]
                    if profit > maxprofit:
                        maxprofit = profit
            if maxprofit > max_:
                max_ = maxprofit

        return max_

    def maxProfit(self, prices):
        i = 0
        valley, peak = prices[0], prices[0]
        maxprofit = 0
        while i < prices.length - 1:
            while i < prices.length - 1 and prices[i] >= prices[i + 1]:
                i += 1
            valley = prices[i]
            while i < prices.length - 1 and prices[i] <= prices[i + 1]:
                i += 1
            peak = prices[i]
            maxprofit += peak - valley
        return maxprofit

    def maxProfit1(self, prices):
        maxprofit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                maxprofit += prices[i] - prices[i - 1]
        return maxprofit

    """
    buy and hold on until price drops then sell
    but when do we buy?
    buy just at/before it's going up

    """

    def maxProfit2(self, prices):
        if not prices or len(prices) == 1:
            return 0
        profit = 0
        buy_date = -1
        for i in range(len(prices) - 1):
            #inc and hasnt been set
            if prices[i] - prices[i + 1] < 0 and buy_date == -1:
                buy_date = i
            #dec and has been set
            elif prices[i] - prices[i + 1] > 0 and buy_date != 1:
                sell_date = i
                profit += (prices[sell_date] - prices[buy_date])
                # print(
                #     f'prices[sell_date({sell_date})] = {prices[sell_date]} prices[buy_date({buy_date})]: {prices[buy_date]}\n'
                #     f'curr_profit = {prices[sell_date]-prices[buy_date]}\n'
                #     f'total_profit = {profit}\n')
                buy_date = -1
        if buy_date != -1:
            # print('edge case:')
            sell_date = len(prices)-1
            profit += (prices[sell_date] - prices[buy_date])
            # print(
            #     f'prices[sell_date({sell_date})] = {prices[sell_date]} prices[buy_date({buy_date})]: {prices[buy_date]}\n'
            #     f'curr_profit = {prices[sell_date]-prices[buy_date]}\n'
            #     f'total_profit = {profit}\n'
            # )
        return profit

    def maxProfit3(self, prices):
        """
        essentially all we need to do is to add up the positive slope parts
        of our graph
        we don't need to keep track of buy and sell points
        """
        if not prices or len(prices) == 1:
            return 0
        profit = 0
        for i in range(len(prices)-1):
            if prices[i] - prices[i+1] < 0:
                profit += (prices[i+1] - prices[i])
        return profit


if __name__ == '__main__':
    sol = StockUtils()
    prices = [1, 2, 3, 4, 5]
    res = sol.maxProfit2(prices)
    print(res)
