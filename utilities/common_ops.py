import xml.etree.ElementTree as ET
import test_cases.conftest


class CommonOps:

    @staticmethod
    def get_data(node_name):
        path = test_cases.conftest.get_data_path
        root = ET.parse(path).getroot()
        return root.find(".//" + str(node_name)).text






