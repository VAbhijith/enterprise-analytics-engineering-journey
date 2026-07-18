from datetime import datetime
from data_loader import load_customers

def main():
    print("="*60)
    print("novabank analytics system")
    print("="*60)
    print(f"print Execution Started :, {datetime.now()}")
    print("Loading cutomer data...")
    print("system initialized sucsesfully..")
    customers= load_customers("datasets/customers.csv")

    print("\nCustomer Data Loaded Successfully.\n")
    print(customers.head(5))
    print("\nCustomer Data Info:\n")
    print(customers.info())
    print("customer data description:\n")
    print(customers.describe())
    print("\nCustomer Data Columns:\n")
    print(customers.columns)
    print("\nCustomer Data Types:\n")
    print(customers.dtypes)


    print("\n Total Cstomers Loaded:", len(customers))

if __name__=="__main__":
    main()        