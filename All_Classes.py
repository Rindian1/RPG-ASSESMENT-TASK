class StationItem: 
    def __init__(self, _name, _description): 
        self.name = _name 
        self.description = _description 
    def examine(self): 
        print(self.description) 
class DiagnosticTool(StationItem): 
    def __init__(self):  
        super().__init__(
            _name = "Diagnostic Tool",
             _description = "This diagnostic tool seems designed to interface with maintenance droids.") 
    def examine(self): 
        print(self.description) 
class EnergyCrystal(StationItem): 
    def __init__(self): 
        super().__init__(
            _name = "Energy Crystal",
            _description = "The crystal pulses with an unstable, vibrant energy.") 
    def examine(self): 
        print(self.description) 


class Location: 
    def __init__(self, name, description, exits, has_tool = False, has_crystal = False, droid_present = False): 
        self.name = name 
        self.description = description 
        self.exits = exits 
        self.has_tool = has_tool 
        self.has_crystal = has_crystal 
        self.droid_present = droid_present     
    def describe(self): 
        print(self.description)  
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
        pass

class DamagedMaintenanceDroid: 
    def __init__(self, blocking = True):  
        self.blocking = blocking
    def repair(self): 
        self.blocking = False
    def is_blocking(self): 
        return self.blocking

class Player: 
    def __init__(self, current_location, has_tool = False, has_crystal = False, score = 0, hazard_count = 0): 
        self.current_location = current_location  #this is an object
        self.has_tool = has_tool 
        self.has_crystal = has_crystal 
        self.score = score 
        self.hazard_count = hazard_count 
    def move(self, direction):   
        if self.current_location.droid_present == True:  
            self.hazard_count += 1
            return "The droid is blocking your path!"
        elif direction in self.current_location.exits and self.current_location.droid_present == False:  
            self.current_location = self.current_location.exits[direction]   
            return f"You move to the {self.current_location.name}" 
        elif direction not in self.current_location.exits: 
            return "You can not move in that direction" 
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
        elif self.has_tool == False and self.current_location.droid_present == True: 
            return "You don't have a tool to use on the droid." 
        elif self.current_location.droid_present == False: 
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


class GameController: 
    def __init__(self, maintenance_tunnel, maintenance_droid, docking_bay, player, diagnostic_tool, energy_crystal): 
        self.maintenance_tunnel = maintenance_tunnel 
        self.maintenance_droid = maintenance_droid 
        self.docking_bay = docking_bay 
        self.player = player 
        self.diagnostic_tool = diagnostic_tool 
        self.energy_crystal = energy_crystal 
    def setup_world(self):  
        self.maintenance_tunnel = Location("Maintenance Tunnels", "You wake up in the dimly lit maintenance tunnels of the space station. The air hums with the sound of distant machinery.", {"east": self.docking_bay}, True, False, True) 
        self.docking_bay = Location("Docking Bay", "The docking bay is spacious, with various equipment along the walls. A glowing Energy Crystal rests on a nearby console.", {"west": self.maintenance_tunnel}, False, True, False) 
        self.player = Player(self.maintenance_tunnel)  
        self.diagnostic_tool = DiagnosticTool() 
        self.energy_crystal = EnergyCrystal() 
        self.maintenance_droid = DamagedMaintenanceDroid() 
    def start_game(self): 
        print("Welcome to the Space Station Maintenance Game!") #Expand on this later  
        while True: 
            self.player.current_location.describe()   
            try:
                command = input("What will you do? ")
            except ValueError:
                print("Invalid command.")
            self.process_input(command)  
            if self.check_win_condition(command):
                break
    
            
    def process_input(self, command): 
        marker = command.split()[0]  
        instruction = command.split(" ",1)[1]
        if marker == "move":  
            self.player.move(instruction) 
        elif command == "pick up tool": 
            print(self.player.pick_up_tool()) 
        elif command == "use tool": 
            print(self.player.use_tool_on_droid(self.maintenance_droid)) 
        elif command == "pick up crystal": 
            print(self.player.pick_up_crystal())         
        elif command == "status": 
            print(self.player.get_status()) 
        elif command == "win":  
            pass # figure out what to do here 
        else: 
            print("Invalid command.") 
    def check_win_condition(self, command): 
        if self.player.current_location == self.docking_bay and self.player.has_crystal and command == "win": 
            self.player.score += 30 
            print("You win!") 
            print(f"Final Score: {self.player.score}/110, Total Hazards: {self.player.hazard_count}") 
            return True
        else: 
            return Fa



            
    
        
