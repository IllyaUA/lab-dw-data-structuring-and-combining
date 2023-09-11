import pandas as pd# Your code here
import difflib

# Function to find the closest match in the state_mapping dictionary
def find_closest_match(mapping: dict, real_name: str, threshold: float) -> str:
    best_match = None
    best_ratio = threshold  # Set an initial value based on the threshold
    
    for state, abbreviation in mapping.items():
        ratio = difflib.SequenceMatcher(None, real_name, state).ratio()
        if ratio >= threshold and ratio >= best_ratio:
            best_match = abbreviation
            best_ratio = ratio
    
    if best_match:
        return best_match
    return real_name

def fix_abbreviations(df: pd.DataFrame, mapping: dict, col_name: str, threshold: float) -> pd.DataFrame:
    # Use the apply method to replace values in the specified column
    # Pass the threshold parameter explicitly to find_closest_match
    df[col_name] = df[col_name].apply(lambda x: find_closest_match(mapping, x, threshold))
    return df
