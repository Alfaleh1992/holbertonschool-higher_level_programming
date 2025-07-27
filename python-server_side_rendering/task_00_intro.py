import os

def generate_invitations(template, attendees):
    # Check template type
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return

    # Check if template is empty
    if not template.strip():
        print("Template is empty, no output files generated.")
        return

    # Check attendees type
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Error: Attendees must be a list of dictionaries.")
        return

    # Check if attendees list is empty
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # Ensure 'templates' directory exists
    os.makedirs("templates", exist_ok=True)

    for idx, person in enumerate(attendees):
        content = template
        has_error = False

        for key in ["name", "event_title", "event_date", "event_location"]:
            if key not in person or not person[key]:
                print(f"Missing or empty '{key}' in attendee {idx}, using 'N/A'")
                value = "N/A"
                has_error = True
            else:
                value = str(person[key])
            content = content.replace(f'{{{key}}}', value)

        # Write file even if there were errors
        filename = f"templates/output_{idx}.txt"
        with open(filename, "w") as f:
            f.write(content)
