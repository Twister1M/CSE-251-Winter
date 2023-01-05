import threading

count_global = 0

def count(number):
    global count_global
    for x in range(number):
        count_global += 1
        print(f'{x=}')

class MyThread(threading.Thread):
    
    def __init__(self, number):
        
        threading.Thread.__init__(self)
        print(f'{self.name} is being created.\n',end="")
        self.number = number
        self.sum = 0
        
    def run(self):
        
        print(f'{self.name} starting.\n', end="")
        for x in range(10):
            self.sum += 1
        print(f'{self.name} ending.\n', end="")
    
    



def create_threads():
    
    print("-- Process Started --")
    
    t1 = MyThread(10)
    t1.start()
    
    print(f"Final Count = {t1.sum}.")
    
    
    
    pass





if __name__ == "__main__":
    create_threads()
    print("-- End of Program --")