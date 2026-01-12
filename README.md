# AI PLM Change Impact Analyzer

A lightweight Python project that demonstrates a **Product Lifecycle Management (PLM)** model and a simple engine for analyzing the impact of change requests on parts, BOMs, and related documents.

## Project Layout

```
ai-plm-change-impact-analyzer/
├── app.py                # UI entry point (to be expanded)
├── impact_engine.py      # Core logic for change‑impact analysis
├── plm_model/            # Domain model
│   ├── __init__.py
│   ├── part.py
│   ├── bom.py
│   ├── document.py
│   ├── lifecycle.py
│   └── change.py
├── data/                 # Sample JSON data
│   ├── parts.json
│   ├── boms.json
│   └── documents.json
├── requirements.txt      # Python dependencies
└── README.md             # This file
```

## Getting Started

1. **Create a virtual environment (optional but recommended)**  
   ```bash
   python -m venv venv
   source venv/Scripts/activate   # Windows
   # or
   source venv/bin/activate       # macOS/Linux
   ```

2. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the placeholder UI**  
   ```bash
   python app.py