class Solution:
    def maximumWealth(self, accounts):
        richest = 0

        for customer in accounts:
            wealth = sum(customer)
            richest = max(richest, wealth)

        return richest
        