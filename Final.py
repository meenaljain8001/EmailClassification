import pickle
import Creating_dictionary as cd

if __name__ == "__main__":
    print('model loading!')
    filename = "SpamClassification.sav"
    model = pickle.load(open(filename, 'rb'))
    print('model loaded!')

    d = cd.make_dict()
        
    while True:
        
        features = []
        inp = input(">")  #input from the user
        if (inp=="exit"):
            break
        
        for word in d : #make feature vector again
            features.append(inp.count(word[0])) #for every word in dictionary count how many times word occur in input string and append that in features
        
        res = model.predict([features])
        
        if res == 0:
            print('Not Spam!')
        else:
            print('Spam!')

