# MS Auto Rewards
What is this project? Well this was my solution to getting all the microsoft points possible without having to use bing on a daily basis. This project uses a combination of Python + Selenium, I learned these skills during a dev ops course I was taking through Udacity and I wanted to put those newly aqquired skills to something fun.

## Getting started

1) Download and install Python 3
2) Download the Selenium Driver
3) Download the Edge Selenium Driver
4) Open MS Edge and sign into your Microsoft account on the ms rewards website
5) Modify the code in `config.py driverPath` for the path to the selenium Edge driver
6) Create a python env using `python -m venv ./.ms-rewards-auto`
7) Install dependencies `pip install -r requirements`
8) Modify the main.ps1 powershell script to point to the path where the code is so we can call this powershell script to run the code