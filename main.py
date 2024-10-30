import json
import csv
import os
from typing import List, Dict, Any

def read_json_data(json_file: str) -> List[Dict[str, Any]]:
    if not os.path.exists(json_file):
        print("File not found.")
        return []
    
    with open(json_file, "r") as file:
        user_data = json.load(file)
        file.close()

    return user_data

def filter_data(user_data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    user_data = [
        user for user in user_data
        if (user["phoneNumber"].startswith("+1") or user["phoneNumber"].startswith("+1")) and "4.0 Safari" in user["userAgent"]
    ]

    return user_data

def write_to_csv(user_data: List[Dict[str, Any]]) -> None:
    with open("out.csv", "w", newline='') as file:
        fieldnames = [
            "name",
            "phoneNumber",
            "email",
            "address",
            "userAgent",
            "hexcolor",
        ]

        writer = csv.DictWriter(file, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)

        writer.writeheader()
        for data in user_data:
            writer.writerow(data)

#

data = read_json_data("in.json")
filtered_data = filter_data(data)
write_to_csv(filtered_data)
