# Zhong Hong VRF Gateway (Aqara Version) Home Assistant Integration

This integration uses a hybrid HTTP+TCP approach to solve the response delay issues of the original HTTP-only method, providing a more user-friendly experience.

> [!WARNING]
> 
> This integration is only compatible with the Zhong Hong VRF Aqara version gateway. After reset, it now supports multiple outdoor units (tested up to 2 units).

# Installation

## Install via HACS

[![Open your Home Assistant instance and open a repository inside the HACS store.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=Johnnybyzhang&repository=Zhong_Hong_VRF&category=integration)

## Manual Installation

Copy the `zhong_hong_vrf` folder from `custom_components` to the `custom_components` directory in your Home Assistant, then manually restart Home Assistant.

# Setup

[![Open your Home Assistant instance and start setting up a new integration.](https://my.home-assistant.io/badges/config_flow_start.svg)](https://my.home-assistant.io/redirect/config_flow_start/?domain=zhong_hong_vrf)

> [!CAUTION]
> 
> If you cannot use the button above, please follow these steps:
> 
> 1. Navigate to the Home Assistant integrations page (Settings --> Devices & Services)
> 2. Click the `+ Add Integration` button in the bottom right corner
> 3. Search for `Zhong Hong VRF`

> [!NOTE]
> 
> 1. Gateway IP: Please enter the IP address of your VRF gateway
> 2. TCP Port: Default is `9999`
> 3. Username: Default is `admin`
> 4. Password: Default is empty

# Removal Instructions

To completely remove the Zhong Hong VRF integration from your Home Assistant:

## Via Home Assistant UI (Recommended)

1. Navigate to **Settings** → **Devices & Services**
2. Find the **Zhong Hong VRF** integration in your list
3. Click on the integration to open its details
4. Click the **three-dot menu** (⋮) in the top right corner
5. Select **Remove** and confirm the removal
6. The integration and all associated devices/entities will be removed automatically

## Clean Up Stale Devices/Entities (If Needed)

If you have orphaned devices or entities after removal:

1. Go to **Settings** → **Devices & Services** → **Devices** tab
2. Look for any devices with "Zhong Hong VRF" or "AC" in their names
3. Click on each device and select **Remove Device**
4. Go to **Settings** → **Devices & Services** → **Entities** tab  
5. Filter for entities containing "zhong_hong" or your AC device names
6. Select and remove any remaining entities

## Manual File Removal (If Needed)

If installed manually and you want to completely remove files:

1. Stop Home Assistant
2. Navigate to your `custom_components` directory
3. Delete the `zhong_hong_vrf` folder
4. Restart Home Assistant

## Re-adding the Integration

To add the integration again after removal:
- Simply follow the **Setup** instructions above
- All devices will be rediscovered automatically
- Previous entity names and customizations will need to be reconfigured

# Supported AC Brands

This integration supports a wide range of AC brands including:
- **Major Brands**: Hitachi, Daikin, Toshiba, Mitsubishi Heavy Industries, Mitsubishi Electric, Gree, Midea, Haier, Samsung, LG
- **Chinese Brands**: Hisense, AUX, Chigo, TICA, TCL
- **Specialized Systems**: Protocol converters, thermostats, modular systems
- **Regional Variants**: York Qingdao, CH-York, CoolWind, and more

For a complete list of supported brands, see the `AC_BRANDS` mapping in [`custom_components/zhong_hong_vrf/const.py`](https://github.com/Johnnybyzhang/Zhong_Hong_VRF/blob/main/custom_components/zhong_hong_vrf/const.py).

# Development

This project follows Home Assistant integration best practices and includes comprehensive testing and quality assurance.

## Development Commands

- `make fmt` - Format code with black and ruff
- `make lint` - Run linting checks
- `make test` - Run test suite
- `make audit` - Run security audits
- `make install-dev` - Install development dependencies

## Contributing

Please follow the conventional commit format:
- `feat(scope): description` - New features
- `fix(scope): description` - Bug fixes  
- `chore(scope): description` - Maintenance tasks

All PRs must be ≤300 lines of code and include tests.

# Credits

[xswxm/home-assistant-zhong-hong](https://github.com/xswxm/home-assistant-zhong-hong)

---

**[中文版本 → README.md](./README.md)**
