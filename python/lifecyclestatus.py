class Lifecyclestatus:
    def __init__(self, i):
        self.__status = i
        self.transitions = {'In Study': ["In Design"], 'In Design': ["In Test"],
                            'In Test': ["In Design", "Rejected", "Active"],
                            'Active': ["Retired", "Launched"], 'Launched': ["Retired"],
                            'Retired': ["Obsolete"], 'Rejected': [], 'Obsolete': [],
                            None: ["In Study", "In Design", "In Test", "Active",
                                   "Launched"]}
        
    def can_transition_from(self, transition):
        return [x for x in self.transitions[self.__status] if x == transition] != []
