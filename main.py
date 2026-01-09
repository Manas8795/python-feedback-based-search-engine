import os # to let the user open the files later after the results 
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
            for filename,score in results:

                # now building all the files as clickable files so first making the path 
                abs_path = os.path.abspath(
                        os.path.join(data_directory,filename)
                        )
                
                #convert into clickable url 
                file_url = f"file;//{abs_path}"

                print(f"- {file_url} (score : {score})")
            print()
if __name__ ==  "__main__":
    main()
