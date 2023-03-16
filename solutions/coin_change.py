class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # memo = [[sys.maxsize for _ in range(len(coins))] for _ in range(amount + 1)]

        # for i in range(len(coins)):
        #     memo[0][i] = 0

        # for i in range(1, amount + 1):
        #     for j, coin in enumerate(coins):
        #         if j > 0:
        #             memo[i][j] = memo[i][j-1]
        #         if i - coin >= 0:
        #             memo[i][j] = min(memo[i][j], memo[i-coin][j] + 1)
                
        # return memo[amount][len(coins)-1] if memo[amount][len(coins)-1] != sys.maxsize else -1

        memo = [sys.maxsize for _ in range(amount + 1)]

        memo[0] = 0

        for a in range(1, amount + 1):
            for coin in coins:
                if a - coin >= 0:
                    memo[a] = min(memo[a], memo[a-coin] + 1)
                
        
        return memo[amount] if memo[amount]!= sys.maxsize else -1

