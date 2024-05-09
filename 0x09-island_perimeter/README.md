# 🏝️ Island Perimeter

![](https://assets.leetcode.com/uploads/2018/10/12/island.png)

## Project Overview 🪶
This project focuses on calculating the perimeter of an island represented in a grid. The purpose is to provide a function that accurately computes the perimeter of the island based on the given grid.

## 🔧 Requirements and Dependencies:
- Python 3.4.3 🐍
- PEP 8 style (version 1.7)

## 📚 Tasks:

### 📝 Island Perimeter
---------------------
### 📜 Task Requirements 
Create a function `def island_perimeter(grid):` that returns the perimeter of the island described in `grid`.

- `grid` is a list of list of integers:
    - 0 represents water
    - 1 represents land
    - Each cell is square, with a side length of 1
    - Cells are connected horizontally/vertically (not diagonally).
    - `grid` is rectangular, with its width and height not exceeding 100
- The grid is completely surrounded by water
- There is only one island (or nothing).
- The island doesn't have "lakes" (water inside that isn't connected to the water surrounding the island).

**🧪 Sample Input:**

```python
grid = [
    [0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0]
]
```

**⚡Expected Output:**

```
12
```

### 🗂️ Files 
- **[0-island_perimeter.py](0-island_perimeter.py)**


### Description

The `island_perimeter(grid)` function iterates through the grid and checks each cell for land ("1"). If a land cell is found, it checks its adjacent cells (up, down, left, right) for water ("0") and increments the perimeter count for each water neighbor. This way, the function calculates the total length of the island's borders touching the water.


## 🎓 Key Takeaways

&nbsp; &nbsp; ☑️ Implemented a function to solve a 2D grid problem using nested loops and conditional statements.

&nbsp; &nbsp; ☑️ Learned to navigate through a 2D grid, identify land cells, and count their perimeter edges.

&nbsp; &nbsp; ☑️ Gained experience with problem-solving strategies and applying Python concepts for grid manipulation.


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
