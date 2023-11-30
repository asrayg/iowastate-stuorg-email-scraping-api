import json

def write_officer_info_to_text(organization_info, output_file):
    with open(output_file, 'w', encoding='utf-8') as text_file:
        text_file.write("Name\tPosition\tEmail Address\n")
        for subtext, officers in organization_info.items():
            for position, info in officers.items():
                if position.lower() != 'advisers':
                    name = info['name']
                    email = info['email']
                    text_file.write(f"{name}\t{position}\t{email}\n")

if __name__ == "__main__":
    input_json_file = "officer_information.json"
    output_text_file = "officer_information.txt"

    with open(input_json_file, 'r', encoding='utf-8') as json_file:
        all_officer_information = json.load(json_file)

    for organization_name, organization_info in all_officer_information.items():
        write_officer_info_to_text(organization_info, output_text_file)

    print(f"Officer information (excluding Advisers) written to {output_text_file}.")
