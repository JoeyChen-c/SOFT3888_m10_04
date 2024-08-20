import pandas as pd

def load_excel(file_name):
    """Load the main Excel file."""
    return pd.read_excel(file_name)

def load_csv(file_name):
    """Load a CSV file."""
    return pd.read_csv(file_name)

def save_csv(df, file_name):
    """Save DataFrame to a CSV file."""
    df.to_csv(file_name, index=False)

def add_labels(df, label):
    """Add a label column to the DataFrame."""
    df['Label'] = label
    return df
if __name__ == "__main__":
    # Load the main Excel file (HCR data)
    hcr_data = load_excel('HCR 2023 Preliminary File.xlsx')
    
    # List of universities and their corresponding CSV files
    universities = {
        'Australian National University': 'Incites Researchers - Australian National University.csv',
        'Monash University': 'Incites Researchers - Monash University.csv',
        'University of Adelaide': 'Incites Researchers - University of Adelaide.csv',
        'University of Melbourne': 'Incites Researchers - University of Melbourne.csv',
        'University of New South Wales Sydney': 'Incites Researchers - University of New South Wales Sydney.csv',
        'University of Queensland': 'Incites Researchers - University of Queensland.csv',
        'University of Sydney': 'Incites Researchers - University of Sydney.csv',
        'University of Western Australia': 'Incites Researchers - University of Western Australia.csv'
    }
    print(hcr_data)