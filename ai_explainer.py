from transformers import pipeline

# Instruction-tuned model (CPU friendly)
llm = pipeline(
    "text2text-generation",
    model="google/flan-t5-large",
    max_new_tokens=250,
    temperature=0.2
)

def explain_impact(impact_result: dict) -> dict:
    part = impact_result["part"]
    severity = impact_result["impact_severity"]
    lifecycle_risk = impact_result["lifecycle_risk"]

    reasons = "\n".join(
        f"- {r}" for r in impact_result["impact_reasons"]
    )

#     prompt = f"""
# You are a PLM assistant.

# Do NOT make decisions.
# ONLY explain the provided impact analysis in detail.

# Part: {part.part_number} ({part.name})
# Revision: {part.revision}
# Lifecycle State: {part.lifecycle.value}

# Impact Severity: {severity}
# Lifecycle Risk: {lifecycle_risk}

# Impact Reasons:
# {reasons}

# Explain the impact clearly for a PLM engineer.
# """
    prompt = f'''
You are a PLM assistant.

You must ONLY explain the provided impact analysis.
Do NOT invent new objects or decisions.

Use the following structure exactly:

Summary:
- 2 lines max

Impacted Objects:
- Parts
- BOMs
- Documents

Why This Is High Impact:
- Explain using lifecycle and dependencies

Recommended Next Steps:
- PLM process actions only (no design decisions)

PLM Data:
Part: {part.part_number}
Name: {part.name}
Revision: {part.revision}
Lifecycle: {part.lifecycle.value}

Impact Severity: {severity}
Lifecycle Risk: {lifecycle_risk}

Impact Reasons:
{reasons}

Use standard PLM terminology:
- Engineering Change Order (ECO)
- Released object
- Where-used analysis
- Downstream dependency
- Controlled lifecycle

Rules:
- Do NOT suggest design changes
- Do NOT approve or reject changes
- Do NOT infer missing data
- Only explain what is explicitly provided

'''
    response = llm(prompt)[0]["generated_text"]
    # return response
    return {
        "raw_text": response,
        "severity": severity,
        "lifecycle": part.lifecycle.value
    }
