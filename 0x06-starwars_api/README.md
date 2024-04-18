# Star Wars API ✨

![](https://media1.tenor.com/m/5qDyUA_lkZ8AAAAC/star-wars-logo.gif)


## Project Overview 🪶
This project is a script that interacts with the Star Wars API to retrieve information about characters from Star Wars movies.

## 🔧 Requirements and Dependencies:
- Node.js version 10.14.x
- `semistandard` module
- `request` module

## 📚 Tasks:

### 📝 Star Wars Characters
---------------------
**📜 Task requirements:** 
Write a script that prints all characters of a Star Wars movie. The first positional argument passed is the Movie ID. Display one character name per line in the same order as the "characters" list in the `/films/` endpoint.

**🗂️ Files:** 
- **[0-starwars_characters.js](0-starwars_characters.js)**

**🗒️ Description:** 
This script makes a request to the Star Wars API films endpoint with the provided movie ID. It then extracts the list of characters from the response and prints them out one by one.

### 📝 Additional Information

**Installation Commands:**
```bash
$ curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
$ sudo apt-get install -y nodejs
$ sudo npm install semistandard --global
$ sudo npm install request --global
$ export NODE_PATH=/usr/lib/node_modules
```

**Running the script:**
```bash
$ ./0-starwars_characters.js <movie_id>
```
Replace <movie_id> with the ID of the Star Wars movie you want to retrieve characters from.

## 🎓 Key Takeaways
 - Interacting with REST APIs using Node.js
 - Making HTTP requests with the request module
 - Parsing JSON responses from API requests

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
