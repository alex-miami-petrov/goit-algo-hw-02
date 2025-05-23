
def check(express):
    stack = []

    delim = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    open_delim = set(delim.values())
    close_delim = set(delim.keys())


    for char in express:
        if char in open_delim:
            stack.append(char)
        elif char in close_delim:
            if not stack:
                return "Несиметрично (зайвий закриваючий розділювач)"
    
            last_opened = stack.pop()


            if last_opened != delim[char]:
                return "Несиметрично (зайвий закриваючий розділювач)"
            

    if stack:
        return "Несиметрично (незакритий розділювач)"
    else:
        return "Симетрично"


express = [
    "( ){[ 1 ]( 1 + 3 )( ){ }}:",       
    ]         

print("--- Перевірка симетрії розділювачів ---")

for exp in express:
    res = check(exp)

print(f"\n{exp} = {res}")
