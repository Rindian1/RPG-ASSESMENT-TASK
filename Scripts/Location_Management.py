class Location: 
    def __init__(self, name, description, exits, has_tool=False, has_crystal=False, droid_present=False): 
        self.name = name 
        self.description = description 
        self.exits = exits 
        self.has_tool = has_tool 
        self.has_crystal = has_crystal 
        self.droid_present = droid_present     
    
    def describe(self): 
        """Returns a complete description of the location including items and obstacles"""
        description = self.description
        
        # Add information about items and obstacles
        if self.has_tool:
            description += "\nYou see a diagnostic tool on the floor."
        if self.has_crystal:
            description += "\nYou see an energy crystal on a nearby console."
        if self.droid_present:
            description += "\nA damaged maintenance droid is blocking the way!"
            
        return description
    
    def add_exit(self, direction, location):  
        """Add an exit in the specified direction to another location"""
        if direction not in self.exits: 
            self.exits[direction] = location   
        else: 
            print(f"{direction} is already an exit.")
    
    def remove_tool(self):
        """Remove tool from location if present"""
        if self.has_tool:
            self.has_tool = False
            return True
        return False
        
    def remove_crystal(self):
        """Remove crystal from location if present"""
        if self.has_crystal:
            self.has_crystal = False
            return True
        return False
    
    def set_droid_present(self, flag): 
        """Set whether the droid is present in this location"""
        self.droid_present = flag

class DamagedMaintenanceDroid: 
    def __init__(self, blocking=True):  
        self.blocking = blocking
    
    def repair(self): 
        """Repair the droid, making it no longer blocking"""
        self.blocking = False
    
    def is_blocking(self): 
        """Return whether the droid is still blocking"""
        return self.blocking