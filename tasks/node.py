import logging

import common
from config import OpsCenterConfiguration, NodeConfiguration


def create_nodes(session_id, config: OpsCenterConfiguration, datacenter_id, node_config: NodeConfiguration):
    node_id = None
    node_list = common.do_get(config, session_id, 'nodes/')
    for node in node_list['results']:
        # Check if datacenter is existing for this cluster.
        if node['datacenter-id'] == datacenter_id and node['name'] == node_config.name:
            logging.warning("Node already exists, skipping creation. node_name: %s", node_config.name)
            node_id = node['id']
            return node_id

    if not node_id:
        make_node_response = common.do_post(
            config, session_id, "nodes/",
            {
                "name": node_config.name,
                "listen-address": node_config.private_ip,
                "native-transport-address": "0.0.0.0",
                "broadcast-address": node_config.node_ip,
                "native-transport-broadcast-address": node_config.node_ip,
                "ssh-management-address": node_config.node_ip,
                "datacenter-id": datacenter_id,
                "rack": node_config.rack
            }
        )

        node_id = make_node_response['id']
        logging.info("Created datacenter, datacenter_id: %s, name: %s", node_id, node_config.name)
        return node_id
