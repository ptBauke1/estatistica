import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#pie chart
def pie_chart(data, title):
    plt.figure(figsize=(10, 7))
    plt.pie(data, labels=data.index, autopct='%1.1f%%', startangle=140)
    plt.title(title)
    plt.show()
    
#histogram
def histogram(data, title):
    plt.figure(figsize=(10, 7))
    plt.hist(data, bins=10, alpha=0.7, color='blue')
    plt.title(title)
    plt.show()

def main():
    file = 'Uso_de_Ad-Blockers_no_YouTube_respostas.xlsx'
    df = pd.read_excel(file)
    data = df['Qual é a sua idade?'].value_counts()
    histogram(data, 'Histogram')
    
if __name__ == '__main__':
    main()