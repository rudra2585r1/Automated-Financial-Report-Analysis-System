import re
import matplotlib.pyplot as plt


def generate_trend_chart(text):

    pattern = r"\$([0-9.]+)M"

    numbers = re.findall(pattern, text)

    if len(numbers) >= 3:

        revenues = [float(n) for n in numbers[:3]]

        years = ["2022", "2023", "2024"]

        plt.figure()

        plt.plot(years, revenues, marker="o")

        plt.title("Revenue Trend")
        plt.xlabel("Year")
        plt.ylabel("Revenue (Million USD)")

        plt.grid(True)

        plt.savefig("static/revenue_trend.png")

        plt.close()