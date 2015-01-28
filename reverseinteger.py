class Solution:
    # @return an integer
    def reverse(self,x):
        m = str(x)
        mylen = len(m)
        if m[0] == '-':
            tmp = "-"
            for i in range(1, mylen):
                tmp += m[mylen - i]
        else:
            tmp = ""
            for i in range(0, mylen):
                tmp += m[mylen -1 -i]
        tmp = int(tmp)
        if -2147483648L <= tmp <= 2147483647L:   return tmp

        return 0
