# Space Station Maintenance Game

A text-based RPG built in Python demonstrating Object-Oriented Programming principles for SE-11 Software Engineering Assessment.

## Overview

You are a maintenance worker who has awakened in the dimly lit tunnels of a space station. Your mission is to collect the Energy Crystal and complete your maintenance duties. Navigate through the station, repair equipment, and overcome obstacles to succeed.

## Game Features

- **Object-Oriented Design**: Demonstrates inheritance, polymorphism, and encapsulation
- **Interactive Gameplay**: Text-based command interface
- **Score System**: Earn points for completing objectives (max 110 points)
- **Hazard Tracking**: Monitor dangerous encounters
- **Multiple Commands**: Move, examine, pick up items, and more

## Golden Path Walkthrough

1. **Start**: Begin in Maintenance Tunnels
2. **Pick up tool**: `pick up tool` (+10 points)
3. **Repair droid**: `use tool` (+20 points)
4. **Move to bay**: `move east` 
5. **Get crystal**: `pick up crystal` (+50 points)
6. **Complete mission**: `win` (+30 points)

**Total Score**: 110/110 points

## How to Play

### Running the Game
```bash
python main.py
```

### Available Commands
- `move [direction]` - Move between locations (e.g., "move east")
- `pick up tool` - Pick up the diagnostic tool
- `use tool` - Use tool to repair the droid
- `pick up crystal` - Pick up the energy crystal
- `examine [item]` - Examine items in detail
- `status` - View score, hazards, location, and inventory
- `win` - Complete the mission (Docking Bay with crystal only)
- `help` - Show command help
- `quit` or `exit` - End game

### Game Mechanics
- **Movement**: Navigate between Maintenance Tunnels and Docking Bay
- **Obstacles**: Repair the damaged droid to unlock the eastern passage
- **Scoring**: Earn points by completing objectives in the correct sequence
- **Hazards**: Attempting blocked movement increases hazard counter

## File Structure

```
├── main.py                    # Game entry point
├── Game_Management.py         # Main game controller and logic
├── Player_Management.py