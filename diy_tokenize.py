import sys

def diy_tokenize(filename):
    delimiters = ['\n', '\t', '.', ',', ';', '!', '?']   # and ' '
    special_characters = ['%', '$', '&', '(', ')']
    try:
        with open(filename, 'r') as f:
            text = f.read()
            if not text:
                print("no data in file " + filename)
                return False
    except IOError as e:
        print("I/O error({0}): {1}".format(e.errno, e.strerror))
    except: #handle other exceptions such as attribute errors
        print("Unexpected error:", sys.exc_info()[0])  
    
    # split
    for delimiter in delimiters:
        text = text.replace(delimiter,' ')
    text=text.split()

    for special_character in special_characters:
        text = [w.replace(special_character, '') for w in text]

    
    text = [w for w in text if len(w) != 0]

    text = [w.replace("\"", '') if (w[0]=="\"" and w[len(w)-1]=="\"") else w for w in text ]

    text = [w for w in text if len(w) != 0]
    
    text = [w.replace("\'", '') if (w[0]=="\'" and w[len(w)-1]=="\'") else w for w in text ]
    
    text = [w.lower() for w in text]

    return text
    

    


    