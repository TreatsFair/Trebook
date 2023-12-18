import os
import time
from datetime import datetime

HEADERS = ["ISBN", "Author", "Title", "Publisher", "Genre", "Year Published", "Date Purchased", "Status"]
design = '=' * 50
designs = '=' * 230

# Change to your open_file path 
open_file = "books_StudentIDs.txt"

# Clear screen for linux, macOS and windows
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


# Adding book records 
def add_book_records(dict_book):
    duplicate_isbns = [book["ISBN"] for book in dict_book]
    while True:
        # Clears terminal screen
        clear_screen()
        while True:
            # Bolds the text
            print(f"{design}\n\033[1mAdding book record\033[0m\n{design}")
            adding_books_isbn = input("Enter book's ISBN: ")
            if adding_books_isbn.startswith("978") and adding_books_isbn.isdigit() and len(adding_books_isbn) == 13:
                if adding_books_isbn not in duplicate_isbns:
                    adding_books_author = input("Enter book's Author: ").title()
                    if adding_books_author.isalpha():
                        adding_books_title = input("Enter book's Title: ").title()
                        adding_books_publisher = input("Enter book's Publisher: ").title()
                        adding_books_genre = input("Enter book's Genre: ").title()
                        adding_books_year_published = input("Enter book's Year Published [yyyy]: ")
                        adding_books_date_purchased = input("Enter book's Date Purchased [dd-mm-yy]: ")
                        adding_books_status = input("Enter book's Status [read/to-read]: ").lower()
                        break

                    # When book author is inputted in numbers
                    else:
                        print("Please enter proper Book's Author name, no digits.")
                        time.sleep(2)
                        clear_screen()

                # If duplicates are found
                else:
                    print(f"\nBook ISBN {adding_books_isbn} is already found in book records.")
                    time.sleep(2)
                    clear_screen()

            # Invalid ISBN format or number
            else:
                print("Invalid ISBN format.")
                time.sleep(1.4)
                clear_screen()

        # Appending the new book information into a dictionary
        new_book = {
                    "ISBN": adding_books_isbn,
                    "Author": adding_books_author,
                    "Title": adding_books_title,
                    "Publisher": adding_books_publisher,
                    "Genre": adding_books_genre,
                    "Year Published": adding_books_year_published,
                    "Date Purchased": adding_books_date_purchased,
                    "Status": adding_books_status
        }

        # Appending new book information into the dict book
        dict_book.append(new_book)
        print("\n...Adding Book...")
        time.sleep(1)
        
        # Asking user whether to continue adding information or go back to the main menu
        while True:
            clear_screen()
            continuation = input("Continue adding information?\n[y] for yes or [n] for no\n\nSelect option [y or n]: ").lower()
            if continuation == 'y':
                break
            elif continuation == 'n':
                clear_screen()
                print("Going back to the main menu...")
                time.sleep(1)
                return dict_book
            else:
                print("Please enter 'y' or 'n'.")
                time.sleep(1)
                clear_screen()


# Deleting book records
def delete_book_records(dict_book): 
    while True:
        deleted_books = []
        # Setting book_not_found to True, when the book is not found inside the book records
        book_not_found = True
        clear_screen()
        print(f"{design}\n\033[1mDeleting book record\033[0m\n{design}")
        user_delete = input("Please enter the ISBN of the book you want to delete: ")
        clear_screen()

        # Checking for book's ISBN record
        for isbn in dict_book:
            if user_delete == isbn["ISBN"]:
                while True:
                    confirmation = input(f"Are you sure you want to delete book ISBN {user_delete}?\nType [y] to confirm or [n] to cancel\n\nSelect option [y or n]: ").lower()
                    if confirmation == 'y':
                        # Iterating through the dict book and appends all the other books into a list except the one that was specified to be deleted
                        for all in dict_book:
                            if not user_delete == all["ISBN"]:
                                deleted_books.append(all)
                        dict_book = deleted_books
                        clear_screen()
                        break
                    elif confirmation == 'n':
                        clear_screen()
                        break
                    else:
                        clear_screen()
                        print("Invalid input. Please enter [y] or [n]\n\nSelect option [y or n]: ")
                        time.sleep(1.5)
                        clear_screen()

                # Setting a variable to False, when there is a matching book record
                book_not_found = False 

        # if book_not_found is True, it indicates that book was not found 
        if book_not_found:
            print(f"ISBN '{user_delete}' could not be found. Please enter a valid ISBN.\n")

        while True:
            continuation = input("Do you want to continue deleting book(s)?\n[y] for yes or [n] for no\n\nSelect option [y or n]: ").lower()
            if continuation == 'y':
                break
            elif continuation == 'n':
                clear_screen()
                print("Going back to the main menu...")
                time.sleep(1)
                return dict_book
            else:
                print("\nInvalid input. Please enter [y] or [n].")
                time.sleep(1.5)
                clear_screen()

    
# Checking book records
def update_book_records(dict_book):
    clear_screen()
    # Loops until the user inputs one of the given option
    while True:
        print(f"{design}\n\033[1mUpdating book record\033[0m\n{design}")
        user_prompt = input("[1] for ISBN\n[2] for Author and Title\n\nSelect option [1 or 2]: ")
        if not user_prompt in ['1','2']:
            print("\nPlease select one of the options")
            time.sleep(1)
            clear_screen()
        else:
            clear_screen()
            break

    if user_prompt == '1':
        user_wants = input("Enter Book's ISBN: ")
    else:
        user_author = input("Enter Book's Author: ").title()
        user_title = input("Enter Book's Title: ").title()

    #to check whether there is book records 
    recordsFound = False

    # Matching the book's ISBN to the book records
    if user_prompt == '1':
        for dicts in dict_book:
            value = dicts['ISBN']
            if value == user_wants:
                # Set to true as a matching book's record is found
                recordsFound = True
                if_books_found(dicts,dict_book)

    # Matching the book's Author and Title to the book records
    else:
        for dicts in dict_book:
            value = dicts['Author']
            values = dicts['Title']
            if value == user_author and values == user_title:
                # Set to true as a matching book's record is found
                recordsFound = True
                if_books_found(dicts,dict_book)
                

    #if recordsFound = True, This means that there is records found, else print not found
    if not recordsFound:
        if user_prompt == '1':
            print(f"No existing records related to book ISBN: {user_wants}")
        else:
            print(f"No existing records related to book Author: {user_author} and book Title: {user_title}")
    time.sleep(1.4)
    # Returning to main menu
    return


# To check whether user inputed one of the options
def if_books_found(dicts,dict_book):
    while True:
        # Asking user what they would like update
        to_update = input("\nWhat would u like to update?\n[1] for ISBN\n[2] for Author\n[3] for Title\n[4] for Publisher\n[5] for Genre\n[6] for Year Published\n[7] for Date Purchased\n[8] for Status\n\nSelect option [1 to 8]: ")
        if not to_update in ['1','2','3','4','5','6','7','8']:
            print("\nPlease select one of the options")
            time.sleep(1)
            clear_screen()
        else:
            clear_screen()
            break
    updating_book_records(to_update,dicts,dict_book)

# Updating book records
def updating_book_records(to_update,dicts,dict_book):
    match to_update:
        case '1':
            updating_name = "ISBN"
        case '2':
            updating_name = "Author"
        case '3':
            updating_name = "Title"
        case '4':
            updating_name = "Publisher"
        case '5':
            updating_name = "Genre"
        case '6':
            updating_name = "Year Published"
        case '7':
            updating_name = "Date Purchased"
        case '8':
            updating_name = "Status"


    update = input(f"Updating Book's {updating_name} to: ").title()
    # Replacing the old information with the new information of the book
    dicts[updating_name] = update
    clear_screen()
    
    while True:
        continuation = input("Do you want to continue updating current book?\nType 'y' to continue or 'n' to discontinue\n\nSelect option [y or n]: ").lower()
        if continuation in ['y','n']:
            break

    if continuation == 'y':
        clear_screen()
        if_books_found(dicts,dict_book)

    else:
        while True:
            clear_screen()
            continue_updating = input("Would you like to update other books?\nType 'y' for yes or 'n' for no\n\nSelect option [y or n]: ").lower()
            if continue_updating in ['y','n']:
                break

        if continue_updating == 'y':
            clear_screen()
            update_book_records(dict_book)
        else:
            clear_screen()
            print("Going back to the main menu...")
        return

# Displaying book records
def display_book_records(dict_book):
    while True:
        clear_screen()
        print(f"{designs}")
        # Printing each header with a specified format
        for header in HEADERS:
            print(f"| {header:<28}", end = '')
        print(f"\n{designs}", end = '')

        # Setting i to 0, to count for the amount of books
        i = 0
        # Printing each details of the book with a specified format
        for every in dict_book:
            print()
            for line in every.values():
                line = line.strip()
                print(f"| {line:<28}", end = '')
            print()
            i += 1
        print(designs)
        print()

        print(f"Total of {i} book(s).\n")

        # Variable is set to _ as it will not be used, and only used for this sole purpose
        _ = input("Enter any key to return back to the main menu.\n")
        clear_screen()
        print("Going back to the main menu...")
        time.sleep(1)
        return

# Searching for books
def search_for_books(dict_book):
    while True:
        clear_screen()
        while True:
            print(f"{design}\n\033[1mSearching book record(s)\033[0m\n{design}")
            isbn = input("Please enter book's ISBN: ")
            # Checking whether book ISBN is in the correct format
            if isbn.isdigit() and isbn.startswith('978'):
                break
            # If invalid format, it would reprompt again
            else:
                print("\nInvalid ISBN format.")
                time.sleep(1)
                clear_screen()
        author = input("Please enter book's author: ").title()
        title = input("Please input book's title: ").title()

        book_not_found = False

        clear_screen()
        for dict in dict_book:
            # Matching book ISBN, author and title to the book dictionary
            if isbn == dict["ISBN"] and author == dict["Author"] and title == dict["Title"]:
                print(designs)
                for header in HEADERS:
                    print(f"| {header:<25}", end = '')
                print()
                print(designs)
                for values in dict.values():
                    values = values.strip()
                    print(f"| {values:<25}", end = '')
                    book_not_found = True
                print()
                print(designs)
                print()

        # If no matching books were found
        if not book_not_found:
            clear_screen()
            print(f"No existing records found for Book ISBN: {isbn}, Author: {author} and Title: {title}\n")
            time.sleep(1)

        # Asks the user whether to continue searching for books or return to the main menu
        while True:
            continuation = input("Continue searching?\nType 'y' for yes or 'n' for no.\n\nSelect option [y or n]: ").lower()
            if continuation in ['y','n']:
                break
            else:
                clear_screen()
                print("Please input 'y' for yes and 'n' for no.")
                time.sleep(1.4)
                clear_screen()

        if continuation == 'y':
            clear_screen()

        elif continuation == 'n':
            clear_screen()
            print("Going back to the main menu...")
            time.sleep(1.4)
            return

# Exiting the program and only then rewrite the text file with the new informations
def exit(dict_book):
    with open(open_file, 'w') as file:
        for all in dict_book:
            #the .join concatenates a comma at the end of every string and adds a new line after each row
            line = ','.join(all.values()) + '\n' 
            file.write(line)

    clear_screen()
    print(design)
    print("Thank you for using Trebook Management system.")
    print(design)
    time.sleep(1.5)
    clear_screen()
    return
    
# Main menu
def main():
    dict_book = []
    
    # Starts initializing the text file
    try:
        with open(open_file, 'r+') as file:
            # Naming each column in the text file
            for lines in file:
                data = lines.strip().split(',')
                isbn = data[0]
                author = data[1].title()
                title = data[2].title()
                publisher = data[3].title()
                genre = data[4].title()
                year_published = data[5]
                date_purchased = data[6]
                reading_status = data[7]

                # Assigning each row and adding it into the dictionary
                row = {
                        "ISBN": isbn,
                        "Author": author,
                        "Title": title,
                        "Publisher": publisher,
                        "Genre": genre,
                        "Year Published": year_published,
                        "Date Purchased": date_purchased,
                        "Status": reading_status
                    }

                dict_book.append(row)

    except FileNotFoundError:   
        print(f"File '{open_file}' not found.")

    # Get today's date
    today_date = datetime.now().date()

    # Get the day of the week for today
    # Using strftime to get the full weekday name
    day_of_week = datetime.now().strftime("%A")

    # Asks user for input and loops until they enter one of the options
    while True:
        while True:
            clear_screen()
            print(f"{day_of_week}\t\t\t\t\t{today_date}")
            print(f"{design}\n\033[1mTrebook management system\033[0m\n{design}")
            print("What would you like to do?")
            print("1) Add Book Record(s)\n2) Delete Book Record(s)\n3) Update Book Record(s)")
            print("4) Display all Book Record(s)\n5) Search for Book(s)\n6) Exit\n")

            user_option = input("Enter option (1-6): ")
            if user_option in ['1','2','3','4','5','6']:
                break
            else:
                print("Please select one of the options")
                time.sleep(1)
                clear_screen()

        # Matching user option 
        match user_option:
            case '1':
                dict_book = add_book_records(dict_book)
            case '2':
                dict_book = delete_book_records(dict_book)
            case '3':
                update_book_records(dict_book)
            case '4':
                display_book_records(dict_book)
            case '5':
                search_for_books(dict_book) 
            case '6':
                exit(dict_book)
                break


if __name__ == "__main__":
    main()
