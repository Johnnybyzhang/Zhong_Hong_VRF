"""Zhong Hong VRF integration for Home Assistant."""

from __future__ import annotations

import logging

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import (
    CONF_HOST,
    CONF_PASSWORD,
    CONF_PORT,
    CONF_USERNAME,
    Platform,
)
from homeassistant.core import HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady

from .client import ZhongHongClient
from .const import DOMAIN
from .coordinator import ZhongHongDataUpdateCoordinator
from .runtime_data import ZhongHongRuntimeData

_LOGGER = logging.getLogger(__name__)

PLATFORMS = [Platform.CLIMATE]


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up Zhong Hong VRF from a config entry."""
    _LOGGER.info("Setting up Zhong Hong VRF integration for %s", entry.data[CONF_HOST])

    host = entry.data[CONF_HOST]
    port = entry.data[CONF_PORT]
    username = entry.data[CONF_USERNAME]
    password = entry.data[CONF_PASSWORD]

    client = ZhongHongClient(host, port, username, password)

    try:
        await client.async_setup()
    except Exception as ex:
        _LOGGER.error("Failed to setup Zhong Hong client: %s", ex)
        raise ConfigEntryNotReady from ex

    coordinator = ZhongHongDataUpdateCoordinator(hass, entry)
    await coordinator.async_config_entry_first_refresh()

    # Store runtime data in the config entry instead of hass.data
    entry.runtime_data = ZhongHongRuntimeData(coordinator=coordinator)

    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)

    _LOGGER.info("Successfully set up Zhong Hong VRF integration")
    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    _LOGGER.info("Unloading Zhong Hong VRF integration for %s", entry.data[CONF_HOST])

    unload_ok = await hass.config_entries.async_unload_platforms(entry, PLATFORMS)

    if unload_ok:
        # Clean up runtime data
        runtime_data: ZhongHongRuntimeData = entry.runtime_data
        await runtime_data.coordinator.async_shutdown()

        _LOGGER.info("Successfully unloaded Zhong Hong VRF integration")

    return unload_ok
