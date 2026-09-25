class Solution:
    def braceExpansionII(self, expression: str):
        n = len(expression)

        def parse_expr(i):
            # Union: a,b,c
            result = set()

            while i < n and expression[i] != '}':
                part, i = parse_term(i)
                result |= part

                if i < n and expression[i] == ',':
                    i += 1

            return result, i

        def parse_term(i):
            # Concatenation: ab, {a,b}c, a{b,c}
            result = {""}

            while i < n and expression[i] not in '},':
                if expression[i] == '{':
                    part, i = parse_expr(i + 1)

                    # Skip '}'
                    i += 1
                else:
                    part = {expression[i]}
                    i += 1

                # Cartesian product / concatenation
                new_result = set()

                for a in result:
                    for b in part:
                        new_result.add(a + b)

                result = new_result

            return result, i

        result, _ = parse_expr(0)

        return sorted(result)