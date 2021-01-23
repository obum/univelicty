import datetime
from prettytable import PrettyTable

# TODO. 1: Determine the monthly income

with open("financial.csv", "r") as file:
    header = file.readline()
    del header
    
    # Get the entire dates into a list
    
    original_date_list = []
    formated_date_list = []
    income_list = []
    
    for line in file.readlines():
        
        date_cell = line.split(",")[3]
        
        original_date_list.append(date_cell)
        
        d_year = datetime.datetime.strptime(date_cell, "%m/%d/%Y").strftime("%Y")
        d_month = datetime.datetime.strptime(date_cell, "%m/%d/%Y").strftime("%b")
        
        d_time =  d_year + " - " + d_month
        
        formated_date_list.append(d_time)
        
        income_cell = float(line.split(",")[6])
        income_list.append(income_cell)
    
    unique_date_list = set(formated_date_list) #71
    
    monthly_income = list(zip(formated_date_list, income_list)) # 5061
    
    time_zipper = dict(zip(original_date_list, formated_date_list))

    monthly_income_dict = time_zipper.fromkeys(time_zipper.values(), 0)
    
    for date in unique_date_list:
        for income in monthly_income:
            if date == income[0]:
                monthly_income_dict[date] += round(income[1])
                
    table = PrettyTable(["Payment Month", "Amount"])
    for key, value in monthly_income_dict.items():
        table.add_row([key, (value)])
    print(table)
                
    # print(monthly_income_dict)
                
    
        
    
    
    
        
        
    
    
    
    
        

        
        
        
        
    
    
    