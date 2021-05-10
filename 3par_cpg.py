import logging
from LoginSession import Session

import JsonFIle

if __name__ == '__main__':
    json_filepath = 'C:\\Users\\jatin\\Desktop\\Development\\3par_cpg\\config.json'

    file1 = JsonFIle.JsonFile(json_filepath)
    logging.info("\nReading JSON File\n")
    try:
        data = file1.read_json()
        logging.info("\nJSON FILE READ SUCCESSFULLY\n")
    except Exception as exception:
        logging.debug("\nJSON FILE READ FAILED\n" + exception)

    ipaddress = data["ip"]
    username = data["credentials"]["user"]
    password = data["credentials"]['password']

    logging.info("\nCredential Read \n IP Address: " + ipaddress + "Username: " + username + "Password: " + password)

    logging.info("\nSession Started\n")
    session1 = Session(ipaddress, username, password)
    print(session1.get_all_cpg())

    cpg_number = session1.no_of_cpgs()
    logging.info("\nUPDATING JSON FILE\n")
    try:
        file1.update_json("cpg_number", cpg_number)
        logging.info("\nJSON FILE UPDATED SUCCESSFULLY\n")
    except Exception as exception:
        print("UPDATE JSON FILE FAILED")
        logging.debug("\nUPDATE JSON FILE FAILED\n" + exception)
