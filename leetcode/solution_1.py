class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        s = ""
        for i in digits:
            s += str(i)
        num = int(s) + 1

        return [int(i) for i in str(num)]
