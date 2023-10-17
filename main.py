import argparse
import logging

import common
from config import OpsCenterConfiguration
from tasks.cluster import create_cluster
from tasks.config_profile import create_config_profile
from tasks.credential import create_credential
from tasks.datacenter import create_datacenter
from tasks.node import create_nodes
from tasks.repo import create_repo

parser = argparse.ArgumentParser(
    prog='DSE OpsCenter Configuration',
    description='Set up OpsCenter LCM with configuration')

parser.add_argument("--debug", help="Enable debug logging.", action='store_true')
parser.add_argument('-f', '--config', help='Location of config yaml. (default config/config.yaml)')
args = parser.parse_args()

config = OpsCenterConfiguration()
config.load_config(args.config)

if args.debug:
  logging.basicConfig(level=logging.DEBUG)
else:
  logging.basicConfig(level=logging.INFO)

session_id = common.get_session_token(config)

repo_id = create_repo(session_id, config)
credential_id = create_credential(session_id, config)
config_profile_id = create_config_profile(session_id, config)
cluster_id = create_cluster(session_id, config, repo_id, credential_id,
                            config_profile_id)

for datacenter_config in config.datacenter_configuration:
  datacenter_id = create_datacenter(session_id, cluster_id, config,
                                    datacenter_config)
  for node_config in datacenter_config.node_configuration:
    node_id = create_nodes(session_id, config, datacenter_id, node_config)

# Add nodes

# Run install
