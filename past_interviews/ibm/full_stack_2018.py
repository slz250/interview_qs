global final_max

"""
n: dollar amt
bundleQuantities: arr w/ arr[i] being number of notebooks in bundles
bundleCosts: arr w/ arr[i] being cost per bundle

max # of notebooks that can be bought
"""
def budgetShopping(n, bundleQuantities, bundleCosts):
    def helper(store_num, temp_total, money_left):
        for i in range(store_num, len(bundleQuantities)):
            max_amount = money_left / bundleCosts[i]
            for j in range(0, max_amount+1):
                temp_total += j * bundleQuantities[i]
                if j == max_amount + 1:
                    global final_max
                    final_max = temp_total if temp_total > final_max else final_max
                    return
                money_left -= j * bundleCosts[i]
                helper(i+1, temp_total, money_left)
                temp_total -= j * bundleQuantities[i]
                money_left += j * bundleCosts[i]

    helper(0, 0, n)
    return final_max