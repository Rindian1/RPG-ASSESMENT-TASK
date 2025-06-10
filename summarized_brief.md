# Simplified RPG - Summary

## Core Requirements
- Text-based RPG in Python
- Individual development
- OOP principles required
- No AI assistance unless properly documented

## Game Locations
1. Maintenance Tunnels (starting location)
   - Contains DiagnosticTool initially
   - Contains DamagedMaintenanceDroid initially
2. Docking Bay
   - Contains EnergyCrystal initially
   - Win condition location

## Game Objects
1. StationItem (Abstract Base Class)
   - _name
   - _description
   - examine() - abstract method

2. DiagnosticTool (inherits from StationItem)
   - examine() - returns tool description

3. EnergyCrystal (inherits from StationItem)
   - examine() - returns crystal description

4. Location
   - name, description, exits
   - has_tool, has_crystal, droid_present flags
   - Methods: describe(), remove_tool(), remove_crystal(), set_droid_present()

5. DamagedMaintenanceDroid
   - blocking (boolean)
   - repair() - sets blocking to False
   - is_blocking() - returns blocking status

6. Player
   - current_location
   - has_tool, has_crystal (booleans)
   - score, hazard_count
   - Methods: move(), pick_up_tool(), use_tool_on_droid(), pick_up_crystal(), get_status()

7. GameController
   - Manages game state and flow
   - Handles player input
   - Checks win condition

## Game Flow
1. Start in Maintenance Tunnels
2. Pick up Diagnostic Tool (+10 points)
3. Use tool on Damaged Maintenance Droid (+20 points)
4. Move to Docking Bay
5. Pick up Energy Crystal (+50 points)
6. Type "win" in Docking Bay (+30 points)

## Hazard Rule
- Attempting to move east (to Docking Bay) while droid is blocking:
  - Increment hazard counter
  - Display "droid blocking" message

## Commands
- move [direction] - Move between locations
- pick up tool - Pick up diagnostic tool
- use tool - Use tool on droid
- pick up crystal - Pick up energy crystal
- status - Show score and hazards
- win - Complete the mission (only works in Docking Bay with crystal)

## Scoring
- Pick up tool: +10
- Use tool on droid: +20
- Pick up crystal: +50
- Win game: +30
- Max score: 110

## Technical Requirements
- Python implementation
- Object-oriented design
- Input validation
- Clear output messages
- Proper error handling

## Deliverables
1. Complete Python source code
2. Documentation of any AI assistance used
