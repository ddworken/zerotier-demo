import dill

def run_dill(d):
    return dill.loads(d)()