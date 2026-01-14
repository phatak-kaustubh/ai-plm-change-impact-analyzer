# # Document / drawing representation

# class Document:
#     def __init__(self, doc_id: str, title: str, doc_type: str, related_parts: list = None):
#         self.doc_id = doc_id
#         self.title = title
#         self.doc_type = doc_type  # e.g., 'drawing', 'specification'
#         self.related_parts = related_parts or []  # list of Part IDs

#     def __repr__(self):
#         return f"Document(id={self.doc_id}, title={self.title}, type={self.doc_type})"
from dataclasses import dataclass

@dataclass
class Document:
    doc_id: str
    title: str
    doc_type: str   # Drawing, Spec, Report
    related_part: str
