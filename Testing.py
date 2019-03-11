import pickle
import Creating_dictionary as cd
import Dataset as d
import Training as t

def make_dict():
    md = cd.make_dict()
    return d
def make_dataset(md):
    features_data, labels = d.make_dataset(md)
    return features_data, labels

def text_model(features,labels):
    saved_model_name = t.text_model(features,labels)
    return saved_model_name

def load_model(filename):
    
    #load the model
    model = pickle.load(open(filename, 'rb'))
    result = model.score(x_test,y_test)
    return model

if __name__ == "__main__":
    dict = make_dict()
    features,labels = make_dataset(dict)
    model_name = text_model(features,labels)
    
