from datetime import datetime
from data_loader import load_customers
from logger import logger
from analytics import get_city_with_most_customer,get_customers_with_the_highest_balance

def main():
    print("="*60)
    print("novabank analytics system")
    print("="*60)
    print(f"print Execution Started :, {datetime.now()}")
    print("Loading cutomer data...")
    print("system initialized sucsesfully..")
    customers= load_customers("datasets/customers.csv")

    # print("\nCustomer Data Loaded Successfully.\n")
    logger.info("Customer dataset loaded successfully.")
    print(customers.head(5))
    print("\nCustomer Data Info:\n")
    print(customers.info())
    print("customer data description:\n")
    print(customers.describe())
    print("\nCustomer Data Columns:\n")
    print(customers.columns)
    print("\nCustomer Data Types:\n")
    print(customers.dtypes)
    # print("\n Total Cstomers Loaded:", len(customers))
    total_number_of_customers= len(customers)
    logger.info("Total number of customers loaded: %d", total_number_of_customers)
    active_customers=customers[customers['Status']=='Active']
    logger.info("Total number of Active Customers: %d", len(active_customers))
    inactive_customers=customers[customers["Status"]=='Inactive']
    logger.info("Total number of inactive customers: %d", len(inactive_customers))
    logger.info("=" * 50)
    logger.info("Customer Balance Summary")
    logger.info("=" * 50)
    customer_avg_blance=customers["Balance"].mean()
    logger.info("Average balance: %.2f", customer_avg_blance)
    customer_max_balance= customers["Balance"].max()
    logger.info("Maximum balance: %.2f", customer_max_balance)
    customer_lowest_balance=customers["Balance"].min()
    logger.info("Lowest balance: %.2f", customer_lowest_balance)
    logger.info("=" * 50)
    logger.info("Customer location Summary")
    logger.info("=" * 50)
    most_customer_city, customer_count= get_city_with_most_customer(customers)
    logger.info("City with the most customers: %s (customer count %d)",
                most_customer_city, 
                customer_count )
    logger.info("=" * 50)
    logger.info("Customer Balance Summary")
    logger.info("=" * 50)
    customer_with_highest_balance= get_customers_with_the_highest_balance(customers)
    logger.info("customer with the highest balance: %d",
                customer_with_highest_balance, 
                 )
    

if __name__=="__main__":
    main()        