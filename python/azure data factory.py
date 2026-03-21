def mapping_from_headers(header_list):
    """
    Creates a mapping for Azure Data Factory mapping
    based on a header list.
    """

    mapping = ""
    mapping = """{
    "type": "TabularTranslator",
    "collectionReference": "$['items']",
    "mapComplexValuesToString": False
    "mappings": ["""

    for column in header_list:
        mapping = mapping + """
        {
        "source": {
            "path": "['{0}']"
        },
        "sink": {
            "name": "{0}",
            "type": "String"
        }
        }""".replace("{0}", column)

        if column != header_list[-1]:
            mapping = mapping + ","
    mapping = mapping + "\n  ]\n}"

    return mapping
