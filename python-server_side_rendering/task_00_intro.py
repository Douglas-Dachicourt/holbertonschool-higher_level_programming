import os

def generate_invitations(template, attendees):
    if not isinstance(template, str):
        raise TypeError("Template must be a string")
    
    if not isinstance(attendees, list):
        raise TypeError("Attendees must be a list of dictionaries")  
    
    if template is None or template == "":
        raise TypeError("Template is empty, no output files generated.")

    if not attendees:
        raise TypeError("No data provided, no output files generated.")
      
    for attendee in attendees:
        if not isinstance(attendee, dict):
            raise TypeError("Each attendee must be a dictionary")
    
        update = template.replace("{name}", attendee.get("name", "N/A"))
        update = update.replace("{event_title}", attendee.get("event_title", "N/A"))
        update = update.replace("{event_date}", attendee.get("event_date", "N/A"))
        update = update.replace("{event_location}", attendee.get("event_location", "N/A"))


    if os.path.exists("template.txt"):
        with open("output_X.txt", "w") as file:
            file.write(update) 
