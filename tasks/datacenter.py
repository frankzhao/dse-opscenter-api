import logging

import common
from config import OpsCenterConfiguration, DatacenterConfiguration


def create_datacenter(session_id, cluster_id, config: OpsCenterConfiguration,
                      datacenter_config: DatacenterConfiguration):
    datacenter_id = None
    datacenter_list = common.do_get(config, session_id, 'datacenters/')
    # datacenter_config_names = [d.name for d in config.datacenter_configuration]
    for datacenter in datacenter_list['results']:
        # Check if datacenter is existing for this cluster.
        if datacenter['cluster-id'] == cluster_id and datacenter['name'] == datacenter_config.name:
            logging.warning("Datacenter already exists, skipping creation. datacenter_name: %s", datacenter_config.name)
            datacenter_id = datacenter['id']
            return datacenter_id

    if not datacenter_id:
        make_dc_response = common.do_post(
            config, session_id, "datacenters/",
            {
                "name": datacenter_config.name,
                "cluster-id": cluster_id,
                "solr-enabled": datacenter_config.solr_enabled,
                "spark-enabled": datacenter_config.spark_enabled,
                "graph-enabled": datacenter_config.graph_enabled,
            }
        )
        dc_id = make_dc_response['id']
        logging.info("Created datacenter, datacenter_id: %s", dc_id)

        return dc_id
