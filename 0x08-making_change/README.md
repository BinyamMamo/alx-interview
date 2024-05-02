# Making Change Project ✨

> "Why did the Mr. Bucks go to school? Because it wanted to get changed!" 🤣

## Project Overview 🪶

The Making Change project aims to solve the problem of determining the fewest number of coins needed to meet a given amount. By implementing a dynamic programming approach, the project efficiently computes the minimum number of coins required for a given total using a provided set of coin denominations.

## 🔧 Requirements and Dependencies:

- Python 3.4.3
- PEP 8 style compliance
- Ubuntu 14.04 LTS

## 📚 Tasks:

### 📝 0. Change comes from within
---------------------
**📜 Task requirements:** 

Given a pile of coins of different values, determine the fewest number of coins needed to meet a given amount total.

Prototype: `def makeChange(coins, total)`
Return: fewest number of coins needed to meet `total`
- If `total` is `0` or less, return `0`
- If `total` cannot be met by any number of coins you have, return `-1`

**Sample Input:**

```python
makeChange([1, 2, 25], 37)
makeChange([1256, 54, 48, 16, 102], 1453)
```

**Expected Output:**

```
7
-1
```

**🗂️ Files:** 
- **[0-making_change.py](0-making_change.py)**

**🗒️ Description:** 

The file `0-making_change.py` implements a function `makeChange(coins, total)` that determines the fewest number of coins needed to meet a given amount `total`. It utilizes dynamic programming to efficiently compute the minimum number of coins required using the provided set of coin denominations.

## 🎓 Key Takeaways

- Implemented dynamic programming approach for solving the coin change problem.
- Enhanced understanding of algorithm optimization techniques.

## 📫 Contact Me

[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/BinyamMamo)
[![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:binyammamo01@gmail.com)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/binyammamo)
[![Twitter](https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](#)
[![Website](https://img.shields.io/badge/Website-000000?style=for-the-badge&logo=About.me&logoColor=white)](https://binyammamo.github.io)

<pre id="banner" class="color-change" style="color: #449999" align="center">


 █████╗ ██╗     ██╗  ██╗    ███████╗██╗    ██╗███████╗
██╔══██╗██║     ╚██╗██╔╝    ██╔════╝██║    ██║██╔════╝
███████║██║      ╚███╔╝     ███████╗██║ █╗ ██║█████╗  
██╔══██║██║      ██╔██╗     ╚════██║██║███╗██║██╔══╝  
██║  ██║███████╗██╔╝ ██╗    ███████║╚███╔███╔╝███████╗
╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝    ╚══════╝ ╚══╝╚══╝ ╚══════╝
                                                      
</pre>