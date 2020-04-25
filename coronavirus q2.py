import xlrd
import matplotlib.pyplot as plt
loc= ("D:\\COVID 19 Hackthon\\americanstates.xlsx")
print("Hello! Do you want to known which state in USA will be right to  study in this corona infected condition")
print("Than you are in perfect place")
print("Here you will know about the detail of deaths in states of USA")
wb=xlrd.open_workbook(loc)
sheet=wb.sheet_by_index(0)
print("These are the states where you must be likeing to to study")
print(sheet.col_values(0))
r=sheet.nrows
c=sheet.ncols
n=int(input("Enter the number which has been asigned to the state where you want to study"))
print("These are the details of deaths of the selected state")
for i in range (1,c):
    print("Deaths in" ,sheet.cell_value(0,i),"years age gaps are",sheet.cell_value(n,i))
print("This is the graph of age vs death of the selected state")
x=[sheet.cell_value(0,i) for i in range (1,c)]
y=[sheet.cell_value(n,i) for i in range (1,c)]
fig = plt.figure(figsize = (10, 5)) 
plt.bar(x, y, color ='red',width = 0.4) 
plt.plot(x,y)
plt.xlabel('age gaps')
plt.ylabel('deaths')
plt.title('Selected state age vs death graph')
plt.show()
print ("Now here is the list of top 10 states acording to the deaths in USA")
for i in range (1,16):
    print(sheet.cell_value(i,0))
