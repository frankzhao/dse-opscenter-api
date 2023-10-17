import logging

import common
from config import OpsCenterConfiguration


def create_cluster(session_id, config: OpsCenterConfiguration, repository_id, machine_credential_id, config_profile_id):
    cluster_id = None
    cluster_list = common.do_get(config, session_id, 'clusters/')
    for cluster in cluster_list['results']:
        if cluster['name'] == config.cluster_name:
            logging.warning("Cluster already exists, skipping creation. cluster_name: %s", config.cluster_name)
            cluster_id = cluster['id']

    if not cluster_id:
        make_cluster_response = common.do_post(
            config,
            session_id,
            "clusters/",
            {
                "name": config.cluster_name,
                "repository-id": repository_id,
                "machine-credential-id": machine_credential_id,
                "old-password": "cassandra",
                "new-password": config.cassandra_default_password,
                "config-profile-id": config_profile_id
            }
        )
        cluster_id = make_cluster_response['id']
        logging.info("Created cluster, cluster_id: %s", cluster_id)

    return cluster_id
