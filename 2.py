from collections import deque

def pal_check(text):
    cleaned_text = "".join(char for char in text if text.isalnum()).lower()
    char_deque = deque(cleaned_text)


    while len(char_deque) > 1:
        first = char_deque.popleft()
        last = char_deque.pop()


        if first != last:
            return f"Не паліндром"
        

    return f"Паліндром"


print(f"Козак => {pal_check('Козак')}")
print(f"No lemon, no melon => {pal_check('No lemon, no melon')}")