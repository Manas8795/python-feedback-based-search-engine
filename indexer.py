import os 
from preprocessing import preprocess_text

def build_inverted_index(data_dir: str) -> dict:

    """ 
    Builds an inverted index from word -> document that's why it is called inverted the documents are the sample text files in the data directory 
    
    Parameters:
        data_dir -> path of the data directory
    Returning values:
        a dict of inverted index of { word : document } pair 
    """

    inverted_index = {}

    # iterating over all the files 
    for filename in os.listdir(data_dir):

        #files only txt type 
        if not filename.endswith(".txt"):
            continue

        file_path = os.path.join(data_dir,filename)
        
        #reading file content 
        with open(file_path,"r",encoding="utf-8") as file:
            text = file.read()  

        #preprocess the text 
        words = preprocess_text(text)

        # updating the inverted index 
        for word in words: 
            if word not in inverted_index:
                inverted_index[word] = set()

            inverted_index[word].add(filename)

    return inverted_index

