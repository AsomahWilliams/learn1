import csv
from collections import Counter

def analyze_sales_data(file_path):
    total_revenue = 0.0
    product_counter = Counter()

    try:
        # Open the CSV file
        with open(file_path, mode='r', newline='') as csvfile:
            csv_reader = csv.DictReader(csvfile)

            # Process each row in the CSV
            for row in csv_reader:
                # Accumulate total revenue
                total_revenue += float(row['price'])
                
                # Count occurrences of each product
                product_counter[row['product']] += 1

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return
    except ValueError as e:
        print(f"Error: {e}. Please check the data format.")
        return
    except Exception as e:
        print(f"An error occurred: {e}")
        return

    # Calculate the most frequently purchased product
    if product_counter:
        most_frequent_product = product_counter.most_common(1)[0][0]
    else:
        most_frequent_product = None

    # Print results
    print(f"Total Sales Revenue: ${total_revenue:.2f}")
    print(f"Most Frequently Purchased Product: {most_frequent_product}")

# Example usage
if __name__ == "__main__":
    # Specify the path to the CSV file
    csv_file_path = 'sales_data.csv'  # Change this to your actual file path

    # Analyze the sales data
    analyze_sales_data(csv_file_path)