#!/usr/bin/python3

def generate_invitations(template, attendees):
    # Vérifier les types et le contenu
    if not isinstance(template, str):
        print(f"Error: template should be a string, got {type(template)}")
        return
    if not isinstance(attendees, list)  or not all (isinstance(a, dict) for a in attendees):
        print(f"Error: attendees should be a list of dictionaries")
        return 

    # Gérer les entrées vides
    if template.strip() == "":
        print("Template is empty, no ouptut files generated.")
        return
    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    """
    Traiter chaque participant :
        1. Parcourt de la liste
        2. Pour chaque part particpant, j'ajoute les valeurs
        3. Si valleur manquant -> "N/A"
    """
    for idx, attendee in enumerate(attendees, start=1):
        invitation = template
        invitation = invitation.replace("{name}", str(attendee.get("name") or "N/A"))
        invitation = invitation.replace("{event_title}", str(attendee.get("event_title") or "N/A"))
        invitation = invitation.replace("{event_date}", str(attendee.get("event_date") or "N/A"))
        invitation = invitation.replace("{event_location}", str(attendee.get("event_location") or "N/A"))

    # Générer les fichiers
    output_filename = f"output_{idx}.txt"
    try:
        with open(output_filename, "w") as f:
            f.write(invitation)
        print(f"{output_filename} generated successfully.")
    except Exeption as e:
        print(f"Error writing {output_filename}: {e}")
