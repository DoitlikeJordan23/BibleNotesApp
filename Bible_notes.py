import csv

#This creates a function named add_verse, which takes the user input and saves it into the created file, Bible_notes.csv.
def add_verse():
    book = input("Enter the book name: ")
    chapter = input("Enter the chapter number: ")
    verse = input("Enter the verse number: ")
    God = input("What does this verse say about God? ")
    man = input("What does this verse say about man? ")
    relationship = input("What does this verse say about the relationship between God and man? ")
    
    with open("Bible_notes.csv", "a", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([book, chapter, verse, God, man, relationship])
    print("Verse added successfully!\n")

#This creates a function search_verses which looks into the saved verses for a specified topic.
def search_verses():
    topic = input("Enter a topic (God, man, or relationship): ")
    with open("Bible_notes.csv", "r") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row[3].lower() == topic.lower() or row[4].lower() == topic.lower() or row[5].lower() == topic.lower():
                print(f"\nBook: {row[0]}")
                print(f"Chapter: {row[1]}")
                print(f"Verse: {row[2]}")
                print(f"God: {row[3]}")
                print(f"Man: {[row[4]}")
                print(f"Relationship: {row[5]}\n")
                
#This creates a function called main, which serves as the entry point of the program and provides the main menu functionality. 
def main():
    print("Welcome to Bible Notes App!")
    
    while True:
        print("1. Add a verse")
        print("2. Search verses by topic")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")
        
        if choice == "1":
            add_verse()
        elif choice == "2":
            search_verses()
        elif choice == "3":
            print("Thank you for using Bible Notes App. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again")
            
if __name__ == "__main__":
    main()
