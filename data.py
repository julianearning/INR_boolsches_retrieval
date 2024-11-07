import pandas as pd

class Dictionary:
    def __init__(self, init_data):
        if init_data is not None:
            self.next_id = init_data.max(axis=0)['Doc_ID'] + 1# column AAL's max
            # init data soll pd Dataframe sein, siehe Kap 2 S 16
            self.dictionary=init_data
        else:
            self.next_id = 1
            self.dictionary = pd.DataFrame({'Term': [], 'Doc_ID': [], 'Frequency': []})

    
        
    

class InvertedIndex:
    def __init__(self, init_data):
        invertedindex = {}
        if init_data is not None:
            curr_term = '$'
            doc_list = []
            for index, row in init_data.iterrows():
                if (row['Term'] != curr_term) and (curr_term != '$'):
                    invertedindex[curr_term] = doc_list
                    doc_list = [row['Doc_ID']]
                    curr_term = row['Term']
                elif row['Term'] == curr_term:
                    doc_list.append(row['Doc_ID'])
                elif curr_term == '$':
                    doc_list = [row['Doc_ID']]
                    curr_term = row['Term']

        
            self.invertedindex=invertedindex
        else:
            self.invertedindex = {}

    def basic_intersect(self,term1, term2):
        answer = []
        i = 0
        p1 = self.invertedindex[term1]
        p2 = self.invertedindex[term2]
        while (p1 != None) and (p2 != None):
            if p1 == p2:
                answer.append(p1)
                #p1 
        print("intersect")  
