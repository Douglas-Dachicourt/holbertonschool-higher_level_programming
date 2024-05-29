#!/usr/bin/python3
"""import xml.etree.ElementTree module"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Function serialize_to_xml:
    This will take a Python dictionary and a filename as parameters.
    It should serialize the dictionary into XML and save it to the given
    filename

    Paramaters:

    - dictionary: A basic Python dictionary


    - filename: the new file xml to create and where we copy xml converted
    data


    """

    root = ET.Element("data")

    for key, value in dictionary.items():
        child_node = ET.Element(key)
        child_node.text = str(value)
        root.append(child_node)

    tree = ET.ElementTree(root)

    with open(filename, "wb") as f:
        tree.write(f, encoding="utf-8", xml_declaration=True)


def deserialize_from_xml(filename):
    """
    Function deserialize_from_xml:
    This will take a filename as its parameter, read the XML data
    from that file, and return a deserialized Python dictionary.

    Paramaters:

    - filename: an xml file


    Return:
    A deserialized Pyyhon dictionary

    """

    tree = ET.parse(filename)
    root = tree.getroot()

    dict = {}

    for child in root:
        child_key = child.tag
        child_value = child.text
        dict[child_key] = child_value

    return dict
