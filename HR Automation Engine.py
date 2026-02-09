import pandas as pd
import xlsxwriter

# --- AUTOMATED REPORTING ENGINE (GENERAL VERSION) ---
# Aim: Replicating existing corporate report record and styles into automated outputs.

def export_hr_report(df, output_path):
    # Create an ExcelWriter object using xlsxwriter engine
    writer = pd.ExcelWriter(output_path, engine='xlsxwriter')
    df.to_excel(writer, index=False, sheet_name='Employee_Report')

    workbook  = writer.book
    worksheet = writer.sheets['Employee_Report']

    # --- PIXEL-PERFECT FORMATTING ---
    # Replicating Existing Style: Colored Header, White Text, Bold, Double Borders
    header_format = workbook.add_format({
        'bg_color': '#FF00FF',
        'font_color': '#FFFFFF',
        'align': 'center',
        'valign': 'vcenter',
        'bold': True,
        'border': 1,
        'top': 2, # Thick top border
        'bottom': 2
    })

    # Apply formatting to headers
    for col_num, value in enumerate(df.columns.values):
        worksheet.write(0, col_num, value, header_format)

    # --- SMART AUTO-FIT COLUMN WIDTH ---
    # Automatically adjust column width based on content length
    for i, col in enumerate(df.columns):
        column_len = max(df[col].astype(str).str.len().max(), len(col)) + 2
        worksheet.set_column(i, i, column_len)

    writer.close()

    print("Report generated with 100% formatting specification.")



