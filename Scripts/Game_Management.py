from ast import Break
from Location_Management import Location, DamagedMaintenanceDroid
from Player_Management import Player
from Items import DiagnosticTool, EnergyCrystal

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
        # Create locations
        self.maintenance_tunnel = Location(
            "Maintenance Tunnels", 
            "You have woken up in the dimly lit maintenance tunnels of the space station. The air hums with the sound of distant machinery.", 
            {"east": None}, 
            has_tool=True, 
            droid_present=True
        )
        
        self.docking_bay = Location(
            "Docking Bay", 
            "The docking bay is spacious, with various equipment along the walls. A glowing Energy Crystal rests on a nearby console.", 
            {"west": self.maintenance_tunnel}, 
            has_crystal=True
        )
        
        # Update the exit references now that both locations exist
        self.maintenance_tunnel.exits["east"] = self.docking_bay
        
        # Create items and droid
        self.diagnostic_tool = DiagnosticTool()
        self.energy_crystal = EnergyCrystal()
        self.maintenance_droid = DamagedMaintenanceDroid()
        
        # Create player
        self.player = Player(self.maintenance_tunnel)
    
    def start_game(self): 
        print("Welcome to the Space Station Maintenance Game!")
        print("Available commands: move [direction], pick up tool, use tool, pick up crystal, status, win")
        
        while True: 
            print("\n" + "="*50)
            print(f"=== {self.player.current_location.name.upper()} ===")
            print(self.player.current_location.describe())
            
            # Show available exits
            exits = ", ".join(self.player.current_location.exits.keys())
            print(f"\nExits: [{exits}]")
            
            # Show items in current location
            if self.player.current_location.has_tool:
                print("You see a diagnostic tool on the floor.")
            if self.player.current_location.has_crystal:
                print("You see an energy crystal on a console.")
            if self.player.current_location.droid_present:
                print("A damaged maintenance droid is blocking the way!")
            
            # Get and process command

            command = input("\nWhat will you do? ").strip().lower()
                
            if command == "quit" or command == "exit":
                print("Thanks for playing!")
                break
                    
            if command.startswith("move "):
                direction = command.split(" ", 1)[1]
                print(self.player.move(direction))
            else:
                self.process_input(command)  
                if self.check_win_condition(command):   
                    break
    
    def process_input(self, command): 
        if command == "pick up tool": 
            print(self.player.pick_up_tool())
        elif command == "use tool": 
            print(self.player.use_tool_on_droid(self.maintenance_droid))
        elif command == "pick up crystal": 
            print(self.player.pick_up_crystal())
        elif command == "status": 
            print(self.player.get_status())
        elif command == "help":
            self.show_help()
        elif command == "win": 
            pass
                
        else: 
            print(f"Unknown command: '{command}'")
            print("Invalid command. Type 'help' for available commands.")
        return False

    def check_win_condition(self, command):
        if command != "win": 
            return False
        """Check if the player has won the game"""
        # Check if player is in the docking bay and has the crystal
        if (self.player.current_location.name == "Docking Bay" and 
            self.player.has_crystal): 
            print("\n" + "=" * 50) 
            self.player.score += 30
            print("[+30 points] Mission complete!")
            print("\n=== MISSION ACCOMPLISHED ===")
            print("You secured the Energy Crystal and completed your mission!")
            print(f"\nFinal Score: {self.player.score}/110")
            print(f"Hazards encountered: {self.player.hazard_count}")
            print("\nThank you for playing!")
            return True
            # Access the private score attribute directly since we made it private
        else: 
            print("Win condition not met")
            print("Make sure you're in the Docking Bay with the Energy Crystal.")
            return False
    
    def show_help(self):
        print("\nAvailable commands:")
        print("  move [direction] - Move in the specified direction (e.g., 'move east')")
        print("  pick up tool - Pick up the diagnostic tool")
        print("  use tool - Use the diagnostic tool on the droid")
        print("  pick up crystal - Pick up the energy crystal")
        print("  status - Show your current score and hazard count")
        print("  win - Complete the mission (only works in Docking Bay with crystal)")
        print("  help - Show this help message")
        print("  quit/exit - Quit the game")
