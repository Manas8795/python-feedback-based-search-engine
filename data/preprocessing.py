import string 

# these words does't add meaning to the senten viewed from a searching expreience , so we will remove these words
STOPWORDS = {
        "the ","is","was","a","an","and","or","to","of","in","on","for","which","very","but"
    }

def preprocess_text(text:str) -> list:
    """
    Takes tbe normal raw text as input and then return a clear list of tokens

    Steps:
    1. Convert texts into lowercase.
    2. remove punctaution 
    3. tokenization
    4. remove the stopwords 
    """
    
    # lowercasing
    text = text.lower()

    # removing punctuations
    text = text.translate(str.maketrans("","",string.punctuation))

    # splitting into tokens 
    tokens = text.split()

    # removing stopwords 
    cleaned_tokens = [
            word for word in tokens if word not in STOPWORDS
            ]
    
    # returning the processed keywords only 
    return cleaned_tokens

    
