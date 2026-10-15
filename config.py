import os

base_path = os.path.dirname(os.path.abspath(__file__)) + '/'

mock_json_port = os.environ.get('MOCK_JSON_PORT', 8080)
mock_xml_port = os.environ.get('MOCK_XML_PORT', 8090)

service_json_host = os.environ.get('SERVICE_JSON_HOST', 'http://localhost')
service_json_port = os.environ.get('SERVICE_JSON_PORT', 8080)

service_xml_host = os.environ.get('SERVICE_XML_HOST', 'http://localhost')
service_xml_port = os.environ.get('SERVICE_XML_PORT', 8090)

rutube_host_dev = os.environ.get('RUTUBE_HOST', 'https://rutube.dev')
rutube_port_dev = os.environ.get('RUTUBE_PORT', 443)
rutube_get_jwt = os.environ.get('https://rutube.ru:443/api/v3/accounts/phone/login')

rutube_host = os.environ.get('RUTUBE_HOST', 'https://rutube.ru')
rutube_port = os.environ.get('RUTUBE_PORT', 443)
