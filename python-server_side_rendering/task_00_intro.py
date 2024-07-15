import os

def generate_invitations(template, attendees):

    if not isinstance(template, str):
        print("Error: Template must be a string")
        return
    
    if not isinstance(attendees, list):
        print("Error: Attendees must be a list of dictionaries")  
        return

    if template is None or template == '':
        print("Error: Template is empty, no output files generated.")
        return

    if not attendees:
        print("Error: No data provided, no output files generated.")
        return
    
    def get_value(key, attendee):
        return attendee.get(key, "N/A") if attendee.get(key) else "N/A"

    for index, attendee in enumerate(attendees, start=1):
        try:
            update = template.replace("{name}", get_value("name", attendee))
            update = update.replace("{event_title}", get_value("event_title", attendee))
            update = update.replace("{event_date}", get_value("event_date", attendee))
            update = update.replace("{event_location}", get_value("event_location", attendee))
        except AttributeError as e:
            raise TypeError(f"Error replacing placeholders: {e}")

        output_file = f"output_{index}.txt"

        try:
            if not os.path.exists(output_file):           
                with open(output_file, "w") as file:
                    file.write(update) 
            else: 
                print(f"output_file {output_file} already exists.")
        except IOError as e:
            raise IOError("Error to write on {output_file}: {e}")
