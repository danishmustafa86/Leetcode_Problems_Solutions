class Solution:
    def countOfAtoms(self, formula: str) -> str:

        stack = [collections.Counter()]
        i, n = 0, len(formula)
        
        while i < n:
            if formula[i] == '(':
                stack.append(collections.Counter())
                i += 1
            elif formula[i] == ')':
                top = stack.pop()
                i += 1
                i_start = i
                while i < n and formula[i].isdigit():
                    i += 1
                multiplicity = int(formula[i_start:i] or 1)
                for elem in top:
                    stack[-1][elem] += top[elem] * multiplicity
            else:
                i_start = i
                i += 1
                while i < n and formula[i].islower():
                    i += 1
                elem = formula[i_start:i]
                i_start = i
                while i < n and formula[i].isdigit():
                    i += 1
                multiplicity = int(formula[i_start:i] or 1)
                stack[-1][elem] += multiplicity
        
        result = []
        for elem in sorted(stack[-1]):
            count = stack[-1][elem]
            result.append(f"{elem}{count if count > 1 else ''}")
        
        return "".join(result)
