# Part object definition

class Part:
    def __init__(self, part_id: str, name: str, description: str = ""):
        self.part_id = part_id
        self.name = name
        self.description = description

    def __repr__(self):
        return f"Part(id={self.part_id}, name={self.name})"
