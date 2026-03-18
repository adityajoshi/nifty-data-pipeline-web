import pandas as pd
import io

def generate_excel_from_dataframe(input_df, output_target='NSE_Sectoral_Master_List.xlsx'):
    """
    Takes an input DataFrame containing multiple sectors (identified by a 'Sector' column)
    and writes them to an Excel file with a Summary sheet.
    
    If output_target is None, returns the Excel file as a bytes object (in-memory).
    """
    summary_data = []
    
    # Use BytesIO if output_target is None
    output = output_target if output_target else io.BytesIO()
    
    if input_df is None or input_df.empty:
        if not output_target:
            return output.getvalue()
        return None
        
    # Initialize Excel Writer
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        
        if 'Sector' in input_df.columns:
            # Group by sector and process each
            for sector, df in input_df.groupby('Sector'):
                sheet_name = str(sector)[:31]
                
                # Add to Summary List
                summary_data.append({
                    'Sector Index': str(sector).upper(),
                    'Total Stocks': len(df)
                })
                
                # Write individual sector sheet without the 'Sector' column to match original CSVs
                df.drop(columns=['Sector'], errors='ignore').to_excel(writer, sheet_name=sheet_name, index=False)
        else:
            # Fallback if DataFrame has no Sector column
            input_df.to_excel(writer, sheet_name='Data', index=False)
            summary_data.append({
                'Sector Index': 'DATA',
                'Total Stocks': len(input_df)
            })

        # Create and Write Master Summary Sheet
        summary_df = pd.DataFrame(summary_data)
        summary_df.to_excel(writer, sheet_name='Summary', index=False)
        
        # Move 'Summary' to the first position
        workbook = writer.book
        workbook.worksheets_objs.insert(0, workbook.worksheets_objs.pop())

    if output_target:
        return output_target
    else:
        return output.getvalue()

if __name__ == "__main__":
    # Example test usage:
    dummy_data = pd.DataFrame({
        'Symbol': ['TATA', 'MARUTI', 'HDFC', 'SBI'],
        'Price': [1000, 8000, 1600, 500],
        'Sector': ['niftyauto', 'niftyauto', 'niftybank', 'niftybank']
    })
    
    # This will generate NSE_Sectoral_Master_List.xlsx in the current directory
    generate_excel_from_dataframe(dummy_data)