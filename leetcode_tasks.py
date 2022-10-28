class Best_Time_to_Buy_and_Sell_Stock:

    def maxProfit(self, prices: list[int]) -> int:
        # Runtime: 1614 ms, faster than 72.30% of Python3 online submissions for Best Time to Buy and Sell Stock.
        # Memory Usage: 25 MB, less than 85.61% of Python3 online submissions for Best Time to Buy and Sell Stock.
        i = 0
        best = 0
        min_bound = prices[0]
        max_bound = 0
        while i < len(prices) - 1:
            if prices[i] < prices[i + 1] and prices[i] <= min_bound:
                new_max = max(prices[i + 1:])
                profit = new_max - prices[i]
                if profit > best:
                    best = profit
                    min_bound = prices[i]
                    max_bound = new_max
            i += 1
        if max_bound == 0:
            return 0
        return max_bound - min_bound

class lengthOfLastWord:
    """
    Given a string s consisting of words and spaces, return the length of the last word in the string.
    A word is a maximal substring consisting of non-space characters only.

    Runtime: 61 ms, faster than 27.97% of Python3 online submissions for Length of Last Word.
    Memory Usage: 14 MB, less than 5.39% of Python3 online submissions for Length of Last Word.
    """
    def lengthOfLastWord(self, s: str) -> int:
        from string import ascii_letters, whitespace
        good_chars = (ascii_letters + whitespace).encode()
        junk_chars = bytearray(set(range(0x100)) - set(good_chars))

        s = s.encode('ascii', 'ignore').translate(None, junk_chars).decode()
        words = s.split(" ")
        words = [x for x in words if x != '']
        return len(words[-1])