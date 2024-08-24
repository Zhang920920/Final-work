#範例一
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def size(self):
        return len(self.items)

def decimal_to_binary(decimal_num):
    stack = Stack()  # 創建一個空堆疊，用於存儲餘數

    while decimal_num > 0:
        remainder = decimal_num % 2  # 計算餘數
        stack.push(remainder)  # 將餘數推入堆疊中
        decimal_num = decimal_num // 2  # 更新商

    binary_str = ""
    while not stack.is_empty():
        binary_str += str(stack.pop())  # 彈出堆疊中的餘數，建構二進制字符串

    return binary_str
print(decimal_to_binary(233))  

#範例二
def decimal_to_octal(decimal_num):
    stack = Stack()  # 創建一個空堆疊，用於存儲餘數

    while decimal_num > 0:
        remainder = decimal_num % 8  # 計算餘數
        stack.push(remainder)  # 將餘數推入堆疊中
        decimal_num = decimal_num // 8  # 更新商

    octal_str = ""
    while not stack.is_empty():
        octal_str += str(stack.pop())  # 彈出堆疊中的餘數，建構八進制字符串

    return octal_str
print(decimal_to_octal(233))  
