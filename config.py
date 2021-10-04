import os
import pathlib

edge = {
    "driverPath":pathlib.Path(os.path.join(os.environ['USERPROFILE'],"Downloads\edgedriver_win64_93\msedgedriver.exe")),
    "userDataPath": "user-data-dir="+os.environ['USERPROFILE']+"\\AppData\\Local\\Microsoft\\Edge\\User Data",
    "mobileUserAgent": "user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0 Mobile/15E148 Safari/604.1"
}