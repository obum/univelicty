import datetime
from prettytable import PrettyTable

# TODO.1: Determine monthly income

with open("financial.csv") as f:
    header = f.readline()
    del header
    
    date_list = []
    original_date_list = []
    income_list = []
    company_list = []
    
    # Get all the lines in the file
    
    for line in f.readlines():
        
        # get the date column
        date_cell = line.split(",")[3]
        original_date_list.append(date_cell)
        
        # d_year = datetime.datetime.strptime(date_cell, "%m/%d/%Y").strftime("%Y")
        d_month = datetime.datetime.strptime(date_cell, "%m/%d/%Y").strftime("%m")
        # d_time =  d_year +" - "+ d_month 
        new_date_cell = date_cell.replace(date_cell, d_month)
        date_list.append(new_date_cell)
        
        # get the income column
        income_cell = float(line.split(",")[6])
        income_list.append(income_cell)
        
        # get the income column
        
        company = line.split(",")[5]            
        company_list.append(company)

        unique_company = set(company_list)
    
    time_income_zipper = list(zip(original_date_list, income_list))
    time_zipper_list = set(zip(original_date_list, date_list))
    time_zipper = dict(zip(original_date_list, date_list))
    monthly_income = time_zipper.fromkeys(time_zipper.values(), 0)
    monthly_income_diff = time_zipper.fromkeys(time_zipper.values(), 0)

    for date_type in time_zipper_list:
        for time_income in time_income_zipper:
            if date_type[0] == time_income[0]:
                monthly_income[date_type[1]] += time_income[1]
    
    monthly_income_list = []            
                
    for key, value in monthly_income.items():
        monthly_income_list.append([key, round(value)])
    monthly_income_list.sort(key=lambda x: x[0], reverse = False)
    
    monthly_income = dict(monthly_income_list)
    
    # table = PrettyTable(["Payment Month", "Amount"])
    # for key, value in monthly_income.items():
    #     table.add_row([key, round(value)])
    # print(table)
    
# -------------------------------------------------------------------------------------------

# TODO 2 : determine the monthly difference in income

monthly_income_list = [0]

for income in monthly_income.values():
    monthly_income_list.append(income)

index = 0
diff_list = []

while (index < (len(monthly_income_list)-1)):
    diff = round(monthly_income_list[index+1] - monthly_income_list[index])
    diff_list.append(diff)
    index += 1
    
monthly_income_diff = list(zip(monthly_income.keys(), monthly_income.values() ,diff_list))

table = PrettyTable(["Payment Month", "Amount", "Monthly difference in amount"])
for key, value, diff in monthly_income_diff:
    table.add_row([key, value, diff])    
print(table)

# -------------------------------------------------------------------------------------------------------------------

# TODO. 3:  determine the month with the highest and lowest income

    # monthly_income_list.sort(key=lambda x: x[1], reverse = True)

    # monthly_income_list = list(monthly_income_list)
    # last_index = len(monthly_income_list) - 1
    # first_index = 0
    # highest_month = monthly_income_list[first_index][0]
    # f_highest_month = datetime.datetime.strptime(highest_month, "%Y - %m").strftime("%b %Y")
    # lowest_month = monthly_income_list[last_index][0]
    # f_lowest_month = datetime.datetime.strptime(lowest_month, "%Y - %m").strftime("%b %Y")

    # print(f"Month with highest income is {f_highest_month}")
    # print(f"Month with lowest income is {f_lowest_month}")
    
# ----------------------------------------------------------------------------------------------------

# TODO. 4:Seperate all company details into different excel sheet.
    # f.seek(0)
    # header = f.readline()
    # for company in unique_company:
    #     for line in f.readlines():
    #         if company in line or line == header:
    #             with open(f"company/{company}.csv", "a+") as new_file:
    #                 new_file.write(line)
    #     f.seek(0)