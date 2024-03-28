# ✨ Log Parsing

## ✍️ Project Description:
This project 🎯 aims to create a Python 🐍 script that parses log files 📑, computes metrics 📊, and displays statistics 📈 based on the parsed data. The script reads input from stdin 📥, processes each line according to a specified format 📄, and calculates various statistics such as total file size 🗂️ and counts of different HTTP status codes 🌐.

## 🔧 Requirements and Dependencies:
- Python 3.4.3 🐍
- PEP 8 style (version 1.7.x)

## 📚 Tasks:
- **0. Log Parsing**
  - **📜 Task Requirements:** Write a script that:
    - Read stdin line by line and compute metrics.
    - Print total file size and number of lines by status code after every 10 lines or keyboard interruption.
    - Handle input format and skip lines if not in the specified format.
    - Print statistics in ascending order of status codes.

    ```bash
    $ cat 0-generator.py
    ```
    ``` python
    #!/usr/bin/python3
    import random
    import sys
    from time import sleep
    import datetime
    
    for i in range(10000):
        sleep(random.random())
        sys.stdout.write("{:d}.{:d}.{:d}.{:d} - [{}] \"GET /projects/260 HTTP/1.1\" {} {}\n".format(
            random.randint(1, 255), random.randint(1, 255), random.randint(1, 255), random.randint(1, 255),
            datetime.datetime.now(),
            random.choice([200, 301, 400, 401, 403, 404, 405, 500]),
            random.randint(1, 1024)
        ))
        sys.stdout.flush()
    ```

    **Expected Output**
    ``` bash
    $ ./0-generator.py | ./0-stats.py
    File size: 5213
    200: 2
    401: 1
    403: 2
    404: 1
    405: 1
    500: 3
    File size: 11320
    200: 3
    301: 2
    400: 1
    401: 2
    403: 3
    404: 4
    405: 2
    500: 3
    File size: 16305
    200: 3
    301: 3
    400: 4
    401: 2
    403: 5
    404: 5
    405: 4
    500: 4
    ^CFile size: 17146
    200: 4
    301: 3
    400: 4
    401: 2
    403: 6
    404: 6
    405: 4
    500: 4
    ```

  - **🗂️ Files:** **[0-stats.py](0-stats.py)**, **[0-generator.py](0-generator.py)**
  - **🗒️ Description:** 
    - **0-stats.py**: Parses log data from stdin, calculates statistics, and prints them out.
    - **0-generator.py**: Generates sample log data for testing purposes.

## 🪄 Concluding paragraph:
Throughout this project 📚, I developed a Python 🐍 script to parse log files 📑, handle interruptions ⚠️, and compute relevant statistics 📊. This project enhanced my understanding 🧠 of file handling 📁 and parsing techniques in Python 🐍.

## 🔗 Contact Information: John Doe 
**Github:** **[Binyam Mamo](https://github.com/BinyamMamo)**
