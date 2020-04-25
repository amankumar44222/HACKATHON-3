import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel ('D:\\COVID 19 Hackthon\\deathduration.xlsx') 
#place "r" before the path string to address special character, such as '\'. Don't forget to put the file name at the end of the path + '.xlsx'
print (df)
def bar(f):
    plt.figure(figsize = (20,30))
    plt.bar(f['Countries'],f['How long did it take to number of confirmed death case to Double(in days)'])
                 #set label
    plt.title('Covid-19 death rate', fontweight = 'bold')
    plt.yticks([5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80])
    plt.ylabel('How long did it take to number of confirmed death case to Double(in days)')
    plt.xlabel('Countries')
    plt.show()
f=pd.read_excel('D:\\COVID 19 Hackthon\\deathduration.xlsx')
bar(f)    