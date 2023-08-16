from datasets import load_dataset
import json

# Load the dataset from HuggingFace
dataset = load_dataset("xiyuez/im-feeling-curious")

# Create an empty list to store the converted data
converted_data = []

# Loop through each example in the dataset and convert it to the desired JSON format
for example in dataset['train']:
    instruction = "Answer the question as accurately as possible."
    input_text = example['question']
    output_text = example['answer']
    converted_data.append({
        "instruction": instruction,
        "input": input_text,
        "output": output_text
    })

# Save the converted data into a JSON file
output_file = "converted_data.json"
with open(output_file, 'w') as f:
    json.dump(converted_data, f, indent=4)

print(f"Conversion completed. The data has been saved in {output_file}.")
