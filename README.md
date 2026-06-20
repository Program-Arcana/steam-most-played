# Steam Most Played 🎮

Python program to visualize a Steam user's most played games in a pie chart. 

![Python](https://img.shields.io/badge/Python-3.10+-yellow)
![Version](https://img.shields.io/badge/Version-1.0-blue)

--- 

## FEATURES 🌟
- Can retrieve data about a Steam user from their profile URL such as their name, ID number, and owned games
- Pie chart visualization of a user's most played games (if their games and profile are made public)

## INSTALLATION ⚙️
Clone the repository while in your desired directory:
```bash
git clone https://github.com/Program-Arcana/steam-most-played.git
```
Navigate to the repository directory to begin using it.

Create and activate a virtual environment:
MacOS:
```bash
python3 -m venv venv
source venv/bin/activate
```
Windows:
```bash
python -m venv venv
venv\Scripts\activate.bat
```

Use package manager pip to install the following:
```bash
pip install matplotlib
pip install numpy
pip install requests
pip install bs4
pip install python-dotenv
```
## USAGE 🔧
You must have a Steam account in order to use this program.  

Go to https://steamcommunity.com/dev, skim to "Obtaining an Steam Web API Key", and click the "by filling out this form" hyperlink.  

Register for an API Key and save it once it gets shown to you. Or you can always go to https://steamcommunity.com/dev/apikey to see it again.  

Create a .env file named ".env" in the same directory as the program files with the following contents:
```bash
API_KEY = "<INSERT-YOUR-API-KEY-HERE>"
```

While you are still in your virtual environment, run this command to start the program:
```bash
python3 visualizer.py
```

You will then be prompted to enter a URL. Copy a Steam user's profile URL (found at the top of the page in the desktop app or in the top search bar on the webpage). Paste the URL and press ENTER to proceed.  

A pie chart will be generated with the user's most played games if their profile is made public or exists. Otherwise, the program will tell you that their profile cannot be accessed or doesn't exist.  

When you are done with the program, you can deactivate the virtual environment with this command:
```bash
deactivate
```

## ATTRIBUTION ©️
- Steam Web API: https://steamcommunity.com/dev
- Matplotlib: https://matplotlib.org/stable/
- Numpy: https://numpy.org
- Requests: https://requests.readthedocs.io/en/latest/
- BeautifulSoup: https://beautiful-soup-4.readthedocs.io/en/latest/#
- Python Dotenv: https://pypi.org/project/python-dotenv/

