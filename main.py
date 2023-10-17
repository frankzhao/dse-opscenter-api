import logging

import common
from config import OpsCenterConfiguration
from tasks.cluster import create_cluster
from tasks.config_profile import create_config_profile
from tasks.credential import create_credential
from tasks.repo import create_repo

config = OpsCenterConfiguration()
config.load_config()

logging.basicConfig(level=config.log_level)

session_id = common.get_session_token(config)

repo_id = create_repo(session_id, config)
credential_id = create_credential(session_id, config)
config_profile_id = create_config_profile(session_id, config)
cluster_id = create_cluster(session_id, config, repo_id, credential_id, config_profile_id)

# Add nodes

# Run install
