
class slow_dict:
    
    def __init__(self, init_dict):
        self.data = init_dict.copy()

    
    def waste_linear_time(self):
        s = 0.0
        for i in range(len(self.data)):
            s += i
        return s
    
    def __contains__(self, key):
        self.waste_linear_time()
        return key in self.data
        
    def __getitem__(self, key):
        self.waste_linear_time()
        return self.data[key]
        
    def __setitem__(self, key, value):
        self.waste_linear_time()
        self.data[key] = value
    
