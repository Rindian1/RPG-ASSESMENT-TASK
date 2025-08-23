class Player: 
    def __init__(self, current_location, has_tool=False, has_crystal=False, score=0, hazard_count=0): 
        self.current_location = current_location  # this is an object
        self.has_tool = has_tool 
        self.has_crystal = has_crystal 
        self.score = score 
        self.hazard_count = hazard_count 
    
    def move(self, direction):   
        # Check if trying to move east while droid is blocking (FIXED LOGIC)
        if direction == "east" and self.current_location.droid_present:  
            self.hazard_count += 1
            return "The damaged maintenance droid is blocking your path!\nHazard count: " + str(self.hazard_count)
        elif direction in self.current_location.exits:  
            self.current_location = self.current_location.exits[direction]   
            return f"You move to the {self.current_location.name}." 
        else: 
            return "You cannot move in that direction." 
    
    def pick_up_tool(self): 
        if self.current_location.has_tool:  
            self.has_tool = True
            self.current_location.remove_tool() 
            self.score += 10 
            return "[+10 points] You picked up the Diagnostic Tool." 
        else: 
            return "There is no tool here." 
    
    def use_tool_on_droid(self, droid): 
        if self.has_tool and self.current_location.droid_present:  
            droid.repair() 
            self.current_location.droid_present = False 
            self.score += 20 
            return "[+20 points] You repaired the droid! It moves aside." 
        elif not self.has_tool and self.current_location.droid_present: 
            return "You don't have a tool to use on the droid." 
        else: 
            return "There is no droid to repair."  
    
    def pick_up_crystal(self): 
        if self.current_location.has_crystal:  
            self.has_crystal = True
            self.current_location.remove_crystal() 
            self.score += 50 
            return "[+50 points] You picked up the Energy Crystal!" 
        else: 
            return "There is no crystal here."  
    
    def get_status(self): 
        # Enhanced status display with location and inventory
        inventory_items = []
        if self.has_tool:
            inventory_items.append("Diagnostic Tool")
        if self.has_crystal:
            inventory_items.append("Energy Crystal")
        
        inventory_str = ", ".join(inventory_items) if inventory_items else "Empty"
        
        return (f"=== STATUS ===\n"
                f"Score: {self.score}\n"
                f"Hazards: {self.hazard_count}\n"
                f"Current Location: {self.current_location.name}\n"
                f"Inventory: {inventory_str}")