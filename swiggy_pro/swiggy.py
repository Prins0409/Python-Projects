import csv
from html.parser import HTMLParser
from itertools import count
from tkinter import N
import requests
import json
from bs4 import BeautifulSoup
def write_output(data):
	with open('swiggy.csv', mode='w',newline="", encoding="utf-8") as output_file:
		writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
		writer.writerow(["job_Id","job_title","location","unit","discription","web_url","page_url"])
		for row in data:
			writer.writerow(row)

def fetch_data():
        urls = ["https://careers.swiggy.com/#/careers?src%3Dcareers%26p%3DeyJwYWdlVHlwZSI6ImpkIiwiY3ZTb3VyY2UiOiJjYXJlZXJzIiwicmVxSWQiOjY4NzksInJlcXVlc3RlciI6eyJpZCI6IiIsImNvZGUiOiIiLCJuYW1lIjoiIn0sInBhZ2UiOiJjYXJlZXJzIiwiYnVmaWx0ZXIiOi0xLCJjdXN0b21GaWVsZHMiOnt9fQ=%3D",
        "https://careers.swiggy.com/#/careers?src%3Dcareers%26p%3DeyJwYWdlVHlwZSI6ImpkIiwiY3ZTb3VyY2UiOiJjYXJlZXJzIiwicmVxSWQiOjY4NzUsInJlcXVlc3RlciI6eyJpZCI6IiIsImNvZGUiOiIiLCJuYW1lIjoiIn0sInBhZ2UiOiJjYXJlZXJzIiwiYnVmaWx0ZXIiOi0xLCJjdXN0b21GaWVsZHMiOnt9fQ=%3D",
        "https://careers.swiggy.com/#/careers?src%3Dcareers%26p%3DeyJwYWdlVHlwZSI6ImpkIiwiY3ZTb3VyY2UiOiJjYXJlZXJzIiwicmVxSWQiOjY4NzQsInJlcXVlc3RlciI6eyJpZCI6IiIsImNvZGUiOiIiLCJuYW1lIjoiIn0sInBhZ2UiOiJjYXJlZXJzIiwiYnVmaWx0ZXIiOi0xLCJjdXN0b21GaWVsZHMiOnt9fQ=%3D",
        "https://careers.swiggy.com/#/careers?src%3Dcareers%26p%3DeyJwYWdlVHlwZSI6ImpkIiwiY3ZTb3VyY2UiOiJjYXJlZXJzIiwicmVxSWQiOjY4NjIsInJlcXVlc3RlciI6eyJpZCI6IiIsImNvZGUiOiIiLCJuYW1lIjoiIn0sInBhZ2UiOiJjYXJlZXJzIiwiYnVmaWx0ZXIiOi0xLCJjdXN0b21GaWVsZHMiOnt9fQ=%3D",
        "https://careers.swiggy.com/#/careers?src%3Dcareers%26p%3DeyJwYWdlVHlwZSI6ImpkIiwiY3ZTb3VyY2UiOiJjYXJlZXJzIiwicmVxSWQiOjY4NjAsInJlcXVlc3RlciI6eyJpZCI6IiIsImNvZGUiOiIiLCJuYW1lIjoiIn0sInBhZ2UiOiJjYXJlZXJzIiwiYnVmaWx0ZXIiOi0xLCJjdXN0b21GaWVsZHMiOnt9fQ=%3D",
        "https://careers.swiggy.com/#/careers?src%3Dcareers%26p%3DeyJwYWdlVHlwZSI6ImpkIiwiY3ZTb3VyY2UiOiJjYXJlZXJzIiwicmVxSWQiOjY4MzksInJlcXVlc3RlciI6eyJpZCI6IiIsImNvZGUiOiIiLCJuYW1lIjoiIn0sInBhZ2UiOiJjYXJlZXJzIiwiYnVmaWx0ZXIiOi0xLCJjdXN0b21GaWVsZHMiOnt9fQ=%3D",
        "https://careers.swiggy.com/#/careers?src%3Dcareers%26p%3DeyJwYWdlVHlwZSI6ImpkIiwiY3ZTb3VyY2UiOiJjYXJlZXJzIiwicmVxSWQiOjY4MzEsInJlcXVlc3RlciI6eyJpZCI6IiIsImNvZGUiOiIiLCJuYW1lIjoiIn0sInBhZ2UiOiJjYXJlZXJzIiwiYnVmaWx0ZXIiOi0xLCJjdXN0b21GaWVsZHMiOnt9fQ=%3D",
        "https://careers.swiggy.com/#/careers?src%3Dcareers%26p%3DeyJwYWdlVHlwZSI6ImpkIiwiY3ZTb3VyY2UiOiJjYXJlZXJzIiwicmVxSWQiOjY4MjUsInJlcXVlc3RlciI6eyJpZCI6IiIsImNvZGUiOiIiLCJuYW1lIjoiIn0sInBhZ2UiOiJjYXJlZXJzIiwiYnVmaWx0ZXIiOi0xLCJjdXN0b21GaWVsZHMiOnt9fQ=%3D",
        "https://careers.swiggy.com/#/careers?src%3Dcareers%26p%3DeyJwYWdlVHlwZSI6ImpkIiwiY3ZTb3VyY2UiOiJjYXJlZXJzIiwicmVxSWQiOjY4MjAsInJlcXVlc3RlciI6eyJpZCI6IiIsImNvZGUiOiIiLCJuYW1lIjoiIn0sInBhZ2UiOiJjYXJlZXJzIiwiYnVmaWx0ZXIiOi0xLCJjdXN0b21GaWVsZHMiOnt9fQ=%3D",
        "https://careers.swiggy.com/#/careers?src%3Dcareers%26p%3DeyJwYWdlVHlwZSI6ImpkIiwiY3ZTb3VyY2UiOiJjYXJlZXJzIiwicmVxSWQiOjY3ODIsInJlcXVlc3RlciI6eyJpZCI6IiIsImNvZGUiOiIiLCJuYW1lIjoiIn0sInBhZ2UiOiJjYXJlZXJzIiwiYnVmaWx0ZXIiOi0xLCJjdXN0b21GaWVsZHMiOnt9fQ=%3D",
        "https://careers.swiggy.com/#/careers?src%3Dcareers%26p%3DeyJwYWdlVHlwZSI6ImpkIiwiY3ZTb3VyY2UiOiJjYXJlZXJzIiwicmVxSWQiOjY3NTcsInJlcXVlc3RlciI6eyJpZCI6IiIsImNvZGUiOiIiLCJuYW1lIjoiIn0sInBhZ2UiOiJjYXJlZXJzIiwiYnVmaWx0ZXIiOi0xLCJjdXN0b21GaWVsZHMiOnt9fQ=%3D",
        "https://careers.swiggy.com/#/careers?src%3Dcareers%26p%3DeyJwYWdlVHlwZSI6ImpkIiwiY3ZTb3VyY2UiOiJjYXJlZXJzIiwicmVxSWQiOjY3MTMsInJlcXVlc3RlciI6eyJpZCI6IiIsImNvZGUiOiIiLCJuYW1lIjoiIn0sInBhZ2UiOiJjYXJlZXJzIiwiYnVmaWx0ZXIiOi0xLCJjdXN0b21GaWVsZHMiOnt9fQ=%3D",
        "https://careers.swiggy.com/#/careers?src%3Dcareers%26p%3DeyJwYWdlVHlwZSI6ImpkIiwiY3ZTb3VyY2UiOiJjYXJlZXJzIiwicmVxSWQiOjY2NzUsInJlcXVlc3RlciI6eyJpZCI6IiIsImNvZGUiOiIiLCJuYW1lIjoiIn0sInBhZ2UiOiJjYXJlZXJzIiwiYnVmaWx0ZXIiOi0xLCJjdXN0b21GaWVsZHMiOnt9fQ=%3D",
        "https://careers.swiggy.com/#/careers?src%3Dcareers%26p%3DeyJwYWdlVHlwZSI6ImpkIiwiY3ZTb3VyY2UiOiJjYXJlZXJzIiwicmVxSWQiOjY2NTMsInJlcXVlc3RlciI6eyJpZCI6IiIsImNvZGUiOiIiLCJuYW1lIjoiIn0sInBhZ2UiOiJjYXJlZXJzIiwiYnVmaWx0ZXIiOi0xLCJjdXN0b21GaWVsZHMiOnt9fQ=%3D",
        "https://careers.swiggy.com/#/careers?src%3Dcareers%26p%3DeyJwYWdlVHlwZSI6ImpkIiwiY3ZTb3VyY2UiOiJjYXJlZXJzIiwicmVxSWQiOjY2MjEsInJlcXVlc3RlciI6eyJpZCI6IiIsImNvZGUiOiIiLCJuYW1lIjoiIn0sInBhZ2UiOiJjYXJlZXJzIiwiYnVmaWx0ZXIiOi0xLCJjdXN0b21GaWVsZHMiOnt9fQ=%3D",
        "https://careers.swiggy.com/#/careers?src%3Dcareers%26p%3DeyJwYWdlVHlwZSI6ImpkIiwiY3ZTb3VyY2UiOiJjYXJlZXJzIiwicmVxSWQiOjY1OTQsInJlcXVlc3RlciI6eyJpZCI6IiIsImNvZGUiOiIiLCJuYW1lIjoiIn0sInBhZ2UiOiJjYXJlZXJzIiwiYnVmaWx0ZXIiOi0xLCJjdXN0b21GaWVsZHMiOnt9fQ=%3D",
        "https://careers.swiggy.com/#/careers?src%3Dcareers%26p%3DeyJwYWdlVHlwZSI6ImpkIiwiY3ZTb3VyY2UiOiJjYXJlZXJzIiwicmVxSWQiOjY1OTMsInJlcXVlc3RlciI6eyJpZCI6IiIsImNvZGUiOiIiLCJuYW1lIjoiIn0sInBhZ2UiOiJjYXJlZXJzIiwiYnVmaWx0ZXIiOi0xLCJjdXN0b21GaWVsZHMiOnt9fQ=%3D",
        "https://careers.swiggy.com/#/careers?src%3Dcareers%26p%3DeyJwYWdlVHlwZSI6ImpkIiwiY3ZTb3VyY2UiOiJjYXJlZXJzIiwicmVxSWQiOjY1OTEsInJlcXVlc3RlciI6eyJpZCI6IiIsImNvZGUiOiIiLCJuYW1lIjoiIn0sInBhZ2UiOiJjYXJlZXJzIiwiYnVmaWx0ZXIiOi0xLCJjdXN0b21GaWVsZHMiOnt9fQ=%3D",
        "https://careers.swiggy.com/#/careers?src%3Dcareers%26p%3DeyJwYWdlVHlwZSI6ImpkIiwiY3ZTb3VyY2UiOiJjYXJlZXJzIiwicmVxSWQiOjY1NDAsInJlcXVlc3RlciI6eyJpZCI6IiIsImNvZGUiOiIiLCJuYW1lIjoiIn0sInBhZ2UiOiJjYXJlZXJzIiwiYnVmaWx0ZXIiOi0xLCJjdXN0b21GaWVsZHMiOnt9fQ=%3D",
        "https://careers.swiggy.com/#/careers?src%3Dcareers%26p%3DeyJwYWdlVHlwZSI6ImpkIiwiY3ZTb3VyY2UiOiJjYXJlZXJzIiwicmVxSWQiOjY0OTcsInJlcXVlc3RlciI6eyJpZCI6IiIsImNvZGUiOiIiLCJuYW1lIjoiIn0sInBhZ2UiOiJjYXJlZXJzIiwiYnVmaWx0ZXIiOi0xLCJjdXN0b21GaWVsZHMiOnt9fQ=%3D",
        "https://careers.swiggy.com/#/careers?src%3Dcareers%26p%3DeyJwYWdlVHlwZSI6ImpkIiwiY3ZTb3VyY2UiOiJjYXJlZXJzIiwicmVxSWQiOjY0NzcsInJlcXVlc3RlciI6eyJpZCI6IiIsImNvZGUiOiIiLCJuYW1lIjoiIn0sInBhZ2UiOiJjYXJlZXJzIiwiYnVmaWx0ZXIiOi0xLCJjdXN0b21GaWVsZHMiOnt9fQ=%3D",
        "https://careers.swiggy.com/#/careers?src%3Dcareers%26p%3DeyJwYWdlVHlwZSI6ImpkIiwiY3ZTb3VyY2UiOiJjYXJlZXJzIiwicmVxSWQiOjY0NzYsInJlcXVlc3RlciI6eyJpZCI6IiIsImNvZGUiOiIiLCJuYW1lIjoiIn0sInBhZ2UiOiJjYXJlZXJzIiwiYnVmaWx0ZXIiOi0xLCJjdXN0b21GaWVsZHMiOnt9fQ=%3D",
        "https://careers.swiggy.com/#/careers?src%3Dcareers%26p%3DeyJwYWdlVHlwZSI6ImpkIiwiY3ZTb3VyY2UiOiJjYXJlZXJzIiwicmVxSWQiOjY0MjAsInJlcXVlc3RlciI6eyJpZCI6IiIsImNvZGUiOiIiLCJuYW1lIjoiIn0sInBhZ2UiOiJjYXJlZXJzIiwiYnVmaWx0ZXIiOi0xLCJjdXN0b21GaWVsZHMiOnt9fQ=%3D",
        "https://careers.swiggy.com/#/careers?src%3Dcareers%26p%3DeyJwYWdlVHlwZSI6ImpkIiwiY3ZTb3VyY2UiOiJjYXJlZXJzIiwicmVxSWQiOjYyNTEsInJlcXVlc3RlciI6eyJpZCI6IiIsImNvZGUiOiIiLCJuYW1lIjoiIn0sInBhZ2UiOiJjYXJlZXJzIiwiYnVmaWx0ZXIiOi0xLCJjdXN0b21GaWVsZHMiOnt9fQ=%3D",
        "https://careers.swiggy.com/#/careers?src%3Dcareers%26p%3DeyJwYWdlVHlwZSI6ImpkIiwiY3ZTb3VyY2UiOiJjYXJlZXJzIiwicmVxSWQiOjYyMjYsInJlcXVlc3RlciI6eyJpZCI6IiIsImNvZGUiOiIiLCJuYW1lIjoiIn0sInBhZ2UiOiJjYXJlZXJzIiwiYnVmaWx0ZXIiOi0xLCJjdXN0b21GaWVsZHMiOnt9fQ=%3D",
        "https://careers.swiggy.com/#/careers?src%3Dcareers%26p%3DeyJwYWdlVHlwZSI6ImpkIiwiY3ZTb3VyY2UiOiJjYXJlZXJzIiwicmVxSWQiOjYxODIsInJlcXVlc3RlciI6eyJpZCI6IiIsImNvZGUiOiIiLCJuYW1lIjoiIn0sInBhZ2UiOiJjYXJlZXJzIiwiYnVmaWx0ZXIiOi0xLCJjdXN0b21GaWVsZHMiOnt9fQ=%3D",
        "https://careers.swiggy.com/#/careers?src%3Dcareers%26p%3DeyJwYWdlVHlwZSI6ImpkIiwiY3ZTb3VyY2UiOiJjYXJlZXJzIiwicmVxSWQiOjYwMjMsInJlcXVlc3RlciI6eyJpZCI6IiIsImNvZGUiOiIiLCJuYW1lIjoiIn0sInBhZ2UiOiJjYXJlZXJzIiwiYnVmaWx0ZXIiOi0xLCJjdXN0b21GaWVsZHMiOnt9fQ=%3D",
        "https://careers.swiggy.com/#/careers?src%3Dcareers%26p%3DeyJwYWdlVHlwZSI6ImpkIiwiY3ZTb3VyY2UiOiJjYXJlZXJzIiwicmVxSWQiOjYwMDIsInJlcXVlc3RlciI6eyJpZCI6IiIsImNvZGUiOiIiLCJuYW1lIjoiIn0sInBhZ2UiOiJjYXJlZXJzIiwiYnVmaWx0ZXIiOi0xLCJjdXN0b21GaWVsZHMiOnt9fQ=%3D",
        "https://careers.swiggy.com/#/careers?src%3Dcareers%26p%3DeyJwYWdlVHlwZSI6ImpkIiwiY3ZTb3VyY2UiOiJjYXJlZXJzIiwicmVxSWQiOjU5NjksInJlcXVlc3RlciI6eyJpZCI6IiIsImNvZGUiOiIiLCJuYW1lIjoiIn0sInBhZ2UiOiJjYXJlZXJzIiwiYnVmaWx0ZXIiOi0xLCJjdXN0b21GaWVsZHMiOnt9fQ=%3D",
        "https://careers.swiggy.com/#/careers?src%3Dcareers%26p%3DeyJwYWdlVHlwZSI6ImpkIiwiY3ZTb3VyY2UiOiJjYXJlZXJzIiwicmVxSWQiOjU5MjAsInJlcXVlc3RlciI6eyJpZCI6IiIsImNvZGUiOiIiLCJuYW1lIjoiIn0sInBhZ2UiOiJjYXJlZXJzIiwiYnVmaWx0ZXIiOi0xLCJjdXN0b21GaWVsZHMiOnt9fQ=%3D",
        "https://careers.swiggy.com/#/careers?src%3Dcareers%26p%3DeyJwYWdlVHlwZSI6ImpkIiwiY3ZTb3VyY2UiOiJjYXJlZXJzIiwicmVxSWQiOjU5MTksInJlcXVlc3RlciI6eyJpZCI6IiIsImNvZGUiOiIiLCJuYW1lIjoiIn0sInBhZ2UiOiJjYXJlZXJzIiwiYnVmaWx0ZXIiOi0xLCJjdXN0b21GaWVsZHMiOnt9fQ=%3D",
        "https://careers.swiggy.com/#/careers?src%3Dcareers%26p%3DeyJwYWdlVHlwZSI6ImpkIiwiY3ZTb3VyY2UiOiJjYXJlZXJzIiwicmVxSWQiOjU3NTYsInJlcXVlc3RlciI6eyJpZCI6IiIsImNvZGUiOiIiLCJuYW1lIjoiIn0sInBhZ2UiOiJjYXJlZXJzIiwiYnVmaWx0ZXIiOi0xLCJjdXN0b21GaWVsZHMiOnt9fQ=%3D",
        "https://careers.swiggy.com/#/careers?src%3Dcareers%26p%3DeyJwYWdlVHlwZSI6ImpkIiwiY3ZTb3VyY2UiOiJjYXJlZXJzIiwicmVxSWQiOjU2NjUsInJlcXVlc3RlciI6eyJpZCI6IiIsImNvZGUiOiIiLCJuYW1lIjoiIn0sInBhZ2UiOiJjYXJlZXJzIiwiYnVmaWx0ZXIiOi0xLCJjdXN0b21GaWVsZHMiOnt9fQ=%3D",
        "https://careers.swiggy.com/#/careers?src%3Dcareers%26p%3DeyJwYWdlVHlwZSI6ImpkIiwiY3ZTb3VyY2UiOiJjYXJlZXJzIiwicmVxSWQiOjU2NDUsInJlcXVlc3RlciI6eyJpZCI6IiIsImNvZGUiOiIiLCJuYW1lIjoiIn0sInBhZ2UiOiJjYXJlZXJzIiwiYnVmaWx0ZXIiOi0xLCJjdXN0b21GaWVsZHMiOnt9fQ=%3D",
        "https://careers.swiggy.com/#/careers?src%3Dcareers%26p%3DeyJwYWdlVHlwZSI6ImpkIiwiY3ZTb3VyY2UiOiJjYXJlZXJzIiwicmVxSWQiOjU1ODcsInJlcXVlc3RlciI6eyJpZCI6IiIsImNvZGUiOiIiLCJuYW1lIjoiIn0sInBhZ2UiOiJjYXJlZXJzIiwiYnVmaWx0ZXIiOi0xLCJjdXN0b21GaWVsZHMiOnt9fQ=%3D",
        "https://careers.swiggy.com/#/careers?src%3Dcareers%26p%3DeyJwYWdlVHlwZSI6ImpkIiwiY3ZTb3VyY2UiOiJjYXJlZXJzIiwicmVxSWQiOjU0MzIsInJlcXVlc3RlciI6eyJpZCI6IiIsImNvZGUiOiIiLCJuYW1lIjoiIn0sInBhZ2UiOiJjYXJlZXJzIiwiYnVmaWx0ZXIiOi0xLCJjdXN0b21GaWVsZHMiOnt9fQ=%3D",
        "https://careers.swiggy.com/#/careers?src%3Dcareers%26p%3DeyJwYWdlVHlwZSI6ImpkIiwiY3ZTb3VyY2UiOiJjYXJlZXJzIiwicmVxSWQiOjUzNzgsInJlcXVlc3RlciI6eyJpZCI6IiIsImNvZGUiOiIiLCJuYW1lIjoiIn0sInBhZ2UiOiJjYXJlZXJzIiwiYnVmaWx0ZXIiOi0xLCJjdXN0b21GaWVsZHMiOnt9fQ=%3D",
        "https://careers.swiggy.com/#/careers?src%3Dcareers%26p%3DeyJwYWdlVHlwZSI6ImpkIiwiY3ZTb3VyY2UiOiJjYXJlZXJzIiwicmVxSWQiOjUzNjcsInJlcXVlc3RlciI6eyJpZCI6IiIsImNvZGUiOiIiLCJuYW1lIjoiIn0sInBhZ2UiOiJjYXJlZXJzIiwiYnVmaWx0ZXIiOi0xLCJjdXN0b21GaWVsZHMiOnt9fQ=%3D",
        "https://careers.swiggy.com/#/careers?src%3Dcareers%26p%3DeyJwYWdlVHlwZSI6ImpkIiwiY3ZTb3VyY2UiOiJjYXJlZXJzIiwicmVxSWQiOjUzMjcsInJlcXVlc3RlciI6eyJpZCI6IiIsImNvZGUiOiIiLCJuYW1lIjoiIn0sInBhZ2UiOiJjYXJlZXJzIiwiYnVmaWx0ZXIiOi0xLCJjdXN0b21GaWVsZHMiOnt9fQ=%3D",
        "https://careers.swiggy.com/#/careers?src%3Dcareers%26p%3DeyJwYWdlVHlwZSI6ImpkIiwiY3ZTb3VyY2UiOiJjYXJlZXJzIiwicmVxSWQiOjUxMzcsInJlcXVlc3RlciI6eyJpZCI6IiIsImNvZGUiOiIiLCJuYW1lIjoiIn0sInBhZ2UiOiJjYXJlZXJzIiwiYnVmaWx0ZXIiOi0xLCJjdXN0b21GaWVsZHMiOnt9fQ=%3D",
        "https://careers.swiggy.com/#/careers?src%3Dcareers%26p%3DeyJwYWdlVHlwZSI6ImpkIiwiY3ZTb3VyY2UiOiJjYXJlZXJzIiwicmVxSWQiOjUwNDgsInJlcXVlc3RlciI6eyJpZCI6IiIsImNvZGUiOiIiLCJuYW1lIjoiIn0sInBhZ2UiOiJjYXJlZXJzIiwiYnVmaWx0ZXIiOi0xLCJjdXN0b21GaWVsZHMiOnt9fQ=%3D",
        "https://careers.swiggy.com/#/careers?src%3Dcareers%26p%3DeyJwYWdlVHlwZSI6ImpkIiwiY3ZTb3VyY2UiOiJjYXJlZXJzIiwicmVxSWQiOjUwNDcsInJlcXVlc3RlciI6eyJpZCI6IiIsImNvZGUiOiIiLCJuYW1lIjoiIn0sInBhZ2UiOiJjYXJlZXJzIiwiYnVmaWx0ZXIiOi0xLCJjdXN0b21GaWVsZHMiOnt9fQ=%3D",
        "https://careers.swiggy.com/#/careers?src%3Dcareers%26p%3DeyJwYWdlVHlwZSI6ImpkIiwiY3ZTb3VyY2UiOiJjYXJlZXJzIiwicmVxSWQiOjQ3NDksInJlcXVlc3RlciI6eyJpZCI6IiIsImNvZGUiOiIiLCJuYW1lIjoiIn0sInBhZ2UiOiJjYXJlZXJzIiwiYnVmaWx0ZXIiOi0xLCJjdXN0b21GaWVsZHMiOnt9fQ=%3D",
        "https://careers.swiggy.com/#/careers?src%3Dcareers%26p%3DeyJwYWdlVHlwZSI6ImpkIiwiY3ZTb3VyY2UiOiJjYXJlZXJzIiwicmVxSWQiOjQ1ODgsInJlcXVlc3RlciI6eyJpZCI6IiIsImNvZGUiOiIiLCJuYW1lIjoiIn0sInBhZ2UiOiJjYXJlZXJzIiwiYnVmaWx0ZXIiOi0xLCJjdXN0b21GaWVsZHMiOnt9fQ=%3D",
        "https://careers.swiggy.com/#/careers?src%3Dcareers%26p%3DeyJwYWdlVHlwZSI6ImpkIiwiY3ZTb3VyY2UiOiJjYXJlZXJzIiwicmVxSWQiOjQ1MTksInJlcXVlc3RlciI6eyJpZCI6IiIsImNvZGUiOiIiLCJuYW1lIjoiIn0sInBhZ2UiOiJjYXJlZXJzIiwiYnVmaWx0ZXIiOi0xLCJjdXN0b21GaWVsZHMiOnt9fQ=%3D",
        "https://careers.swiggy.com/#/careers?src%3Dcareers%26p%3DeyJwYWdlVHlwZSI6ImpkIiwiY3ZTb3VyY2UiOiJjYXJlZXJzIiwicmVxSWQiOjQzNzQsInJlcXVlc3RlciI6eyJpZCI6IiIsImNvZGUiOiIiLCJuYW1lIjoiIn0sInBhZ2UiOiJjYXJlZXJzIiwiYnVmaWx0ZXIiOi0xLCJjdXN0b21GaWVsZHMiOnt9fQ=%3D",
        "https://careers.swiggy.com/#/careers?src%3Dcareers%26p%3DeyJwYWdlVHlwZSI6ImpkIiwiY3ZTb3VyY2UiOiJjYXJlZXJzIiwicmVxSWQiOjQzNjgsInJlcXVlc3RlciI6eyJpZCI6IiIsImNvZGUiOiIiLCJuYW1lIjoiIn0sInBhZ2UiOiJjYXJlZXJzIiwiYnVmaWx0ZXIiOi0xLCJjdXN0b21GaWVsZHMiOnt9fQ=%3D",
        "https://careers.swiggy.com/#/careers?src%3Dcareers%26p%3DeyJwYWdlVHlwZSI6ImpkIiwiY3ZTb3VyY2UiOiJjYXJlZXJzIiwicmVxSWQiOjQzNjcsInJlcXVlc3RlciI6eyJpZCI6IiIsImNvZGUiOiIiLCJuYW1lIjoiIn0sInBhZ2UiOiJjYXJlZXJzIiwiYnVmaWx0ZXIiOi0xLCJjdXN0b21GaWVsZHMiOnt9fQ=%3D",
        "https://careers.swiggy.com/#/careers?src%3Dcareers%26p%3DeyJwYWdlVHlwZSI6ImpkIiwiY3ZTb3VyY2UiOiJjYXJlZXJzIiwicmVxSWQiOjQzNTMsInJlcXVlc3RlciI6eyJpZCI6IiIsImNvZGUiOiIiLCJuYW1lIjoiIn0sInBhZ2UiOiJjYXJlZXJzIiwiYnVmaWx0ZXIiOi0xLCJjdXN0b21GaWVsZHMiOnt9fQ=%3D",
        "https://careers.swiggy.com/#/careers?src%3Dcareers%26p%3DeyJwYWdlVHlwZSI6ImpkIiwiY3ZTb3VyY2UiOiJjYXJlZXJzIiwicmVxSWQiOjQzMjksInJlcXVlc3RlciI6eyJpZCI6IiIsImNvZGUiOiIiLCJuYW1lIjoiIn0sInBhZ2UiOiJjYXJlZXJzIiwiYnVmaWx0ZXIiOi0xLCJjdXN0b21GaWVsZHMiOnt9fQ=%3D",
        "https://careers.swiggy.com/#/careers?src%3Dcareers%26p%3DeyJwYWdlVHlwZSI6ImpkIiwiY3ZTb3VyY2UiOiJjYXJlZXJzIiwicmVxSWQiOjQyMjAsInJlcXVlc3RlciI6eyJpZCI6IiIsImNvZGUiOiIiLCJuYW1lIjoiIn0sInBhZ2UiOiJjYXJlZXJzIiwiYnVmaWx0ZXIiOi0xLCJjdXN0b21GaWVsZHMiOnt9fQ=%3D",
        "https://careers.swiggy.com/#/careers?src%3Dcareers%26p%3DeyJwYWdlVHlwZSI6ImpkIiwiY3ZTb3VyY2UiOiJjYXJlZXJzIiwicmVxSWQiOjQxNDAsInJlcXVlc3RlciI6eyJpZCI6IiIsImNvZGUiOiIiLCJuYW1lIjoiIn0sInBhZ2UiOiJjYXJlZXJzIiwiYnVmaWx0ZXIiOi0xLCJjdXN0b21GaWVsZHMiOnt9fQ=%3D",
        "https://careers.swiggy.com/#/careers?src%3Dcareers%26p%3DeyJwYWdlVHlwZSI6ImpkIiwiY3ZTb3VyY2UiOiJjYXJlZXJzIiwicmVxSWQiOjQwMjgsInJlcXVlc3RlciI6eyJpZCI6IiIsImNvZGUiOiIiLCJuYW1lIjoiIn0sInBhZ2UiOiJjYXJlZXJzIiwiYnVmaWx0ZXIiOi0xLCJjdXN0b21GaWVsZHMiOnt9fQ=%3D",
        "https://careers.swiggy.com/#/careers?src%3Dcareers%26p%3DeyJwYWdlVHlwZSI6ImpkIiwiY3ZTb3VyY2UiOiJjYXJlZXJzIiwicmVxSWQiOjM5NzQsInJlcXVlc3RlciI6eyJpZCI6IiIsImNvZGUiOiIiLCJuYW1lIjoiIn0sInBhZ2UiOiJjYXJlZXJzIiwiYnVmaWx0ZXIiOi0xLCJjdXN0b21GaWVsZHMiOnt9fQ=%3D",
        "https://careers.swiggy.com/#/careers?src%3Dcareers%26p%3DeyJwYWdlVHlwZSI6ImpkIiwiY3ZTb3VyY2UiOiJjYXJlZXJzIiwicmVxSWQiOjM5MTYsInJlcXVlc3RlciI6eyJpZCI6IiIsImNvZGUiOiIiLCJuYW1lIjoiIn0sInBhZ2UiOiJjYXJlZXJzIiwiYnVmaWx0ZXIiOi0xLCJjdXN0b21GaWVsZHMiOnt9fQ=%3D",
        "https://careers.swiggy.com/#/careers?src%3Dcareers%26p%3DeyJwYWdlVHlwZSI6ImpkIiwiY3ZTb3VyY2UiOiJjYXJlZXJzIiwicmVxSWQiOjM3MjYsInJlcXVlc3RlciI6eyJpZCI6IiIsImNvZGUiOiIiLCJuYW1lIjoiIn0sInBhZ2UiOiJjYXJlZXJzIiwiYnVmaWx0ZXIiOi0xLCJjdXN0b21GaWVsZHMiOnt9fQ=%3D",
        "https://careers.swiggy.com/#/careers?src%3Dcareers%26p%3DeyJwYWdlVHlwZSI6ImpkIiwiY3ZTb3VyY2UiOiJjYXJlZXJzIiwicmVxSWQiOjM2MjgsInJlcXVlc3RlciI6eyJpZCI6IiIsImNvZGUiOiIiLCJuYW1lIjoiIn0sInBhZ2UiOiJjYXJlZXJzIiwiYnVmaWx0ZXIiOi0xLCJjdXN0b21GaWVsZHMiOnt9fQ=%3D",
        "https://careers.swiggy.com/#/careers?src%3Dcareers%26p%3DeyJwYWdlVHlwZSI6ImpkIiwiY3ZTb3VyY2UiOiJjYXJlZXJzIiwicmVxSWQiOjM0MDcsInJlcXVlc3RlciI6eyJpZCI6IiIsImNvZGUiOiIiLCJuYW1lIjoiIn0sInBhZ2UiOiJjYXJlZXJzIiwiYnVmaWx0ZXIiOi0xLCJjdXN0b21GaWVsZHMiOnt9fQ=%3D",
        "https://careers.swiggy.com/#/careers?src%3Dcareers%26p%3DeyJwYWdlVHlwZSI6ImpkIiwiY3ZTb3VyY2UiOiJjYXJlZXJzIiwicmVxSWQiOjMzODQsInJlcXVlc3RlciI6eyJpZCI6IiIsImNvZGUiOiIiLCJuYW1lIjoiIn0sInBhZ2UiOiJjYXJlZXJzIiwiYnVmaWx0ZXIiOi0xLCJjdXN0b21GaWVsZHMiOnt9fQ=%3D",
        "https://careers.swiggy.com/#/careers?src%3Dcareers%26p%3DeyJwYWdlVHlwZSI6ImpkIiwiY3ZTb3VyY2UiOiJjYXJlZXJzIiwicmVxSWQiOjI5MzQsInJlcXVlc3RlciI6eyJpZCI6IiIsImNvZGUiOiIiLCJuYW1lIjoiIn0sInBhZ2UiOiJjYXJlZXJzIiwiYnVmaWx0ZXIiOi0xLCJjdXN0b21GaWVsZHMiOnt9fQ=%3D",
        "https://careers.swiggy.com/#/careers?src%3Dcareers%26p%3DeyJwYWdlVHlwZSI6ImpkIiwiY3ZTb3VyY2UiOiJjYXJlZXJzIiwicmVxSWQiOjI3OTYsInJlcXVlc3RlciI6eyJpZCI6IiIsImNvZGUiOiIiLCJuYW1lIjoiIn0sInBhZ2UiOiJjYXJlZXJzIiwiYnVmaWx0ZXIiOi0xLCJjdXN0b21GaWVsZHMiOnt9fQ=%3D",
        "https://careers.swiggy.com/#/careers?src%3Dcareers%26p%3DeyJwYWdlVHlwZSI6ImpkIiwiY3ZTb3VyY2UiOiJjYXJlZXJzIiwicmVxSWQiOjI0MzksInJlcXVlc3RlciI6eyJpZCI6IiIsImNvZGUiOiIiLCJuYW1lIjoiIn0sInBhZ2UiOiJjYXJlZXJzIiwiYnVmaWx0ZXIiOi0xLCJjdXN0b21GaWVsZHMiOnt9fQ=%3D",
        "https://careers.swiggy.com/#/careers?src%3Dcareers%26p%3DeyJwYWdlVHlwZSI6ImpkIiwiY3ZTb3VyY2UiOiJjYXJlZXJzIiwicmVxSWQiOjIxNTYsInJlcXVlc3RlciI6eyJpZCI6IiIsImNvZGUiOiIiLCJuYW1lIjoiIn0sInBhZ2UiOiJjYXJlZXJzIiwiYnVmaWx0ZXIiOi0xLCJjdXN0b21GaWVsZHMiOnt9fQ=%3D",
        "https://careers.swiggy.com/#/careers?src%3Dcareers%26p%3DeyJwYWdlVHlwZSI6ImpkIiwiY3ZTb3VyY2UiOiJjYXJlZXJzIiwicmVxSWQiOjE3NTgsInJlcXVlc3RlciI6eyJpZCI6IiIsImNvZGUiOiIiLCJuYW1lIjoiIn0sInBhZ2UiOiJjYXJlZXJzIiwiYnVmaWx0ZXIiOi0xLCJjdXN0b21GaWVsZHMiOnt9fQ=%3D",
        "https://careers.swiggy.com/#/careers?src%3Dcareers%26p%3DeyJwYWdlVHlwZSI6ImpkIiwiY3ZTb3VyY2UiOiJjYXJlZXJzIiwicmVxSWQiOjE0MTUsInJlcXVlc3RlciI6eyJpZCI6IiIsImNvZGUiOiIiLCJuYW1lIjoiIn0sInBhZ2UiOiJjYXJlZXJzIiwiYnVmaWx0ZXIiOi0xLCJjdXN0b21GaWVsZHMiOnt9fQ=%3D",
        "https://careers.swiggy.com/#/careers?src%3Dcareers%26p%3DeyJwYWdlVHlwZSI6ImpkIiwiY3ZTb3VyY2UiOiJjYXJlZXJzIiwicmVxSWQiOjcwOCwicmVxdWVzdGVyIjp7ImlkIjoiIiwiY29kZSI6IiIsIm5hbWUiOiIifSwicGFnZSI6ImNhcmVlcnMiLCJidWZpbHRlciI6LTEsImN1c3RvbUZpZWxkcyI6e319=",
        "https://careers.swiggy.com/#/careers?src%3Dcareers%26p%3DeyJwYWdlVHlwZSI6ImpkIiwiY3ZTb3VyY2UiOiJjYXJlZXJzIiwicmVxSWQiOjQ2MiwicmVxdWVzdGVyIjp7ImlkIjoiIiwiY29kZSI6IiIsIm5hbWUiOiIifSwicGFnZSI6ImNhcmVlcnMiLCJidWZpbHRlciI6LTEsImN1c3RvbUZpZWxkcyI6e319=",
        "https://careers.swiggy.com/#/careers?src%3Dcareers%26p%3DeyJwYWdlVHlwZSI6ImpkIiwiY3ZTb3VyY2UiOiJjYXJlZXJzIiwicmVxSWQiOjY4LCJyZXF1ZXN0ZXIiOnsiaWQiOiIiLCJjb2RlIjoiIiwibmFtZSI6IiJ9LCJwYWdlIjoiY2FyZWVycyIsImJ1ZmlsdGVyIjotMSwiY3VzdG9tRmllbGRzIjp7fX0= "]
        data = '{"source":"careers","code":"","filterByBuId":-1}'
        headers = {
            "accept": "application/json, text/plain, */*",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "en-US,en;q=0.9",
            "content-length": "48",
            "content-type": "application/json",
            "origin": "https://careers.swiggy.com",
            "referer": "https://careers.swiggy.com/",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "Windows",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "cross-site",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
            }
        url = requests.post('https://swiggy.mynexthire.com/employer/careers/reqlist/get',headers=headers,data=data)
        json_data = json.loads(url.text)

        for index,item in enumerate(json_data['reqDetailsBOList']):
            urls1 = urls[index]
            job_Id = item['reqId']
            job_title = item['reqTitle']
            location = item['location']
            unit = item['buName']
            discription = item['jdDisplay']
            web_url = "https://careers.swiggy.com/#/careers"
            store =[job_Id,job_title,location,unit,discription,web_url,urls1]
            yield store
def scrape():
    data = fetch_data()
    write_output(data)
scrape()