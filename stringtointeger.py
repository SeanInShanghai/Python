class Solution:
    # @return an integer
    def atoi(self, str):
        index = 0
        result = 0
        sign = 1
        
        if len(str) == 0: 
            return 0
        
        while str[index].isspace():
            index += 1

        if str[index] == '-':
            sign = -1
        
        if str[index] in "-+":
            index += 1

        if not str[index].isdigit():
            return 0
        
        while index < len(str) and str[index].isdigit():
            result = result * 10 + int(str[index])
            index +=1
         
        result = result * sign
        if sign == 1 and result >= 2147483647: 
            return 2147483647
        if sign == -1 and result <= -2147483648:
            return -2147483648
        
        return result

s = Solution()
print s.atoi("123")
