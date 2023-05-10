# Import needed libraries
import pandas

# Main function
def export_file(df: pandas.DataFrame, file_path: str, heading: str, footer: str):
    # Open file
    file = open(file_path, "w")
    # Write all text into the file
    file.write(f"{heading}\n\n")
    file.write(f"{df.to_string()}\n\n")
    file.write(footer)
    file.close()