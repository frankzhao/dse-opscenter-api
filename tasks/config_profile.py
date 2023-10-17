import logging

import common
from config import OpsCenterConfiguration


def create_config_profile(session_id, config: OpsCenterConfiguration):
    config_profile_id = None
    config_profiles_list = common.do_get(config, session_id, 'config_profiles/')
    for profile in config_profiles_list['results']:
        if profile['name'] == config.config_profile_name:
            logging.warning("Config profile already exists, skipping creation. config_profile_name: %s",
                            config.config_profile_name)
            config_profile_id = profile['id']

    if not config_profile_id:
        config_profile_response = common.do_post(
            config,
            session_id,
            "config_profiles/",
            {"name": config.config_profile_name,
             "datastax-version": config.datastax_version,
             'json': {
                 "cassandra-env-sh": {},
                 "dse-env-sh": {}
             },
             "comment": 'LCM provisioned as %s' % config.config_profile_name}
        )

        config_profile_id = config_profile_response['id']
        logging.info("Created config profile, config_profile_id: %s", config_profile_id)

    return config_profile_id
