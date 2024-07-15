import os

attendees = [
    {"name": "Alice", "event_title": "Python Conference", "event_date": "2023-07-15", "event_location": "New York"},
    {"name": "Bob", "event_title": "Data Science Workshop", "event_date": "2023-08-20", "event_location": "San Francisco"},
    {"name": "Charlie", "event_title": "AI Summit", "event_date": None, "event_location": "Boston"}
]

def generate_invitations(template, attendees):
    if type(template) is not str:
        raise TypeError("Template must be a string")
    """
    if type(attendees) is not dict and attendees is not isinstance(attendees, list):
        raise TypeError("Attendees must be a list of dictionaries")
    """    
    if template is None or template == "":
        raise TypeError("Template is empty, no output files generated.")
        
    if isinstance(attendees, list) is None:
        raise TypeError("No data provided, no output files generated.")
      
    if os.path.exists("template.txt"):
        for i in attendees:
                print(i[0])
        
