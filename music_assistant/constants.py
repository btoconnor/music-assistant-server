"""All constants for Music Assistant."""

__version__ = "0.0.43"
REQUIRED_PYTHON_VER = "3.7"

CONF_USERNAME = "username"
CONF_PASSWORD = "password"
CONF_ENABLED = "enabled"
CONF_HOSTNAME = "hostname"
CONF_PORT = "port"
CONF_TOKEN = "token"
CONF_URL = "url"
CONF_NAME = "name"
CONF_CROSSFADE_DURATION = "crossfade_duration"
CONF_FALLBACK_GAIN_CORRECT = "fallback_gain_correct"
CONF_GROUP_DELAY = "group_delay"
CONF_VOLUME_CONTROL = "volume_control"
CONF_POWER_CONTROL = "power_control"

CONF_KEY_BASE = "base"
CONF_KEY_PLAYERSETTINGS = "player_settings"
CONF_KEY_PROVIDERS = "providers"

EVENT_PLAYER_ADDED = "player added"
EVENT_PLAYER_REMOVED = "player removed"
EVENT_PLAYER_CHANGED = "player changed"
EVENT_STREAM_STARTED = "streaming started"
EVENT_STREAM_ENDED = "streaming ended"
EVENT_CONFIG_CHANGED = "config changed"
EVENT_MUSIC_SYNC_STATUS = "music sync status"
EVENT_QUEUE_UPDATED = "queue updated"
EVENT_QUEUE_ITEMS_UPDATED = "queue items updated"
EVENT_QUEUE_TIME_UPDATED = "queue time updated"
EVENT_SHUTDOWN = "application shutdown"
EVENT_PROVIDER_REGISTERED = "provider registered"
EVENT_PLAYER_CONTROL_REGISTERED = "player control registered"
EVENT_PLAYER_CONTROL_UNREGISTERED = "player control unregistered"
EVENT_PLAYER_CONTROL_UPDATED = "player control updated"
EVENT_SET_PLAYER_CONTROL_STATE = "set player control state"

# websocket commands
EVENT_REGISTER_PLAYER_CONTROL = "register player control"
EVENT_UNREGISTER_PLAYER_CONTROL = "unregister player control"
EVENT_UPDATE_PLAYER_CONTROL = "update player control"
