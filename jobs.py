from dill import pickle

def run_dill(d):
    return pickle.loads(d)()