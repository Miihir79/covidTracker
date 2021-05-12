import tkinter as tk
import requests
import datetime


def getCovidData():
    api = "https://disease.sh/v3/covid-19/all"
    apiIndia = "https://disease.sh/v3/covid-19/gov/India"
    json_data = requests.get(api).json()
    json_data_india = requests.get(apiIndia).json()
    total_india_cases = str(json_data_india['total']['todayActive'])
    total_india_today_cases = str(json_data_india['total']['todayCases'])
    total_india_today_deaths = str(json_data_india['total']['todayDeaths'])
    total_india_today_recovered = str(json_data_india['total']['todayRecovered'])
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

    lable3.config(text="\nIndia new active:" + total_india_cases + "\nIndia new cases today:" + total_india_today_cases
                       + "\nIndia new deaths today:" + total_india_today_deaths+ "\nIndia new recoveries today:" + total_india_today_recovered)
    lable2.config(text=date)


canvas = tk.Tk()
canvas.geometry("800x800")
canvas.title("Covid Tracker")

f = ("poppins", 15, "bold")
f1 = ("poppins", 17, "bold")
f2 = ("poppins", 17, "bold")

lable = tk.Label(canvas, font=f)
lable.pack(pady=20)

lable1 = tk.Label(canvas, font=f1)
lable3 = tk.Label(canvas, font=f2)
lable1.pack(pady=20)
lable3.pack(pady=20)
lable2 = tk.Label(canvas, font=8)
lable2.pack()
button = tk.Button(canvas, font=f, text="Load", command=getCovidData)
button.pack(pady=20)

getCovidData()

canvas.mainloop()
