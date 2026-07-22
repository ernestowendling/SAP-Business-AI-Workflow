# SAP Business AI Workflow

An auditable invoice-processing prototype that extracts invoice information, validates business data and produces a controlled approval decision.

The project demonstrates how Python and business AI can support an SAP-oriented accounts-payable workflow while preserving validation logic, exception handling and a traceable audit record.

## Business problem

Invoice processing often requires employees to manually review documents, identify suppliers, compare invoice information with purchase orders and decide whether an invoice can proceed.

This creates several operational risks:

* incomplete or incorrectly captured invoice data;
* invoices linked to unknown or inactive vendors;
* invalid or unavailable purchase orders;
* inconsistent approval decisions;
* limited evidence explaining how a decision was reached;
* excessive manual effort for routine cases.

This prototype structures those checks into a controlled workflow.

## What the application does

The application allows a user to upload an invoice in PDF format.

It then:

1. extracts readable text from the document;
2. identifies relevant invoice fields;
3. validates the supplier;
4. validates the purchase order;
5. applies approval-decision logic;
6. records each processing step in an audit trail;
7. presents the extracted information and final decision in a Streamlit interface.

## Workflow

```text
Invoice PDF
    ↓
Text extraction
    ↓
Invoice field extraction
    ↓
Vendor validation
    ↓
Purchase-order validation
    ↓
Approval decision
    ↓
Audit trail and user output
```

## Control design

The project is built around explicit controls rather than an opaque automated decision.

### PDF-processing control

The workflow checks whether readable text was extracted successfully. A document with no usable text is not passed silently to the next stage.

### Data-extraction control

Extracted invoice fields are displayed so the user can review what the system identified.

### Vendor control

The supplier is checked against the available vendor data or validation rules.

### Purchase-order control

The purchase-order reference is checked before an approval outcome is produced.

### Decision control

The approval decision is determined from the validation results rather than from an unrestricted language-model response.

### Audit-trail control

Each important processing stage records:

* the control or processing step;
* its status;
* an explanatory message.

This provides a visible record of how the workflow progressed and where an exception occurred.

## Example use case

A finance or accounts-payable user uploads an invoice.

The application extracts fields such as:

* invoice number;
* supplier name;
* purchase-order number;
* invoice date;
* invoice amount.

It then checks the supplier and purchase order.

A valid invoice may receive an approval outcome, while an invoice with missing or invalid business data is referred for review.

## Project structure

```text
SAP-Business-AI-Workflow/
│
├── app.py
├── requirements.txt
├── README.md
│
├── utils/
│   ├── parser.py
│   └── audit.py
│
├── validation/
│   └── validator.py
│
├── data/
│   └── sample reference data
│
└── tests/
    └── validation and workflow tests
```

The exact structure may evolve as additional controls and integration components are added.

## Main components

### `app.py`

Runs the Streamlit interface and coordinates the end-to-end workflow.

### `utils/parser.py`

Contains the PDF text-extraction and invoice-field extraction logic.

### `utils/audit.py`

Provides the audit-trail functionality used to record processing steps and control outcomes.

### `validation/validator.py`

Contains the vendor validation, purchase-order validation and approval-decision logic.

## Technology stack

* Python
* Streamlit
* Pandas
* PDF text extraction
* Modular validation logic
* Audit-trail recording
* Git and GitHub

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR-USERNAME/SAP-Business-AI-Workflow.git
cd SAP-Business-AI-Workflow
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it in Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

## Run the application

```bash
streamlit run app.py
```

The application will open in the browser.

## Testing

Run the test suite with:

```bash
pytest
```

Tests should cover, at a minimum:

* valid vendors;
* invalid or unknown vendors;
* valid purchase orders;
* invalid purchase orders;
* missing invoice information;
* approval and review decisions;
* audit-trail entries.

## Sample data

The repository should contain only fictional or anonymised sample information.

Do not upload:

* real invoices;
* personal data;
* confidential supplier records;
* SAP credentials;
* production-system extracts.

## Current limitations

This is a portfolio prototype and not a production SAP integration.

Current limitations may include:

* invoice extraction based on simplified document formats;
* local or sample vendor and purchase-order data;
* no direct connection to SAP;
* no production authentication or role management;
* no automated posting of financial entries;
* limited document-format coverage;
* no human approval interface beyond the prototype workflow.

## Potential development

Future iterations may include:

* SAP API or OData integration;
* confidence scoring for extracted fields;
* duplicate-invoice detection;
* invoice-to-purchase-order amount matching;
* configurable tolerance thresholds;
* human-review queues;
* role-based approval controls;
* structured exception reporting;
* persistent audit storage;
* expanded automated tests;
* containerised deployment.

## Why this project matters

The project is not intended to replace SAP or accounts-payable specialists.

It demonstrates how AI-assisted document processing can be embedded within a controlled business workflow where validation rules, exceptions and decision evidence remain visible.

The objective is to combine automation with the governance standards expected in enterprise and regulated environments.

## Author

**Ernesto Wendling**

Financial-services governance and transformation professional building controlled AI and automation solutions with Python, SAP-oriented workflows and large language models.

[LinkedIn](YOUR-LINKEDIN-URL)
