
from xml.etree import ElementTree

def _to_dict(tree):
    """
    I'm aware that we should be careful with big xml files due to recursion applied here.
    """
    if len(tree) > 0:
        return {tree.tag: [_to_dict(child) for child in tree]}
    else:
        return {tree.tag: tree.text or ""}



def xml_to_dict(xml_file):
    """
    Given an xml file-like object, returns the json representation of the xml's tree structure

    Note: I also tried xmltodict and untagled libs but both lack of correct handling of repeated keys.
    I had to fallback to bare xml lib.
    """
    data = xml_file.readlines()
    xml_string = "".join([line.decode('utf-8') for line in data])
    try:
        xml_tree = ElementTree.fromstring(xml_string)
    except ElementTree.ParseError:
        return None
    else:
        return _to_dict(xml_tree)