# # BOM (Bill of Materials) structure

# class BOM:
#     def __init__(self, bom_id: str, name: str, parts: list):
#         self.bom_id = bom_id
#         self.name = name
#         self.parts = parts  # list of Part instances

#     def __repr__(self):
#         return f"BOM(id={self.bom_id}, name={self.name}, parts={len(self.parts)})"
from dataclasses import dataclass
from typing import List

@dataclass
class BOMItem:
    part_number: str
    quantity: int

@dataclass
class BOM:
    bom_id: str
    parent_part: str
    items: List[BOMItem]
