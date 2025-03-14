def create_shopping_list():
    """
    Create a shopping list by asking the user to input grocery items.
    Stops when the user types "DONE".
    """
    shopping_list = []
    
    while True:
        item = input("Enter a grocery item (type 'DONE' to finish): ").strip()
        
        if item.upper() == "DONE":
            break
        elif item:
            shopping_list.append(item)
        else:
            print("You haven't entered anything. Please try again.")
    
    return shopping_list

def main():
    print("Welcome to the Grocery Shopping List Organizer!")
    
    # Create the shopping list
    shopping_list = create_shopping_list()
    
    # Display the final list
    print("\nYour final shopping list:")
    if shopping_list:
        for idx, item in enumerate(shopping_list, 1):
            print(f"{idx}. {item}")
    else:
        print("No items were added to the shopping list.")

if __name__ == "__main__":
    main()
