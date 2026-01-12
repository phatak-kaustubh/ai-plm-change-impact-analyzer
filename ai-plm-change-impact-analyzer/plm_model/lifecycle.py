# Lifecycle rules for parts and documents

class LifecycleRule:
    def __init__(self, rule_id: str, description: str, applicable_to: str):
        self.rule_id = rule_id
        self.description = description
        self.applicable_to = applicable_to  # e.g., 'part', 'document'

    def __repr__(self):
        return f"LifecycleRule(id={self.rule_id}, applies_to={self.applicable_to})"
