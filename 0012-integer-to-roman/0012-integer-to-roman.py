class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        # Map values to their Roman numeral symbols in descending order
        roman_map = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
        ]
        
        res = []
        
        for value, symbol in roman_map:
            if num == 0:
                break 
            # Count how many times the value fits into num
            count = num // value
            if count:
                res.append(symbol * count)
                num %= value  # Update num to the remainder
                
        return "".join(res)