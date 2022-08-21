"""Generate sales report showing total melons each salesperson sold."""

def sales_report(melons_file):

    sales_report = {}
    # Loop over each line in file object
    filename = open(melons_file)

    for line in filename:
        line = line.rstrip() # Remove trailing whitespace
        entries = line.split('|') # Creat a list data
        #[Betty Anderson, 109, 17]
        salesperson, melons_price, melon_qty = entries
        sales_report[salesperson] = {"total_price": melons_price, "quantity": melon_qty}
    
    for key, value in sales_report.items():
        print(f"{key}: {value}")

        
        # print(value)
    # for key in sales_report.items():
    #     print(key)


    #print(sales_report)

sales_report("/Users/drjafer/src/homework/salesperson-report/sales-report.txt")

# sales_report = {"sales_person_name": ['price','quantity']}
# sales_report = {"sales_person_name": {"price": value, "quantity": value}}