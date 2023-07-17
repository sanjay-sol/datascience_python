import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("company_sales_data.csv")
#barplot
profitlist=df['total_profit'].tolist()
monthlist=df['month_number'].tolist()
plt.xlabel('month number')
plt.ylabel('profit in dollar')
plt.xticks(monthlist)
plt.title('company profit per month')
plt.bar(monthlist,profitlist,color='black')
plt.show()
#lineplot
facecream=df['facecream'].tolist()
plt.plot(monthlist,facecream,color='purple')
plt.title('Face Cream Sales Data Per month')
plt.xlabel('Month number')
plt.ylabel('Face Cream Sales')
plt.xticks(monthlist)
plt.show()
#scatter plot
toothpaste=df['toothpaste'].tolist()
plt.scatter(monthlist,toothpaste,label='toothpaste sales',color='orange')
plt.title('Tooth Paste Sales Data per month')
plt.xlabel('Month number')
plt.ylabel('Toothpaste sales')
plt.xticks(monthlist)
plt.show()
#pie chart
label=['face cream','face wash','toothpaste','bathing soap']
salesdata=[df['facecream'].sum(),df['facewash'].sum(),df['toothpaste'].sum(),df['bathingsoap'].sum()]
plt.axis("equal")
plt.pie(salesdata,labels=label,autopct='%1.1f%%')
plt.title('% sales of items sold')
plt.show()
#histogram
total_units=list(df['total_units'])
plt.hist(total_units)
plt.title('Total Profits per month')
plt.show()