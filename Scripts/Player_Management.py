class Player: 
    def __init__(self, current_location, has_tool=False, has_crystal=False, score=0, hazard_count=0): 
        self.current_location = current_location  # this is an object
        self.has_tool = has_tool 
        self.has_crystal = has_crystal 
        self.score = score 
        self.hazard_count = hazard_count 
    
    def move(self, direction):   
        if self.current_location.droid_present and direction == "east":  
            self.hazard_count += 1
            print(f"The droid is blocking your path!\nHazard count: {self.hazard_count}")
        elif direction in self.current_location.exits and not self.current_location.droid_present:  
            self.current_location = self.current_location.exits[direction]   
            print(f"You move to the {self.current_location.name}") 
        elif direction not in self.current_location.exits: 
            print("You cannot move in that direction") 
    
    def pick_up_tool(self): 
        if self.current_location.has_tool:  
            self.has_tool = True
            self.current_location.remove_tool() 
            self.score += 10 
            print(f"[+10 points] You picked up the tool!") 
        else: 
            print("There is no tool here.") 
    
    def use_tool_on_droid(self, droid): 
        if self.has_tool and self.current_location.droid_present:  
            droid.repair() 
            self.current_location.droid_present = False 
            self.score += 20 
            print(f"[+20 points] You repaired the droid!")  
        elif not self.has_tool and self.current_location.droid_present: 
            print("You don't have a tool to use on the droid.")
        else: 
            print("There is no droid to repair.")  
    
    def pick_up_crystal(self): 
        if self.current_location.has_crystal:  
            self.has_crystal = True
            self.current_location.remove_crystal() 
            self.score += 50 
            print(f"[+50 points] You picked up the crystal!") 
        else: 
            print("There is no crystal here.")  
    
    def get_status(self): 
        print(f"Score: {self.score}\nHazards: {self.hazard_count} \n Location: {self.current_location.name}\n Has tool: {self.has_tool}\n Has crystal: {self.has_crystal}")
