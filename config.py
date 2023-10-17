from pyconfigparser import configparser, ConfigError
from schema import Use, And

SCHEMA_CONFIG = {
    'core': {
        'logging': {
            'level': And(Use(str), lambda string: len(string) > 0),
        },
    },
    'dse': {
        'cluster_name': And(Use(str), lambda string: len(string) > 0),
        'datastax_version': And(Use(str), lambda string: len(string) > 0),
        'repository_name': And(Use(str), lambda string: len(string) > 0),
        'config_profile_name': And(Use(str), lambda string: len(string) > 0),
        'opscenter_username': And(Use(str), lambda string: len(string) > 0),
        'opscenter_password': And(Use(str), lambda string: len(string) > 0),
        'opscenter_server_ip': And(Use(str), lambda string: len(string) > 0),
        'install_credential_name': And(Use(str), lambda string: len(string) > 0),
        'install_credential_username': And(Use(str), lambda string: len(string) > 0),
        'install_credential_key': And(Use(str), lambda string: len(string) > 0),
        'cassandra_default_password': And(Use(str), lambda string: len(string) > 0),
    },
}


class OpsCenterConfiguration:
    log_level = None
    cluster_name = None
    datastax_version = None
    repository_name = None
    config_profile_name = None
    username = None
    password = None
    server_ip = None
    install_credential_name = None
    install_credential_username = None
    install_credential_key = None
    cassandra_default_password = None

    def load_config(self):
        # .config/config.yaml
        try:
            config = configparser.get_config(SCHEMA_CONFIG)

            self.log_level = config['core']['logging']['level']
            self.cluster_name = config['dse']['cluster_name']
            self.datastax_version = config['dse']['datastax_version']
            self.repository_name = config['dse']['repository_name']
            self.config_profile_name = config['dse']['config_profile_name']
            self.username = config['dse']['opscenter_username']
            self.password = config['dse']['opscenter_password']
            self.server_ip = config['dse']['opscenter_server_ip']
            self.install_credential_name = config['dse']['install_credential_name']
            self.install_credential_username = config['dse']['install_credential_username']
            self.cassandra_default_password = config['dse']['cassandra_default_password']
        except ConfigError as e:
            print(e)
            exit()
