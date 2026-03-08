"""The Tuya BLE integration."""
from __future__ import annotations

from dataclasses import dataclass

from typing_extensions import Final

DOMAIN: Final = "tuya_ble"

# Tuya cloud auth constants (local copy for HA 2024+ compatibility; core Tuya const was refactored)
CONF_ACCESS_ID: Final = "access_id"
CONF_ACCESS_SECRET: Final = "access_secret"
CONF_APP_TYPE: Final = "app_type"
CONF_AUTH_TYPE: Final = "auth_type"
CONF_COUNTRY_CODE: Final = "country_code"
CONF_ENDPOINT: Final = "endpoint"
CONF_PASSWORD: Final = "password"
CONF_USERNAME: Final = "username"

TUYA_RESPONSE_CODE: Final = "code"
TUYA_RESPONSE_MSG: Final = "msg"
TUYA_RESPONSE_RESULT: Final = "result"
TUYA_RESPONSE_SUCCESS: Final = "success"

TUYA_SMART_APP: Final = "tuya"
SMARTLIFE_APP: Final = "smartlife"

# Built-in Tuya integration domain (for reading existing config entries)
TUYA_DOMAIN: Final = "tuya"


@dataclass(frozen=True)
class TuyaCountry:
    """Tuya data center region."""

    name: str
    country_code: str
    endpoint: str


# Map HA config country (ISO 3166-1 alpha-2) to Tuya country name (no blocking I/O)
DEFAULT_COUNTRY_ALPHA2_TO_NAME: dict[str, str] = {
    "AZ": "Azerbaijan",
    "US": "United States",
    "CA": "Canada",
    "MX": "Mexico",
    "BR": "Brazil",
    "JP": "Japan",
    "KR": "South Korea",
    "AU": "Australia",
    "GB": "United Kingdom",
    "DE": "Germany",
    "FR": "France",
    "ES": "Spain",
    "IT": "Italy",
    "NL": "Netherlands",
    "PL": "Poland",
    "RU": "Russia",
    "TR": "Turkey",
    "IN": "India",
    "CN": "China",
}

# Tuya data center regions (country name, API country code, endpoint)
# See: https://github.com/tuya/tuya-home-assistant/wiki/Countries-Regions-and-Tuya-Data-Center
TUYA_COUNTRIES: tuple[TuyaCountry, ...] = (
    TuyaCountry("Azerbaijan", "994", "https://openapi.tuyaeu.com"),
    TuyaCountry("United States", "1", "https://openapi.tuyaus.com"),
    TuyaCountry("Canada", "1", "https://openapi.tuyaus.com"),
    TuyaCountry("Mexico", "52", "https://openapi.tuyaus.com"),
    TuyaCountry("Brazil", "55", "https://openapi.tuyaus.com"),
    TuyaCountry("Japan", "81", "https://openapi.tuyaus.com"),
    TuyaCountry("South Korea", "82", "https://openapi.tuyaus.com"),
    TuyaCountry("Australia", "61", "https://openapi.tuyaeu.com"),
    TuyaCountry("United Kingdom", "44", "https://openapi.tuyaeu.com"),
    TuyaCountry("Germany", "49", "https://openapi.tuyaeu.com"),
    TuyaCountry("France", "33", "https://openapi.tuyaeu.com"),
    TuyaCountry("Spain", "34", "https://openapi.tuyaeu.com"),
    TuyaCountry("Italy", "39", "https://openapi.tuyaeu.com"),
    TuyaCountry("Netherlands", "31", "https://openapi.tuyaeu.com"),
    TuyaCountry("Poland", "48", "https://openapi.tuyaeu.com"),
    TuyaCountry("Russia", "7", "https://openapi.tuyaeu.com"),
    TuyaCountry("Turkey", "90", "https://openapi.tuyaeu.com"),
    TuyaCountry("India", "91", "https://openapi.tuyain.com"),
    TuyaCountry("China", "86", "https://openapi.tuyacn.com"),
)

DEVICE_METADATA_UUIDS: Final = "uuids"

DEVICE_DEF_MANUFACTURER: Final = "Tuya"
SET_DISCONNECTED_DELAY = 10 * 60

CONF_UUID: Final = "uuid"
CONF_LOCAL_KEY: Final = "local_key"
CONF_CATEGORY: Final = "category"
CONF_PRODUCT_ID: Final = "product_id"
CONF_DEVICE_NAME: Final = "device_name"
CONF_PRODUCT_MODEL: Final = "product_model"
CONF_PRODUCT_NAME: Final = "product_name"

TUYA_API_DEVICES_URL: Final = "/v1.0/users/%s/devices"
TUYA_API_FACTORY_INFO_URL: Final = "/v1.0/iot-03/devices/factory-infos?device_ids=%s"
TUYA_FACTORY_INFO_MAC: Final = "mac"

BATTERY_STATE_LOW: Final = "low"
BATTERY_STATE_NORMAL: Final = "normal"
BATTERY_STATE_HIGH: Final = "high"

BATTERY_NOT_CHARGING: Final = "not_charging"
BATTERY_CHARGING: Final = "charging"
BATTERY_CHARGED: Final = "charged"

CO2_LEVEL_NORMAL: Final = "normal"
CO2_LEVEL_ALARM: Final = "alarm"

FINGERBOT_MODE_PUSH: Final = "push"
FINGERBOT_MODE_SWITCH: Final = "switch"
FINGERBOT_MODE_PROGRAM: Final = "program"
FINGERBOT_BUTTON_EVENT: Final = "fingerbot_button_pressed"

