class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        count = 0

        for num in range(100, 1000):
            # Last digit must be even
            if num % 2 != 0:
                continue

            a = num // 100
            b = (num // 10) % 10
            c = num % 10

            # Check if digits are available
            temp = digits.copy()

            if a in temp:
                temp.remove(a)
            else:
                continue

            if b in temp:
                temp.remove(b)
            else:
                continue

            if c in temp:
                temp.remove(c)
            else:
                continue

            count += 1

        return count