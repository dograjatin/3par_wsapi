import logging

import requests  # Module to handle HTTP Requests
from requests import HTTPError
from urllib3.exceptions import InsecureRequestWarning

# To Suppress SSL Warning
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)


class Session:
    def __init__(self, ip, username, password):
        self.ip = ip
        self.username = username
        self.password = password
        self.no_of_cpgs = self.no_of_cpgs()

    # Method Returns the Generates Session Key
    def __get_session_key(self):

        logging.info("\nLOGGING IN TO OBTAIN SESSION KEY\n")
        try:
            session_id_api = "https://" + self.ip + ":8080/api/v1/credentials"
            login_cred = {'user': self.username, 'password': self.password, 'sessionType': 1}
            login = requests.post(session_id_api, json=login_cred, verify=False)
            session_key = login.json()["key"]
            logging.info("\nLOGGED IN: SESSION KEY OBTAINED SUCCESSFULLY\n")
            return session_key

        except Exception as exception:
            logging.debug("\nLogin Failed : Invalid Credentials\n" + exception)
            print("\nLogin Failed : Invalid Credentials\n")

    # Method Quesries the List of all CPGs and return JSON
    def get_all_cpg(self):
        session_key = {"X-HP3PAR-WSAPI-SessionKey": self.__get_session_key()}
        api_url = "https://" + self.ip + ":8080/api/v1/cpgs"

        logging.info("\nQUERYING ALL CPGs\n")
        try:
            data = requests.get(api_url, headers=session_key, verify=False)
            cpg_list_json = data.json()
            return cpg_list_json
        except HTTPError as http_err:
            logging.debug("\nHTTPError:\n" + http_err)
            return http_err

    def no_of_cpgs(self):
        try:
            no_of_cpgs = self.get_all_cpg()["total"]
            return no_of_cpgs
        except HTTPError as http_err:
            logging.debug("\nHTTPError:\n" + http_err)
            return "ErrorValue"
