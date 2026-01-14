# # Change Request definition

# class ChangeRequest:
#     def __init__(self, change_id: str, description: str, affected_part_ids: list):
#         self.change_id = change_id
#         self.description = description
#         self.affected_part_ids = affected_part_ids  # list of Part IDs that are directly changed

#     def __repr__(self):
#         return f"ChangeRequest(id={self.change_id}, affected_parts={len(self.affected_part_ids)})"
from dataclasses import dataclass

@dataclass
class ChangeRequest:
    cr_id: str
    part_number: str
    description: str
    reason: str
