class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD = 10**9 + 7

        # Answer = C(n + k - 1, 2k)
        N = n + k - 1
        r = 2 * k

        numerator = 1
        denominator = 1

        for i in range(r):
            numerator = numerator * (N - i) % MOD
            denominator = denominator * (i + 1) % MOD

        # Fermat's Little Theorem
        denominator = pow(denominator, MOD - 2, MOD)

        return numerator * denominator % MOD