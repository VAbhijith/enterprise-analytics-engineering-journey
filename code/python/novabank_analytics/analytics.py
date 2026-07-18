def get_city_with_most_customer(customers):
    city_counts = customers["City"].value_counts()
    most_customer_city= city_counts.index[0]
    customer_count = city_counts.iloc[0]
    return most_customer_city, customer_count

def get_customers_with_the_highest_balance(customers):
    """
    Returns the top 3 customers with the highest balance.
    """
    customer_with_highest_balance = customers.sort_values(by=['Balance','Name'],ascending=[False, False])[['Balance','Name']].head(3)
    return customer_with_highest_balance
    