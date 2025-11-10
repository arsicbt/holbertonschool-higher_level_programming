#!/usr/bin/python3
"""
Module that generates invitation files
based on a template and attendee data.
"""


def generate_invitations(template, attendees):
    """Generate invitation files for a list of
    attendees using a given template."""
    # Check types and validity
    if not isinstance(template, str):
        print(f"Error: template should be a string, got {type(template)}")
        return

    if (not isinstance(attendees, list) or
            not all(isinstance(a, dict) for a in attendees)):
        print("Error: attendees should be a list of dictionaries")
        return

    # Handle empty inputs
    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return

    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    # Process each attendee
    for idx, attendee in enumerate(attendees, start=1):
        invit = template
        invit = invit.replace("{name}", str(attendee.get("name") or "N/A"))
        invit = invit.replace("{ev_title}",
                              str(attendee.get("event_title") or "N/A"))
        invit = invit.replace("{ev_date}",
                              str(attendee.get("event_date") or "N/A"))
        invit = invit.replace("{ev_location}",
                              str(attendee.get("event_location") or "N/A"))

        # Generate output file
        output_filename = f"output_{idx}.txt"
        try:
            with open(output_filename, "w", encoding="utf-8") as f:
                f.write(invit)
            print(f"{output_filename} generated successfully.")
        except Exception as e:
            print(f"Error writing {output_filename}: {e}")
