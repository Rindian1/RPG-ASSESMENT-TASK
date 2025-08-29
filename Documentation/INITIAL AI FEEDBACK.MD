# Part A Assessment Report - REVISED
**Student Code Review - OOP Sci-Fi Text-Based RPG**
**Based on Current Repository Code**

## Overall Grade: **16/25 marks (64%)**

---

## **A1. Functional Implementation & Gameplay Logic: 6/10 marks**

### ✅ **Strengths:**
- **Basic Game Structure (2/4 marks):** Game runs and implements core sequence
- **Command Handling (2/3 marks):** Most required commands work, case-insensitive handling
- **Scoring Mechanics (2/2 marks):** Correct point values (+10, +20, +50, +30) totaling 110
- **Basic Stability (0/1 mark):** Game handles some invalid inputs but has critical bugs

### ❌ **Critical Issues Still Present:**

#### **1. MAJOR BUG - Movement Logic (Lost 2 marks)**
```python
# Current code in Player_Management.py - STILL INCORRECT
def move(self, direction):   
    if self.current_location.droid_present:  # This blocks ALL movement
        self.hazard_count += 1
        return "The droid is blocking your path!"
```

**Problem:** The hazard counter increments for ANY movement attempt when droid is present, not just eastward movement as specified in the requirements.

**Should be:**
```python
if direction == "east" and self.current_location.droid_present:
```

#### **2. Missing Required Messages (Lost 1 mark)**
- Messages don't match the required format from the storyboard
- Missing "[+X points]" format in feedback
- Missing "Hazard count: X" display when blocked

#### **3. Status Command Incomplete (Lost 1 mark)**
```python
def get_status(self): 
    return f"Score: {self.score}\nHazards: {self.hazard_count}"
```
**Missing:** Current location and inventory display as specified in requirements.

---

## **A2. Object-Oriented Design & Principles: 7/10 marks**

### ✅ **Strengths:**
- **Class Implementation (2/2 marks):** All required classes present with correct names
- **Inheritance (2/3 marks):** `DiagnosticTool` and `EnergyCrystal` properly inherit from `StationItem`
- **Encapsulation (2/2 marks):** Proper constructors and attribute management
- **Basic Modularity (1/3 marks):** Code separated into files but some design issues



---

## **A3. Code Craftsmanship & Readability: 3/5 marks**

### ✅ **Strengths:**
- **Naming Conventions (1/2 marks):** Generally consistent variable and method names
- **Basic Structure (1/2 marks):** Code organized into logical modules
- **Comments (1/1 mark):** Minimal but present

### ❌ **Issues:**
- **Inconsistent Return Values (Lost 1 mark):** Some methods return different data types
- **Missing Error Handling (Lost 1 mark):** Limited exception handling for edge cases

---

## **Specific Technical Issues:**

### **1. The Critical Movement Bug**
**Current behavior:** Player cannot move west from Docking Bay back to Maintenance Tunnels if they haven't repaired the droid, because the droid_present flag affects ALL movement.

**Test this:** 
1. Start game
2. Try `move west` (impossible direction) - works correctly
3. Try `move east` with droid present - correctly blocks and increments hazard
4. But the logic will also block other movements incorrectly in other scenarios

### **2. Missing Examine Command**
The `Items.py` file has proper `examine()` methods, but there's no way for the player to use them. This means the polymorphism requirement isn't demonstrated.

### **3. Location.describe() Method Underutilized**
```python
def describe(self): 
    return self.description  # Only returns basic description
```

The GameController manually handles showing items/droid status instead of using the Location's describe method properly.

### **4. Inconsistent Message Formatting**
- Some messages end with periods, others don't
- Missing the required "[+X points]" format from storyboard
- Hazard messages don't match specification

---

## **What Works Well:**

1. **Clean Module Structure:** Good separation of concerns across files
2. **Proper Inheritance:** StationItem hierarchy is correctly implemented  
3. **Game Flow:** Basic gameplay loop functions
4. **Command Processing:** Input handling works for most cases

---

## **What Needs Immediate Fixing:**

### **High Priority (Functional Issues):**
1. **Fix movement logic** - only block eastward movement when droid present
2. **Add examine command** to demonstrate polymorphism
3. **Enhance status display** to include location and inventory
4. **Match required message formats** from storyboard

### **Medium Priority (Quality Issues):**
1. **Improve Location.describe()** to handle all display logic
2. **Add better error handling**
3. **Standardize message formatting**

---

## **Grade Breakdown Comparison:**

| Criterion | Previous Score | Current Score | Change |
|-----------|----------------|---------------|---------|
| A1 (Functional) | 7/10 | 6/10 | -1 (worse) |
| A2 (OOP Design) | 8/10 | 7/10 | -1 (worse) |  
| A3 (Craftsmanship) | 3/5 | 3/5 | 0 (same) |
| **TOTAL** | **18/25** | **16/25** | **-2** |

## **Why the Score Decreased:**

The current repository code has not incorporated the fixes identified in the first assessment. The same critical bugs remain, and some aspects (like demonstrating polymorphism through examine commands) are still missing. The code structure is good, but functional requirements are not fully met.

## **Path to Higher Grade:**

With the fixes I provided earlier, this could easily achieve 22-23/25 marks by addressing:
- Movement logic bug (would gain 2-3 marks)
- Enhanced status display (would gain 1 mark) 
- Examine command implementation (would gain 1-2 marks)
- Message formatting improvements (would gain 1 mark)

**Current Grade: 16/25 (64% - Basic level)**
**Potential with fixes: 22-23/25 (88-92% - Thorough/Extensive level)**