import json

# Load the original data.json
with open("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# List of models that should be kept in contenttypes
valid_models = {"admin", "auth", "contenttypes", "sessions", "taekwondo"}  # Keep only relevant ones

# Filter out only contenttypes that belong to missing models
cleaned_data = []
for entry in data:
    if entry["model"] == "contenttypes.contenttype":
        app_label = entry["fields"]["app_label"]
        if app_label not in valid_models:
            continue  # Skip this entry

    cleaned_data.append(entry)

# Save the cleaned data to a new file
with open("cleaned_data.json", "w", encoding="utf-8") as f:
    json.dump(cleaned_data, f, indent=2)

print("✅ Cleaned data saved as cleaned_data.json!")
