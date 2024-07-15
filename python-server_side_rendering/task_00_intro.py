#!/usr/bin/python3

import os

if __name__ == "__main__":

    def generate_invitations(template, attendees):

        if not isinstance(template, str):
            raise TypeError("Template must be a string")
    
        if not isinstance(attendees, list):
            raise TypeError("Attendees must be a list of dictionaries")  
        
        if os.path.exists("template.txt"):
            try:
                with open("template.txt", "r") as file:
                    template = file.read()
            except IOError as e:
                raise IOError(f"Error reading file : {e}")   

        if not template.strip():
            raise TypeError("Template is empty, no output files generated.")

        if not attendees:
            raise TypeError("No data provided, no output files generated.")
    
        for index, attendee in enumerate(attendees, start=1):
            try:
                update = template.replace("{name}", attendee.get("name", "N/A"))
                update = update.replace("{event_title}", attendee.get("event_title", "N/A"))
                update = update.replace("{event_date}", attendee.get("event_date", "N/A"))
                update = update.replace("{event_location}", attendee.get("event_location", "N/A"))
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
