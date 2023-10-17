import common


def create_nodes(session_id, config: OpsCenterConfiguration):
    make_node_response = common.do_post(
        config, session_id, "nodes/",
        {
            "name": node_name,
            "listen-address": private_ip,
            "native-transport-address": "0.0.0.0",
            "broadcast-address": node_ip,
            "native-transport-broadcast-address": node_ip,
            "ssh-management-address": node_ip,
            "datacenter-id": dc_id,
            "rack": "rack1"
        }
    )
