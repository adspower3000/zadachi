from functools import lru_cache


def coin_change(coins: list[int], amount: int) -> int:

    @lru_cache
    def helper(amount):
        if amount == 0:
            return 0

        if amount < 0:
            return float('inf')

        ret = float('inf')

        for c in coins:
            ret = min(ret, 1 + helper(amount - c))

        return ret

    ans = helper(amount)

    return ans if ans != float('inf') else -1

coins = [1,2,5]
amount = 11

print(coin_change(coins, amount))