# Complete implementation of all classes in one file
# This file is kept for compatibility but individual module files are preferred

class StationItem: 
    def __init__(self, _name, _description): 
        self._name = _name 
        self._description = _description 
    
    def examine(self): 
        """Returns the description of the item - to be overridden by subclasses"""
        return self._description

class DiagnosticTool(StationItem): 
    def __init__(self):  
        super().__init__(
            _name="Diagnostic Tool",
            _description="This diagnostic tool seems designed to interface with maintenance droids.") 
    
    def examine(self): 
        """Override to provide specific tool description"""
        return self._description

class EnergyCrystal(StationItem): 
    def __init__(self): 
        super().__init__(
            _name="Energy Crystal",
            _description="The crystal pulses with an unstable, vibrant energy.") 
    
    def examine(self): 
        """Override to provide specific crystal description"""
        return self._description


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

class Player: 
    def __init__(self, current_location, has_tool=False, has_crystal=False, score=0, hazard_count=0): 
        self.current_location = current_location  # this is an object
        self.has_tool = has_tool 
        self.has_crystal = has_crystal 
        self.score = score 
        self.hazard_count = hazard_count 
    
    def move(self, direction):   
        # FIXED: Only block eastward movement when droid is present
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


class GameController: 
    def __init__(self): 
        self.maintenance_tunnel = None
        self.docking_bay = None
        self.maintenance_droid = None
        self.player = None
        self.diagnostic_tool = None
        self.energy_crystal = None
        self.setup_world()
    
    def setup_world(self):  
        """Initialize the game world with locations, items, and player"""
        # Create locations
        self.maintenance_tunnel = Location(
            "Maintenance Tunnels", 
            "You wake up in the dimly lit maintenance tunnels of the space station.\nThe air hums with the sound of distant machinery.", 
            {}, 
            has_tool=True, 
            droid_present=True
        )
        
        self.docking_bay = Location(
            "Docking Bay", 
            "The docking bay is spacious, with various equipment along the walls.\nA glowing Energy Crystal rests on a nearby console.", 
            {}, 
            has_crystal=True
        )
        
        # Set up exits between locations
        self.maintenance_tunnel.exits = {"east": self.docking_bay}
        self.docking_bay.exits = {"west": self.maintenance_tunnel}
        
        # Create items and droid
        self.diagnostic_tool = DiagnosticTool()
        self.energy_crystal = EnergyCrystal()
        self.maintenance_droid = DamagedMaintenanceDroid()
        
        # Create player starting in maintenance tunnels
        self.player = Player(self.maintenance_tunnel)
    
    def start_game(self): 
        """Main game loop"""
        print("=== SPACE STATION MAINTENANCE GAME ===")
        print("Welcome to the Space Station Maintenance Game!")
        print("\nYour mission: Collect the Energy Crystal and escape!")
        print("Type 'help' for available commands.\n")
        
        while True: 
            # Display current location
            print("=" * 50)
            print(f"=== {self.player.current_location.name.upper()} ===")
            print(self.player.current_location.describe())
            
            # Show available exits
            if self.player.current_location.exits:
                exits = ", ".join(self.player.current_location.exits.keys())
                print(f"\nExits: [{exits}]")
            
            # Get and process command
            try:
                command = input("\nWhat will you do?\n> ").strip().lower()
                
                if command in ["quit", "exit"]:
                    print("Thanks for playing!")
                    break
                    
                result = self.process_input(command)
                if result:
                    print(result)
                
                if self.check_win_condition(command):
                    break
                    
            except (EOFError, KeyboardInterrupt):
                print("\nThanks for playing!")
                break
            except Exception as e:
                print("An error occurred. Please try again.")
            
    def process_input(self, command): 
        """Process player input and return appropriate response"""
        command = command.lower().strip()
        
        if command.startswith("move "):
            direction = command.split(" ", 1)[1]
            return self.player.move(direction)
        elif command == "pick up tool": 
            return self.player.pick_up_tool()
        elif command == "use tool": 
            return self.player.use_tool_on_droid(self.maintenance_droid)
        elif command == "pick up crystal": 
            return self.player.pick_up_crystal()
        elif command == "status": 
            return self.player.get_status()
        elif command.startswith("examine "):
            item = command.split(" ", 1)[1]
            return self.examine_item(item)
        elif command == "help":
            return self.show_help()
        elif command == "win":
            return None  # Handled in check_win_condition
        else: 
            return "I don't understand that command. Type 'help' for available commands."
    
    def examine_item(self, item_name):
        """Allow player to examine items (demonstrates polymorphism)"""
        item_name = item_name.lower().strip()
        
        if item_name in ["tool", "diagnostic tool"] and self.player.has_tool:
            return self.diagnostic_tool.examine()
        elif item_name in ["crystal", "energy crystal"] and self.player.has_crystal:
            return self.energy_crystal.examine()
        elif item_name in ["tool", "diagnostic tool"] and self.player.current_location.has_tool:
            return "A standard issue diagnostic tool. It can be used to repair damaged equipment."
        elif item_name in ["crystal", "energy crystal"] and self.player.current_location.has_crystal:
            return "A bright Energy Crystal pulses with energy on the console."
        else:
            return "You don't see that item here."
    
    def check_win_condition(self, command): 
        """Check if the player has won the game"""
        if (self.player.current_location.name == "Docking Bay" and 
            self.player.has_crystal and 
            command == "win"):
            
            self.player.score += 30 
            print("\n" + "=" * 50)
            print("[+30 points] Mission complete!")
            print("\n=== MISSION ACCOMPLISHED ===")
            print("You secured the Energy Crystal and completed your mission!")
            print(f"\nFinal Score: {self.player.score}/110")
            print(f"Hazards encountered: {self.player.hazard_count}")
            print("\nThank you for playing!")
            return True
        elif command == "win":
            return "You cannot win yet. Make sure you're in the Docking Bay with the Energy Crystal."
        
        return False
    
    def show_help(self):
        """Display available commands to the player"""
        help_text = """
=== AVAILABLE COMMANDS ===
  move [direction]     - Move in the specified direction (e.g., 'move east')
  pick up tool         - Pick up the diagnostic tool
  use tool             - Use the diagnostic tool on the droid
  pick up crystal      - Pick up the energy crystal
  examine [item]       - Examine an item (e.g., 'examine tool')
  status               - Show your current score, hazards, location, and inventory
  win                  - Complete the mission (only works in Docking Bay with crystal)
  help                 - Show this help message
  quit/exit            - Quit the game
        """
        return help_text.strip()