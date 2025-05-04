import csv
import json


def parse_job_data_from_file(input_file, output_file):
    output = []
    with open(input_file, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            role = row["Job titiles"]
            impact = int(row["AI Impact"].replace("%", "").strip())
            output.append({"role": role, "impact": impact})

    # Write to JSON file
    with open(output_file, mode="w", encoding="utf-8") as json_file:
        json.dump(output, json_file, indent=4)


# Example usage
input_csv = "My_Data.csv"  # Replace with your actual input file name
output_json = "ai_job_impact.json"  # Output file

parse_job_data_from_file(input_csv, output_json)
print(f"Output written to {output_json}")
