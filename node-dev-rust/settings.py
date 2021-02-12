from suton.toncontrol.settings.depool_settings.auto_replenish import AutoReplenishSettings
from suton.toncontrol.settings.depool_settings.prudent_elections import PrudentElectionSettings
from suton.toncontrol.settings.core import TonSettings
from suton.toncontrol.settings.elections import ElectionSettings, ElectionMode
from suton.toncontrol.settings.depool_settings.depool import DePoolSettings
from suton.tonlibs.toncommon.models.TonCoin import TonCoin


class DepoolElectionSettings(ElectionSettings):

    TON_CONTROL_ELECTION_MODE = ElectionMode.DEPOOL
    DEPOOL_LIST = [
        DePoolSettings(depool_address="",
                       proxy_addresses=["",
                                        ""],
                       prudent_election_settings=PrudentElectionSettings(election_end_join_offset=3000,
                                                                         join_threshold=1),
                       replenish_settings=AutoReplenishSettings(TonCoin(2.5), max_period=7200)
                       )
    ]


class NodeSettings(TonSettings):
    DOCKER_HOST = None  # None for local, or "ssh://root@<ip>" for remote server

    TON_ENV = "rustnet.ton.dev"
    TON_WORK_DIR = "path to work-dir on host machine" # ex "/mnt/ton/validator"
    TON_CONTROL_WORK_DIR = "path to work-dir on hostmachine" # ex "/mnt/ton/control"
    TON_CONTROL_SECRET_MANAGER_CONNECTION_STRING = {
        "encryption_key_name": "example_key.priv", # ex private key name under keys/ folder to use
        "validator_seed": '', # see https://github.com/jarig/suton#seed-encryption
        "validator_address": "", # ex 0:210e0f46cb458760d1798e1d005fe580913d59b34a1684f19f461622a880758a
        "custodian_seeds": [
            "" # encrypted in the same way as validator_seed 
        ],
        "secrets": {
        }
    }
    TON_VALIDATOR_TYPE = "rust"
    ELECTOR_ABI_URL = "https://raw.githubusercontent.com/tonlabs/rustnet.ton.dev/19d29ba/docker-compose/ton-node/configs/Elector.abi.json"
    # explicitly define ton_validator config to use
    TON_VALIDATOR_CONFIG_URL = "https://github.com/tonlabs/rustnet.ton.dev/raw/main/configs/ton-global.config.json"
    TONOS_CLI_CONFIG_URL = "https://rustnet.ton.dev"

    ELECTIONS_SETTINGS = DepoolElectionSettings()
