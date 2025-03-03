def generate_parenthesis(n: int) -> list:
    result = []  
    stack = []   
    
   
    def backtrack(n_open: int, n_closed: int, n: int):
   
        if n_open == n_closed == n:
            result.append("".join(stack))
            return      

        if n_open < n:
            stack.append("(") 
            backtrack(n_open + 1, n_closed, n)  
            stack.pop()
 
        if n_closed < n_open:
            stack.append(")") 
            backtrack(n_open, n_closed + 1, n)  
            stack.pop() 

    backtrack(0, 0, n)
    return result


n = int(input("Enter the number of parenthesis pairs: "))

valid_parenthesis = generate_parenthesis(n)
print(valid_parenthesis)
