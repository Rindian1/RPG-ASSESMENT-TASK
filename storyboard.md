# RPG Storyboard

## Scene 1: Game Start - Maintenance Tunnels

### Location Header
```
=== MAINTENANCE TUNNELS ===
```

### Initial Description
```
You wake up in the dimly lit maintenance tunnels of the space station.
The air hums with the sound of distant machinery.
```

```
What will you do?
> 
```

## Scene 2: Tool Discovery

### Tool Description
```
You see a Diagnostic Tool on the floor.
```

### Player Action
```
> pick up tool
```

### System Response
```
[+10 points] You picked up the Diagnostic Tool.
```

## Scene 3: Droid Encounter

### Droid Description
```
You spot a Damaged Maintenance Droid blocking the east exit.
```

### Player Action
```
> use tool
```

### System Response
```
[+20 points] You repaired the droid! It moves aside, unblocking the east exit.
```

## Scene 4: Moving to Docking Bay

### Player Action
```
> move east
```

### New Location Header
```
=== DOCKING BAY ===
```

### Location Description
```
The docking bay is spacious, with a glowing Energy Crystal on a nearby console.
```

### Available Exits
```
Exits: [west]
```

### Prompt
```
What will you do?
> 
```

## Scene 5: Crystal Collection

### Crystal Description
```
A bright Energy Crystal pulses with energy on the console.
```

### Player Action
```
> pick up crystal
```

### System Response
```
[+50 points] You picked up the Energy Crystal!
```

## Scene 6: Win Condition

### Player Action
```
> win
```

### Win Message
```
[+30 points] Congratulations! You've completed your mission!
```

### Final Score
```
Final Score: 110/110
Hazards encountered: 0
```

## Additional States

### Hazard Encounter

#### Player Action
```
> move east
```

#### Hazard Message
```
The damaged maintenance droid is blocking your path!
Hazard count: 1
```

### Status Check

#### Player Action
```
> status
```

#### Status Display
```
Score: 80/110
Hazards: 1
Current Location: Maintenance Tunnels
Inventory: Diagnostic Tool
```

### Examine Command

#### Player Action
```
> examine tool
```

#### Tool Description
```
A standard issue diagnostic tool. It can be used to repair damaged equipment.
```

### Invalid Command

#### Player Action
```
> jump
```

#### Error Message
```
I don't understand that command. Type 'help' for available commands.
```

## Command List

### Move Command
```
move [direction] - Move between locations
```

### Pick Up Tool Command
```
pick up tool - Pick up diagnostic tool
```

### Use Tool Command
```
use tool - Use tool on droid
```

### Pick Up Crystal Command
```
pick up crystal - Pick up energy crystal
```

### Status Command
```
status - Show score and hazards
```

### Win Command
```
win - Complete the mission (only works in Docking Bay with crystal)
```

### Help Command
```
help - Show available commands
```

## Score System

### Tool Pickup
```
Pick up tool: +10 points
```

### Droid Repair
```
Use tool on droid: +20 points
```

### Crystal Pickup
```
Pick up crystal: +50 points
```

### Game Completion
```
Win game: +30 points
```

### Maximum Score
```
Maximum possible score: 110 points
```
