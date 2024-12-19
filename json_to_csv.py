import json
import os
import pandas as pd

# Set paths
output_dir = "/Users/saraeck/cloud_custodian_env/output"
downloads_dir = "/Users/saraeck/Downloads"

# Walk through all subdirectories to find resources.json files
for root, _, files in os.walk(output_dir):
    for filename in files:
        # Process only resources.json files
        if filename == "resources.json":
            json_path = os.path.join(root, filename)
            print(f"Processing {json_path}")

            # Load JSON data
            with open(json_path) as f:
                data = json.load(f)

            # Flatten JSON data and create a DataFrame
            df = pd.json_normalize(data)

            # Define CSV file path in Downloads
            policy_name = os.path.basename(root)  # Use the policy folder name
            csv_filename = f"{policy_name}_resources.csv"
            csv_path = os.path.join(downloads_dir, csv_filename)

            # Save the DataFrame to CSV
            df.to_csv(csv_path, index=False)
            print(f"Converted {json_path} to {csv_path}")
