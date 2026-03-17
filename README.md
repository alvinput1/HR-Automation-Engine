# HR Reporting Automation Engine 🚀

### Overview
A Python-based HR data automation system designed to transform manual reporting workflows into scalable, accurate, and audit-ready outputs.

This project bridges the gap between data engineering practices and real-world HR reporting needs, ensuring both technical efficiency and business usability..

Open for opportunities. Contact me at alvinput.perdana@gmail.com or https://www.linkedin.com/in/alvinputrap/

### Key Capabilities:
* **Data Pipeline Automation:** Modular processing for filtering, cleaning, and structuring HR datasets
* **Data Cleaning Engine:** Handles inconsistent and historical HR data
* **Excel Report Generator:** Automated professional formatting using XlsxWriter
* **Dynamic Formatting Logic:** Auto-adjust column widths based on content
* **Corporate Style Replication:** Maintains strict formatting consistency for stakeholder adoption

### Features
- **Modular Data Pipeline:** Handles complex filtering for multiple variables.
- **Automated Stylist:** Uses `XlsxWriter` to programmatically apply corporate branding (headers, colors, fonts).
- **Smart Column Auto-Fit:** Dynamically adjusts Excel column widths based on the maximum content length.
- **Historical Data Cleaning:** Specifically designed to handle messy data.

### Tech Stack
* **Python** (Core Logic)
* **Pandas** (Data Transformation & Cleaning)
* **XlsxWriter** (Professional Excel Formatting)

### How It Works (Snippet)
```python
# The engine ensures the output is always "Ready-to-Present"
header_format = workbook.add_format({
    'bg_color': '#FF00FF',
    'font_color': '#FFFFFF',
    'bold': True,
    'border': 1
})
