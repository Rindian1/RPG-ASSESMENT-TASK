class StationItem:
    # Abstracted class for all items
    def __init__(self, _name, _description):
        self._name = _name
        self._description = _description
    
    def examine(self):
        raise NotImplementedError("Subclasses must implement this method")

class DiagnosticTool(StationItem): 
    #Inherits station item
    def __init__(self):
        super().__init__(
            _name="Diagnostic Tool",
            _description="This diagnostic tool seems designed to interface with maintenance droids.")
    
    def examine(self):
        return self._description

class EnergyCrystal(StationItem): 
    #inherits station
    def __init__(self):
        super().__init__(
            _name="Energy Crystal",
            _description="The crystal pulses with an unstable, vibrant energy.")
    
    def examine(self):
        return self._description
