from multiprocessing import Pool

def f(name):
    print ('hello', name)

if __name__ == '__main__':
    names = ["bob","sam","mark"]
    pool = Pool(4)
    pool.map(f,names)
