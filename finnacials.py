from prettytable import PrettyTable
financial = open("financial.csv", "r")

# headers = financial.readline().split(",")

# print(headers[5])

company = []
company_tax = {}
tax_line = []


for line in financial.readlines():
    company.append(line.split(",")[5]) # Company tab
    specific_company = set(company)
    all_company = list(specific_company)
    all_company.remove("Customer/Company")

# financial.seek(0)

for company in all_company:
    
    line_list = []
    
    total = 0
    
    financial.seek(0)
    
    for line in financial.readlines():
        
        if "Amount" not in line and company == line.split(",")[5]:
            
            amount = float(line.split(",")[6])
            
            line_list.append(amount)
            
    total = round(sum(line_list))
            
    company_tax[company] = total
    
financial.close()

itera_list = []



for key in company_tax.items():
    itera = zip(company_tax.keys(), company_tax.values())
    
itera = dict(itera)

for key, value in itera.items():
    itera_list.append([key, value])

itera_list.sort(key=lambda x: x[1], reverse = True)

itera = dict(itera_list[0:10])

table = PrettyTable(["Company", "Total Tax Amount"])

for key, value in itera.items():
    table.add_row([key, value])
table.align = "c"

print(table)






# print(company_tax_list[:10])


    

# for each company find the sum of tax and put in a dictionary

# names = ["samuel", "lucas", "mary",]
# ages = [34, 21, 19,]

# zipped_iterable = zip(names, ages)

# print(list(zip(names, ages)))

# print("\n")

# print(dict(zip(names, ages)))

# table = PrettyTable()

# table.add_column('names', names)
# table.add_column('ages', ages)




# print(table)

# print(dict_zipped)

