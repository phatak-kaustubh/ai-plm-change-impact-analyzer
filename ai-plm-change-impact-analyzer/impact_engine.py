# # Core PLM logic for change impact analysis

# class ImpactEngine:
#     def __init__(self, parts, boms, documents):
#         self.parts = parts
#         self.boms = boms
#         self.documents = documents

#     def analyze_change(self, change_request):
#         """Analyze the impact of a change request.
#         Returns a dictionary with impacted parts, BOMs, and documents.
#         """
#         # Placeholder implementation
#         return {
#             "parts": [],
#             "boms": [],
#             "documents": []
#         }
import json
from plm_model.part import Part
from plm_model.bom import BOM, BOMItem
from plm_model.document import Document
from plm_model.lifecycle import LifecycleState

from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR/"data"

def load_parts():
    with open(DATA_DIR/"parts.json") as f:
        raw = json.load(f)
    return {
        p["part_number"]: Part(
            part_number=p["part_number"],
            name=p["name"],
            revision=p["revision"],
            lifecycle=LifecycleState(p["lifecycle"])
        )
        for p in raw
    }

def load_boms():
    with open(DATA_DIR/"boms.json") as f:
        raw = json.load(f)
    return [
        BOM(
            bom_id=b["bom_id"],
            parent_part=b["parent_part"],
            items=[BOMItem(**i) for i in b["items"]]
        )
        for b in raw
    ]

def load_documents():
    with open(DATA_DIR/"documents.json") as f:
        raw = json.load(f)
    return [
        Document(**d) for d in raw
    ]

def find_where_used(part_number, boms):
    impacted_boms = []

    for bom in boms:
        for item in bom.items:
            if item.part_number == part_number:
                impacted_boms.append(bom)
                break

    return impacted_boms
def find_impacted_documents(part_number, documents):
    return [
        doc for doc in documents
        if doc.related_part == part_number
    ]


from plm_model.lifecycle import can_modify

def assess_lifecycle_risk(part: Part):
    if can_modify(part.lifecycle):
        return "LOW", "Direct modification allowed"
    else:
        return "HIGH", "Released or obsolete part requires formal change"


def classify_impact(part, impacted_boms, impacted_docs):
    severity = "LOW"
    reasons = []

    if impacted_boms:
        severity = "HIGH"
        reasons.append(f"Used in {len(impacted_boms)} active BOM(s)")

    if impacted_docs:
        reasons.append(f"{len(impacted_docs)} related document(s) must be updated")

    return severity, reasons
def analyze_change(part_number):
    parts = load_parts()
    boms = load_boms()
    documents = load_documents()

    part = parts.get(part_number)
    if not part:
        raise ValueError("Part not found")

    impacted_boms = find_where_used(part_number, boms)
    impacted_docs = find_impacted_documents(part_number, documents)

    lifecycle_risk, lifecycle_reason = assess_lifecycle_risk(part)
    impact_severity, impact_reasons = classify_impact(
        part, impacted_boms, impacted_docs
    )

    return {
        "part": part,
        "impact_severity": impact_severity,
        "impact_reasons": impact_reasons,
        "lifecycle_risk": lifecycle_risk,
        "lifecycle_reason": lifecycle_reason,
        "impacted_boms": impacted_boms,
        "impacted_documents": impacted_docs
    }


if __name__ == "__main__":
    result = analyze_change("P-1001")

    print("Impact Severity:", result["impact_severity"])
    print("Lifecycle Risk:", result["lifecycle_risk"])
    print("Reasons:")
    for r in result["impact_reasons"]:
        print("-", r)
