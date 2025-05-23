from queue import Queue
import time
from random import random, uniform

def main():
    q = Queue()
    req_id = 0
    

    print("Симулятор центру обробки заявок запущено. Натисніть Ctrl+C для виходу.")

    try:
        while True:
            cur_time = time.strftime("%H:%M:%S")
            if random() < 0.8:
                req_id += 1
                data = f"Заявка №{req_id}"
                q.put(data)
                print(f"[{cur_time}] Створено: {data}. Залишилось в черзі: {q.qsize()}")

            if not q.empty():
                req = q.get()
                print(f"[{cur_time}] Обробляється: {req}...")
                time.sleep(uniform(0.5, 1.5))
                print(f"[{cur_time}] Завершено обробку: {req}.")
            else:
                print(f"[{cur_time}] Черга заявок порожня. Очікування...")
            

            time.sleep(uniform(0.2, 0.8))


    except KeyboardInterrupt:
        print("\nПрограма зупинена користувачем")
    except Exception as e:
        print(f"Виникла помилка: {e}")


if __name__ == "__main__":
    main()
