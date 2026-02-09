# HR Reporting Automation Engine 🚀

### Overview
A Python-based automation tool designed to transform manual HR data processing into efficient, professional, and audit-ready Excel reports. This project was developed to bridge the gap between technical data engineering and the specific aesthetic standards of corporate HR reporting.

### Key Problems Solved:
* **Time Inefficiency:** Reduced report generation time from **20 minutes to near-instantaneous** execution.
* **Manual Errors:** Eliminated human risks in data filtering, cleaning, and formatting for 1,000+ records.
* **Inconsistent Formatting:** Achieved 100% fidelity in replicating legacy corporate styles (Navy Blue themes, specific borders, and layouts) to ensure high user adoption.

### Features
- **Modular Data Pipeline:** Handles complex filtering for multiple company entities and departments.
- **Automated Stylist:** Uses `XlsxWriter` to programmatically apply corporate branding (headers, colors, fonts).
- **Smart Column Auto-Fit:** Dynamically adjusts Excel column widths based on the maximum content length.
- **Historical Data Cleaning:** Specifically designed to handle messy data dating back to the 1990s.

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
