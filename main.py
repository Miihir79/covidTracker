import tkinter as tk
import requests
import datetime


def getCovidData():
    api = "https://disease.sh/v3/covid-19/all"
    json_data = requests.get(api).json()
    total_cases = str(json_data['cases'])
    total_deaths = str(json_data['deaths'])
    total_recovered = str(json_data['recovered'])
    total_active = str(json_data['active'])
    critical = str(json_data['critical'])
    cases_today = str(json_data['todayCases'])
    deaths_today = str(json_data['todayDeaths'])
    recovered_today = str(json_data['todayDeaths'])
    time_of_data = json_data['updated']

    date = datetime.datetime.fromtimestamp(time_of_data / 1e3)
    lable.config(
        text="Total cases:" + total_cases + "\nTotal Deaths:" + total_deaths + "\nTotal Recovered:" + total_recovered
             + "\nTotal Active cases:" + total_active + "\nCritical cases:" + critical)

    lable1.config(
        text="Cases Today:" + cases_today + "\n Deaths Today:" + deaths_today + "\n Recovered Today:" + recovered_today)

    lable2.config(text=date)


canvas = tk.Tk()
canvas.geometry("400x400")
canvas.title("Covid Tracker")

f = ("poppins", 15, "bold")
f1 = ("poppins", 17, "bold")

lable = tk.Label(canvas, font=f)
lable.pack(pady=20)

lable1 = tk.Label(canvas, font=f1)
lable1.pack(pady=20)
lable2 = tk.Label(canvas, font=8)
lable2.pack()
button = tk.Button(canvas, font=f, text="Load", command=getCovidData)
button.pack(pady=20)

getCovidData()

canvas.mainloop()
