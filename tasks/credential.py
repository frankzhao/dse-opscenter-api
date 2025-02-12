import logging

import common
from config import OpsCenterConfiguration


def create_credential(session_id, config: OpsCenterConfiguration):
    creds_id = None
    credentials_list = common.do_get(config, session_id, 'machine_credentials/')
    for credential in credentials_list['results']:
        if credential['name'] == config.install_credential_name:
            logging.warning("Credential already exists, skipping creation. creds_name: %s", config.install_credential_name)
            creds_id = credential['id']

    if not creds_id:
        machine_credential_response = common.do_post(
            config,
            session_id,
            "machine_credentials/",
            {"name": config.install_credential_name,
             "login-user": config.install_credential_username,
             "become-mode": "sudo",
             "ssh-private-key": config.install_credential_key,
             "use-ssh-keys": True
             }
        )
        creds_id = machine_credential_response['id']
        logging.info("Created credential, machine_credential_id: %s", creds_id)

    return creds_id
