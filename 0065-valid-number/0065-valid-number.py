class Solution:
    def isNumber(self, s: str) -> bool:
        try:
            if s == "Infinity" or s == "NaN" or s == "nan" or s == "-inf" or s == "infinity" or s == "INF" or s == "inf" or s == "+inf" or s == "+infinity" or s == "+Infinity" or s == "-infinity" or s == "-Infinity" or s == "+INF" or s == "-INF" or s== "-nan" or s == "+nan" or s == "+NaN" or s == "-NaN":
                return False
            float(s)
            return True
            
        except ValueError:
            return False