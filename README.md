# 南華大學資料結構-期末報告
11124213 張芮瑜
# 第一題 Python棧實現進制轉換的示例詳解
## 概述
堆疊（stack）又稱為棧或堆棧，是電腦科學中的一種抽象資料型別，只允許在有序的線性資料集合的一端（稱為堆疊頂端，top）進行加入資料（push）和移除資料（pop）的運算。因而按照後進先出的原理運作，堆疊常用一維陣列或連結串列來實現。其中之一是使用堆疊來實現進制轉換，講一個數字從一種進制表示轉為另一種進制表示，本文將深入研究堆疊的原理，以及如何使用Python實現十進制到二進制、八進制和十六進制的進制轉換。
## 了解進制轉換
在計算機科學和數學中，進制是一種表示數字的方式，它決定了一個數字的基數和表示規則。最常見的進制包括：
```
十進制（Decimal）：基數為10，使用0-9這10個數字表示。
二進制（Binary）：基數為2，使用0和1表示。
八進制（Octal）：基數為8，使用0-7表示。
十六進制（Hexadecimal）：基數為16，使用0-9和A-F表示。
```
進制轉換是將數字從一種進制表示轉換為另一種進制表示的過程。接下來的部分，我們將重點關注如何將十進制數轉換為其他進制。
## 進制轉換原理
進制轉換的核心原理涉及到除法和取餘操作。具體步驟如下：
```
從十進制數的最右邊開始，連續進行除法和取餘操作。
將每次取得的餘數存儲起來，它們構成了新進制下的數值。
將商作為下一輪的被除數，直到商為0為止。
將存儲的餘數按照相反的順序排列，得到新進制的表示。
```
## 範例1：十進制到二進制
我們以十進制數 233 為例，將其轉換為二進制。
```
用 2（二進制的基數）除以 233，得到商 116 和餘數 1。
然後，將商 116 除以 2，得到商 58 和餘數 0。
繼續這個過程，直到商為 0。
最後，將所有的餘數從下往上排列，得到二進制表示為 11101001。
這個轉換過程可以輕鬆地使用堆疊來實現。
```
### 使用堆疊進行進制轉換
堆疊是一種理想的數據結構，用於實現進制轉換。我們可以將每次的餘數推入堆疊中，然後按相反的順序從堆疊中彈出這些餘數，從而獲得正確的進制表示。以下是使用Python堆疊實現十進制到二進制轉換的範例代碼：
```
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
```
### 輸出結果
```
11101001
```
![期末結果1](https://github.com/user-attachments/assets/fb2b5c37-07f0-4377-9785-c762a89af712)
這個函數使用堆疊來存儲餘數，並將它們按照正確的順序彈出以構建二進制表示。這個方法可以用於任何十進制到二進制的轉換。
## 範例2：十進制到八進制
將十進制數轉換為八進制的範例。我們只需稍微修改上面的代碼，將基數從2改為8：
```
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
```
### 輸出結果
```
351
```
![期末結果2](https://github.com/user-attachments/assets/96dd1f8f-f617-49d9-9800-4bc5030226fc)
同理，我們只需將基數修改為16，即可實現十進制到十六進制的轉換。
## 進制轉換的應用
```
計算機記憶體管理： 計算機記憶體中的數據通常以二進制形式存儲。進制轉換用於查看和理解記憶體中的數據。
網絡通信： 數據在計算機網絡中以二進制傳輸。進制轉換有助於理解和解析網絡數據包。
圖像處理： 圖像的像素值通常以不同的進制表示，進制轉換可用於修改圖像的顏色深度等。
編程： 程序員可能需要在不同的進制之間進行轉換，以便理解和調試程序中的數據。
密碼學： 加密和解密算法中使用了不同進制的數學操作，包括二進制和十六進制。
```
進制轉換是計算機科學中的一個基本概念，深入了解它將有助於更好地理解計算機系統的內部工作原理。
## 結論
堆疊是一個強大的數據結構，用於實現進制轉換等許多問題。通過深入理解堆疊的工作原理，您可以更好地理解它的應用，包括計算機記憶體管理、編程、網絡通信等領域。
進制轉換在計算機科學和編程中有重要的應用。了解如何使用推疊來實現進制轉換將幫助您更好地理解計算機記憶體管理、網絡通信、圖像處理和編程中的數據表示。
