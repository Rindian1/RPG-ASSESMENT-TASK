class Location: 
    def __init__(self, name, description, exits, has_tool=False, has_crystal=False, droid_present=False): 
        self.name = name 
        self.description = description 
        self.exits = exits 
        self.has_tool = has_tool 
        self.has_crystal = has_crystal 
        self.droid_present = droid_present     
    
    def describe(self): 
        return self.description  
    
    def add_exit(self, direction, location):  
        if direction not in self.exits: 
            self.exits[direction] = location   
        else: 
            print(f"{direction} is already an exit.")
    
    def remove_tool(self):
        if self.has_tool:
            self.has_tool = False
            return True
        return False
        
    def remove_crystal(self):
        if self.has_crystal:
            self.has_crystal = False
            return True
        return False
    
    def set_droid_present(self, flag): 
        self.droid_present = flag

class DamagedMaintenanceDroid: 
    def __init__(self, blocking=True):  
        self.blocking = blocking
    
    def repair(self): 
        self.blocking = False
    
    def is_blocking(self): 
        return self.blocking
