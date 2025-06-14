class Player: 
    def __init__(self, current_location, has_tool=False, has_crystal=False, score=0, hazard_count=0): 
        self.current_location = current_location  # this is an object
        self.has_tool = has_tool 
        self.has_crystal = has_crystal 
        self.score = score 
        self.hazard_count = hazard_count 
    
    def move(self, direction):   
        if self.current_location.droid_present:  
            self.hazard_count += 1
            return "The droid is blocking your path!"
        elif direction in self.current_location.exits and not self.current_location.droid_present:  
            self.current_location = self.current_location.exits[direction]   
            return f"You move to the {self.current_location.name}" 
        elif direction not in self.current_location.exits: 
            return "You cannot move in that direction" 
    
    def pick_up_tool(self): 
        if self.current_location.has_tool:  
            self.has_tool = True
            self.current_location.remove_tool() 
            self.score += 10 
            return "You picked up the tool!" 
        else: 
            return "There is no tool here." 
    
    def use_tool_on_droid(self, droid): 
        if self.has_tool and self.current_location.droid_present:  
            droid.repair() 
            self.current_location.droid_present = False 
            self.score += 20 
            return "You repaired the droid!"  
        elif not self.has_tool and self.current_location.droid_present: 
            return "You don't have a tool to use on the droid." 
        elif not self.current_location.droid_present: 
            return "There is no droid to repair."  
    
    def pick_up_crystal(self): 
        if self.current_location.has_crystal:  
            self.has_crystal = True
            self.current_location.remove_crystal() 
            self.score += 50 
            return "You picked up the crystal!" 
        else: 
            return "There is no crystal here."  
    
    def get_status(self): 
        return f"Score: {self.score}\nHazards: {self.hazard_count}"
