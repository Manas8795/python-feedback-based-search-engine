import os # to let the user open the files later after the results 
import subprocess # to use xdg to open the files later 
from indexer import build_inverted_index
from search import search

def main():
    # storing the values of every parameter that are needed in the functions of other files 

    data_directory = "data"
    inverted_index = build_inverted_index(data_directory)


    print("Basic Python based search engine")
    print("Type 'exit' to quit.\n")

    while True:
        query = input("Enter the search query: ").strip()
        
        if query.lower() == "exit":
            print("Search engine Signing off")
            break

        if not query:
            print("Please enter a valid query.\n")
            continue

        results = search(query,inverted_index)

        if not results:
            print("No matching results found.\n")
        else:
            print("Search Results:")
            ctr = 1
            for filename,score in results:
                print(f"{ctr}.{filename} - score : {score}")
                ctr+=1
            
            choice = input("\nDo you want to open a file , enter the number if not enter 0 : ").strip().lower()

            if choice.isdigit():
                choice = int(choice)

                if choice == 0:
                # User chose not to open any file
                    pass

                elif 1 <= choice <= len(results):
                    filename = results[choice - 1][0]
                    file_path = os.path.abspath(
                        os.path.join(data_directory, filename)
                    )
                    subprocess.run(["xdg-open", file_path])

                else:
                    print("Invalid file number.\n")
            else:
                print("Please enter a valid number.\n")

            print()

if __name__ ==  "__main__":
    main()
