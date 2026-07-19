class Solution:
    def restoreIpAddresses(self, s: str) -> list[str]:
        res = []
        
        # Early exit for strings that are physically too short or too long
        if len(s) < 4 or len(s) > 12:
            return res
            
        def backtrack(start: int, path: list[str]):
            # Base case: If we have 4 segments and used the entire string, it's valid
            if len(path) == 4:
                if start == len(s):
                    res.append(".".join(path))
                return
                
            # Explore segments of lengths 1, 2, and 3
            for length in range(1, 4):
                # Ensure we don't slice past the end of the string
                if start + length > len(s):
                    break
                    
                segment = s[start:start+length]
                
                # Check for leading zeros: if length > 1, it can't start with '0'
                if length > 1 and segment[0] == '0':
                    continue
                    
                # Check value constraint
                if int(segment) > 255:
                    continue
                    
                # Move to the next segment
                backtrack(start + length, path + [segment])
                
        backtrack(0, [])
        return res