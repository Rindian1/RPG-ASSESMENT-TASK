# Space Station Maintenance Game

A text-based adventure game where you play as a space station technician trying to retrieve a valuable energy crystal while navigating through maintenance tunnels and dealing with a damaged maintenance droid.

## Game Overview

You wake up in the maintenance tunnels of a space station with a mission to retrieve an energy crystal from the docking bay. However, a damaged maintenance droid is blocking your path. You'll need to find a way to repair the droid and safely retrieve the crystal.

## Code Structure

```
RPG-ASSESMENT-TASK/
├── Scripts/
│   ├── Game_Management.py  # Main game controller and logic
│   ├── Player_Management.py  # Player class and actions
│   ├── Location_Management.py  # Location and droid classes
│   ├── Items.py  # Game items and inventory
│   └── main.py  # Entry point
└── Documentation/
    └── (various documentation files)
```

### Key Components

1. **GameController (Game_Management.py)**
   - Manages game state and flow
   - Handles player input and game loop
   - Manages win conditions and scoring

2. **Player (Player_Management.py)**
   - Tracks player state (location, inventory, score)
   - Handles player actions (move, pick up items, use items)
   - Manages hazard encounters and scoring

3. **Location (Location_Management.py)**
   - Represents different areas in the game
   - Manages exits and items in each location
   - Handles droid presence and blocking behavior

4. **Items (Items.py)**
   - Base class for all in-game items
   - Specific items: Diagnostic Tool and Energy Crystal

## Golden Path (Walkthrough)

1. **Starting Point: Maintenance Tunnels**
   - You begin in the dimly lit maintenance tunnels
   - The diagnostic tool is available here
   - Type `pick up tool` to collect it

2. **Repair the Droid**
   - Move east (`move east`) to encounter the damaged droid
   - Use the tool on the droid (`use tool`) to repair it
   - This awards points and clears the path

3. **Retrieve the Crystal**
   - Move east again to reach the Docking Bay
   - Pick up the crystal (`pick up crystal`)
   - This awards more points

4. **Complete the Mission**
   - Type `win` to complete the mission
   - You'll see your final score and hazard count

## Available Commands

- `move [direction]` - Move in a direction (e.g., 'move east')
- `pick up tool` - Pick up the diagnostic tool
- `use tool` - Use the tool on the droid
- `pick up crystal` - Pick up the energy crystal
- `status` - Show current score and hazards
- `help` - Show available commands
- `quit` or `exit` - Quit the game

## Scoring System

- Picking up the tool: +10 points
- Repairing the droid: +20 points
- Picking up the crystal: +50 points
- Completing the mission: +30 points
- Maximum possible score: 110 points

## Running the Game

1. Ensure you have Python 3.x installed
2. Navigate to the Scripts directory
3. Run: `python main.py`

## Development Notes

- The game follows object-oriented programming principles
- Each component is modular for easy extension
- The code includes error handling and input validation