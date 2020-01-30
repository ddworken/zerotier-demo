import pickle

def run_pickled_func(d):
    return pickle.loads(d)()