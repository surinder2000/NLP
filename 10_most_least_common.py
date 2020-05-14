import re
# Function to count the occurance of each word in a paragraph
def count_words(text):
    text = text.lower() # converting whole paragraph into lower case
    pattern = re.compile(r'[\W]+') # remove special characters
    text = pattern.sub(' ', text)
    text = text.split() # convert the paragraph into list by splitting it from space
    d = {}
    # Count the occurance of each word and store it in a dict
    for word in text:
        if word not in d:
            d[word] = 1
        else:
            d[word] += 1
            
    return d

file_name = input("Enter filename:")

with open(file_name,'r') as file:
    text = file.read()
    count = count_words(text); 
    # sort the dict into descending order
    sort_count = sorted(count.items(),key = lambda pair: pair[1], reverse=True)
    # Printing 10 most common words
    print("10 most common words are \nWord\t\tcount")
    for word, count in sort_count[:10]:
        print(f'{word}\t\t{count}')
    
    # Printing 10 least common words
    print("\n10 least common words are \nWord\t\tcount")
    for word, count in sort_count[-10:]:
        print(f'{word}\t\t{count}')


