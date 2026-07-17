# Requirement Gap Analyzer

## Overview

Requirement Gap Analyzer is a Python-based terminal application that helps software teams compare client requirements with implemented features.

The system automatically identifies missing requirements, duplicate entries, ambiguous requirements, project coverage, estimated complexity, and overall project risk.

It assists Business Analysts, Project Managers, Developers, QA Engineers, and Product Owners in ensuring that software implementations align with client expectations.

---

## Features

- Requirement Analysis
- Missing Requirement Detection
- Implemented Feature Detection
- Duplicate Requirement Detection
- Ambiguous Requirement Detection
- Priority Detection
- Requirement Coverage Analysis
- Project Complexity Estimation
- Risk Analysis
- Dashboard
- Report Export
- JSON History Storage

---

## Project Structure

requirement-gap-analyzer/

├── requirement_analyzer.py

├── analyzer_studio.py

├── README.md

└── .gitignore

---

## Requirements

Python 3.x

No external libraries required.

---

## Run

python analyzer_studio.py

---

## Menu

1. Analyze Requirements

2. Detect Duplicate Requirements

3. Detect Ambiguous Requirements

4. Estimate Project Complexity

5. Risk Analysis

6. Dashboard

7. Export Report

8. Clear History

9. Exit

---

## Example

Client Requirements

- User Login
- User Registration
- Email Verification
- Dashboard
- Admin Panel
- Report Export

Implemented Features

- User Login
- Dashboard
- Admin Panel

Output

Coverage : 50%

Implemented

- User Login
- Dashboard
- Admin Panel

Missing

- User Registration
- Email Verification
- Report Export

---

## Dashboard

Displays

- Total Client Requirements
- Implemented Requirements
- Missing Requirements
- Coverage Percentage
- Priority Distribution

---

## Generated Files

analysis_history.json

Stores analysis history.

requirement_gap_report.txt

Stores exported analysis report.

---

## Applications

- Software Requirement Analysis
- Requirement Validation
- Project Planning
- Sprint Planning
- Software Development Lifecycle
- Requirement Traceability
- Business Analysis
- QA Verification

---

## Future Improvements

- Semantic Requirement Matching using Sentence Transformers
- Requirement Similarity Scoring
- Requirement Conflict Detection
- Automatic User Story Generation
- Story Point Estimation
- Sprint Planning Suggestions
- Jira Integration
- Azure DevOps Integration
- GitHub Issues Integration
- Interactive Dashboard
- PDF Report Generation
- AI-Based Requirement Classification
- Requirement Dependency Graph

---

## License

MIT License