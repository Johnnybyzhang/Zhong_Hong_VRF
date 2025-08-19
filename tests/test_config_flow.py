"""Test Zhong Hong VRF config flow."""

from __future__ import annotations

import asyncio
from unittest.mock import AsyncMock, Mock, patch

import pytest
from homeassistant import config_entries, data_entry_flow
from homeassistant.const import CONF_HOST, CONF_PASSWORD, CONF_PORT, CONF_USERNAME
from homeassistant.core import HomeAssistant

from custom_components.zhong_hong_vrf import config_flow
from custom_components.zhong_hong_vrf.const import (
    DEFAULT_MAX_TEMP,
    DEFAULT_MIN_TEMP,
    DEFAULT_PASSWORD,
    DEFAULT_PORT,
    DEFAULT_USERNAME,
    DOMAIN,
)


@pytest.fixture
def mock_zhong_hong_client():
    """Mock ZhongHongClient for testing."""
    with patch(
        "custom_components.zhong_hong_vrf.config_flow.ZhongHongClient"
    ) as mock_client_class:
        mock_client = AsyncMock()
        mock_client_class.return_value = mock_client
        
        # Default successful responses
        mock_client.async_setup = AsyncMock()
        mock_client.async_get_device_info = AsyncMock(return_value={
            "manufacturer": "Zhong Hong",
            "model": "VRF Gateway",
            "version": "1.0.0"
        })
        mock_client.async_get_devices = AsyncMock(return_value=[
            {"id": "1-1", "name": "AC 1-1"},
            {"id": "1-2", "name": "AC 1-2"}
        ])
        mock_client.async_shutdown = AsyncMock()
        
        yield mock_client


async def test_form_user_success(hass: HomeAssistant, mock_zhong_hong_client):
    """Test successful user flow creates entry with expected title and data."""
    result = await hass.config_entries.flow.async_init(
        DOMAIN, context={"source": config_entries.SOURCE_USER}
    )
    assert result["type"] == data_entry_flow.FlowResultType.FORM
    assert result["errors"] == {}

    # Submit user input
    test_data = {
        CONF_HOST: "192.168.1.100",
        CONF_PORT: DEFAULT_PORT,
        CONF_USERNAME: DEFAULT_USERNAME,
        CONF_PASSWORD: DEFAULT_PASSWORD,
    }
    
    result2 = await hass.config_entries.flow.async_configure(
        result["flow_id"], test_data
    )
    
    await hass.async_block_till_done()
    
    assert result2["type"] == data_entry_flow.FlowResultType.CREATE_ENTRY
    assert result2["title"] == "Zhong Hong VRF (192.168.1.100)"
    assert result2["data"] == test_data


async def test_form_user_cannot_connect_timeout(hass: HomeAssistant, mock_zhong_hong_client):
    """Test timeout error during connection."""
    mock_zhong_hong_client.async_setup.side_effect = TimeoutError()
    
    result = await hass.config_entries.flow.async_init(
        DOMAIN, context={"source": config_entries.SOURCE_USER}
    )
    
    test_data = {
        CONF_HOST: "192.168.1.100",
        CONF_PORT: DEFAULT_PORT,
        CONF_USERNAME: DEFAULT_USERNAME,
        CONF_PASSWORD: DEFAULT_PASSWORD,
    }
    
    result2 = await hass.config_entries.flow.async_configure(
        result["flow_id"], test_data
    )
    
    assert result2["type"] == data_entry_flow.FlowResultType.FORM
    assert result2["errors"]["base"] == "cannot_connect"


async def test_options_flow_success(hass: HomeAssistant):
    """Test options flow saves configuration correctly."""
    config_entry = config_entries.ConfigEntry(
        domain=DOMAIN,
        title="Test Zhong Hong VRF",
        data={CONF_HOST: "192.168.1.100"},
        options={"min_temp": 18, "max_temp": 28},
        version=1,
        entry_id="test_entry_id",
        source=config_entries.SOURCE_USER,
        unique_id="192.168.1.100",
    )
    
    options_flow = config_flow.ZhongHongOptionsFlowHandler(config_entry)
    
    result2 = await options_flow.async_step_init({
        "min_temp": 16,
        "max_temp": 30
    })
    
    assert result2["type"] == data_entry_flow.FlowResultType.CREATE_ENTRY
    assert result2["data"] == {"min_temp": 16, "max_temp": 30}
