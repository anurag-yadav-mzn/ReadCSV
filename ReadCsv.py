import csv

FILENAME = "sales.csv"

def read_csv_file():
    try:
        with open(FILENAME, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)

            # If the first row is a header, read it separately
            header = next(reader, None)
            if header:
                print("Header:", header)

            print("\nRows:")
            for row in reader:
                print(row)

    except FileNotFoundError:
        print(f"File '{FILENAME}' not found. Make sure it exists in the same folder as this script.")
    except Exception as e:
        print("Error reading CSV file:", e)

# Call Fn
read_csv_file()
