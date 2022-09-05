class Solution(object):
    def diffWaysToCompute(self, expression):
        """
        :type expression: str
        :rtype: List[int]
        """
        def ways(exp):
            obj = {}
            if exp in obj:
                return obj[exp]
            if exp.isnumeric() and len(exp) == 1 or len(exp) == 2 and exp.isnumeric:
                return [int(exp)]
            operators = {'*', '-', '+'}
            ans = []
            for i in range(len(exp)):

                if exp[i] in operators:
                    # break and solve in two parts
                    x = ways(exp[:i])
                    y = ways(exp[i+1:])
                    for a in x:
                        for b in y:
                            if exp[i] == '+':
                                ans.append(a+b)
                            elif exp[i] == '-':
                                ans.append(a-b)
                            elif exp[i] == '*':
                                ans.append(a*b)
            obj[exp] = ans
            return obj[exp]
        return ways(expression)
