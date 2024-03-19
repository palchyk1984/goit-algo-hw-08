import heapq

def merge_cables(cables):
    # Перетворення списку кабелів у мінімальну купу
    heapq.heapify(cables)
    
    total_cost = 0
    while len(cables) > 1:
        # Видалення двох найменших кабелів
        shortest1 = heapq.heappop(cables)
        shortest2 = heapq.heappop(cables)
        
        # З'єднання кабелів та обчислення витрат
        cost = shortest1 + shortest2
        total_cost += cost
        
        # Додавання з'єднаного кабелю до купи
        heapq.heappush(cables, cost)
    
    return total_cost

# Приклад використання
cables = [4, 3, 2, 6]  # Приклад списку довжин кабелів
min_total_cost = merge_cables(cables)
print("Мінімальні витрати на з'єднання кабелів:", min_total_cost)
