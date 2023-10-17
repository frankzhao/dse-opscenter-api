import json
import logging
import os

import requests

from config import OpsCenterConfiguration


def get_session_token(config: OpsCenterConfiguration):
    opscenter_session = os.environ.get('opscenter_session', None)

    if opscenter_session:
        return opscenter_session

    endpoint = "http://%s:8888/login" % config.server_ip

    post_data = {"username": config.username, "password": config.password}

    result = requests.post(endpoint, data=json.dumps(post_data))
    result_data = json.loads(result.text)

    session_id = result_data['sessionid']
    print("Session ID: %s".format(session_id))
    return session_id


def do_get(config: OpsCenterConfiguration, session_id, url):
    base_url = 'http://%s:8888/api/v2/lcm/' % config.server_ip
    result = requests.get(base_url + url,
                          headers={'Content-Type': 'application/json', 'opscenter-session': session_id})
    if result.status_code != 200:
        logging.error("OpsCenter API request failed: %s", result.text)
    logging.debug("%s", result.text)
    result_data = json.loads(result.text)
    return result_data


def do_post(config: OpsCenterConfiguration, session_id, url, post_data):
    base_url = 'http://%s:8888/api/v2/lcm/' % config.server_ip
    result = requests.post(base_url + url,
                           data=json.dumps(post_data),
                           headers={'Content-Type': 'application/json', 'opscenter-session': session_id})
    if result.status_code != 200:
        logging.error("OpsCenter API request failed: %s", result.text)
    logging.debug("%s", result.text)
    result_data = json.loads(result.text)
    return result_data
