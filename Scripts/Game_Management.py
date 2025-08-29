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
        """Initialize the game world with locations, items, and player"""
        # Create the two main game locations
        self.maintenance_tunnel = Location(
            "Maintenance Tunnels", 
            "You have woken up in the dimly lit maintenance tunnels of the space station. The air hums with the sound of distant machinery.", 
            {"east": None}, 
            has_tool=True, 
            droid_present=True
        )
        
        self.docking_bay = Location(
            "Docking Bay", 
            "The docking bay is spacious, with various equipment along the walls.\nA glowing Energy Crystal rests on a nearby console.", 
            {},  # Exits populated below
            has_crystal=True  # Goal location contains the energy crystal
        )
        self.player = Player(self.maintenance_tunnel)
        self.diagnostic_tool = DiagnosticTool()
        self.energy_crystal = EnergyCrystal()
        self.maintenance_droid = DamagedMaintenanceDroid()
        # Create bidirectional connection between locations
        # This allows movement in both directions once droid is cleared
        self.maintenance_tunnel.exits = {"east": self.docking_bay}
        self.docking_bay.exits = {"west": self.maintenance_tunnel}
    
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
        """Process player input and return appropriate response"""
        command = command.lower().strip()
        
        # Handle movement commands
        if command.startswith("move "):
            direction = command.split(" ", 1)[1]
            return self.player.move(direction)
        
        # Handle other commands
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

=== OBJECTIVE ===
1. Pick up the Diagnostic Tool
2. Use it to repair the Damaged Maintenance Droid
3. Move to the Docking Bay
4. Pick up the Energy Crystal
5. Type 'win' to complete your mission!
        """
        print( help_text.strip())