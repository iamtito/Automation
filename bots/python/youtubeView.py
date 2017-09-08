import webbrowser
import time
import os

url = input("Enter youtube URL:")
refresh = input("Enter refresh time:")
browser= input("Enter your browser (e.g chrome/firefox):")
count = input("How many views do you want?:")

def openURL():
	os.system("TASKKILL /F /IM " + browser + ".exe")
	webbrowser.open(url)
	time.sleep(int(refresh))

	for i in range(int(count)):
		print("webpage has been viewed")
		openURL()

openURL()
