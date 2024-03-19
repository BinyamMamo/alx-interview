# ✨ 0x02. Minimum Operations

## ✍️ Project Description:
The "Minimum Operations" project aims to solve the problem of calculating the minimum number of operations needed to achieve a specific number of characters in a text file using only the "Copy All" and "Paste" operations.

## 🔧 Requirements and Dependencies:
- Python 3.4.3
- PEP 8 style
- Ubuntu 14.04 LTS

## 📚 Task:
📝 **Minimum Operations**

**📜 Task Requirements:** Implement a method to calculate the fewest number of operations needed to result in exactly n H characters in the file.
```python
def minOperations(n):
    """
    Calculates the minimum number of operations needed to achieve exactly n H characters

    Args:
        n (int): The desired number of characters

    Returns:
        int: The minimum number of operations needed, or 0 if impossible
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return i + minOperations(n//i)
    return n
```

# Example usage
``` python
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
```
### Output

**n = 4**
```
Min # of operations to reach 4 char: 4
```

**n = 12**
```
Min # of operations to reach 12 char: 7
```

**🗂️ File used:** *[0-minoperations.py](./0-minoperations.py)*

**🗒️ Description:** *[0-minoperations.py](./0-minoperations.py)* contains the implementation of the minOperations function, which calculates the minimum number of operations needed to achieve a specific number of characters.

## 🪄 Concluding paragraph
In this project, I implemented a solution to calculate the minimum number of operations required to reach a certain number of characters in a text file. By following the provided requirements and guidelines, I successfully solved the problem using a greedy algorithm approach. Through this project, I learned about algorithmic problem-solving and the importance of efficient code execution.

## 🔗 Contact Information
**Github:** **[Binyam Mamo](https://github.com/BinyamMamo)**