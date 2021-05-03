from multiprocessing import Process
import time
import os.path
import pickle
def save_data(d, num:str, _class_prod):
    dir = os.path.abspath(os.curdir)
    with open(dir[:-6] + 'data/' + 'data' + num + _class_prod + '.picle', 'wb') as f:
        pickle.dump(d, f)

if __name__ == '__main__':
    save_data('s', '1', 'Proc')
