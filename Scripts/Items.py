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