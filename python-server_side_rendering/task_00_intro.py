import os

def generate_invitations(template, attendees):

    if not isinstance(template, str):
        raise TypeError("Template must be a string")
    
    if not isinstance(attendees, list):
        raise TypeError("Attendees must be a list of dictionaries")  
    
    if not template.strip():
        raise TypeError("Template is empty, no output files generated.")

    if not attendees:
        raise TypeError("No data provided, no output files generated.")
      
    if os.path.exists("template.txt"):
        with open("template.txt", "r") as file:
            template = file.read()
    
    for index, attendee in enumerate(attendees, start=1):
        update = template.replace("{name}", attendee.get("name", "N/A"))
        update = update.replace("{event_title}", attendee.get("event_title", "N/A"))
        update = update.replace("{event_date}", attendee.get("event_date", "N/A"))
        update = update.replace("{event_location}", attendee.get("event_location", "N/A"))

        output_file = f"output_{index}.txt"

        with open(output_file, "w") as file:
            file.write(update) 
