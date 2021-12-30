from suton.toncontrol.settings.depool_settings.auto_replenish import AutoReplenishSettings
from suton.toncontrol.settings.depool_settings.prudent_elections import PrudentElectionSettings
from suton.toncontrol.settings.core import TonSettings
from suton.toncontrol.settings.elections import ElectionSettings, ElectionMode
from suton.toncontrol.settings.depool_settings.depool import DePoolSettings
from suton.tonlibs.toncommon.models.TonCoin import TonCoin


class DepoolElectionSettings(ElectionSettings):

    TON_CONTROL_ELECTION_MODE = ElectionMode.DEPOOL
    DEPOOL_LIST = [
        DePoolSettings(depool_address="0:<addr>",
                       abi_url="https://raw.githubusercontent.com/tonlabs/ton-labs-contracts/DePool_2021_02_01/solidity/depool/DePool.abi.json",
                       prudent_election_settings=PrudentElectionSettings(election_end_join_offset=3000,
                                                                         join_threshold=1),
                       replenish_settings=AutoReplenishSettings(TonCoin(2.5), max_period=7200)
                       )
    ]


class NodeSettings(TonSettings):
    # None for local, or "ssh://root@<ip>" for remote server
    DOCKER_HOST = None

    # for telemetry purposes
    NODE_NAME = "node-main"

    TON_ENV = "main.ton.dev"
    # ex "/mnt/ton/validator", don't forget to chmod 1001:1001 <path> on host
    TON_WORK_DIR = "path to work-dir on host machine"
    # ex "/mnt/ton/control", don't forget to chmod 1002:1002 <path> on host
    TON_CONTROL_WORK_DIR = "path to work-dir on hostmachine"
    TON_CONTROL_SECRET_MANAGER_CONNECTION_STRING = {
        "encryption_key_name": "key.priv",  # ex private key name under keys/ folder to use, used for validator and custodian seed decryption
        "validator_seed": '',  # see https://github.com/jarig/suton#seed-encryption
        "validator_address": "",  # ex 0:210e0f46cb458760d1798e1d005fe580913d59b34a1684f19f461622a880758a
        "custodian_seeds": [
            ""  # encrypted in the same way as validator_seed
        ],
        "secrets": {
        }
    }
    # Current Elector in the Main network is Fift based, remove comment once becomes Solidity based
    # ELECTOR_ABI_URL = "https://raw.githubusercontent.com/tonlabs/rustnet.ton.dev/6b9c09474d2a4a785b04b562d547f12967b8b53d/docker-compose/ton-node/configs/Elector.abi.json"
    # explicitly define ton_validator config to use
    TON_VALIDATOR_CONFIG_URL = "https://raw.githubusercontent.com/tonlabs/main.ton.dev/master/configs/ton-global.config.json"

    # TonoCLI settings
    TON_ENDPOINTS = "https://main2.ton.dev,https://main3.ton.dev,https://main4.ton.dev"

    ELECTIONS_SETTINGS = DepoolElectionSettings()
