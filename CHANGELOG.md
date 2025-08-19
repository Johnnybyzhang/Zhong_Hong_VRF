# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Comprehensive config flow test coverage (95%+ coverage) 
- Runtime data migration from hass.data to ConfigEntry.runtime_data
- Structured logging with improved error context (no PII)
- Development tooling: Makefile, pyproject.toml, linting setup
- Architecture Decision Records (ADRs) for major changes
- Detailed removal instructions in documentation
- Support for 70+ AC brands with clear brand mappings

### Changed
- **BREAKING (Internal)**: Migrated from `hass.data[DOMAIN][entry_id]` to `entry.runtime_data`
- Improved config flow UX with better data descriptions and error messages
- Enhanced logging with INFO/WARN/ERROR levels and structured context
- Updated documentation with comprehensive removal and troubleshooting guides

### Technical Improvements
- Added typed `ZhongHongRuntimeData` dataclass for better type safety  
- Config flow validation with proper error handling and user feedback
- Code formatting with Black (line length 100) and Ruff linting
- Test framework setup with pytest, asyncio, and mocking support
- Security auditing with pip-audit and bandit integration

### Documentation
- ADR-20250819: Runtime data migration rationale and implementation
- Enhanced README with development commands and contribution guidelines
- Complete removal/reinstallation procedures for users
- Cross-linked documentation for Context7 and ADR references

## [1.0.0] - 2024-08-03

### Added
- Initial release of Zhong Hong VRF integration
- Climate entity support with temperature and fan control
- HTTP+TCP hybrid communication for reduced latency
- Support for multiple outdoor units (tested up to 2 units)
- Config flow for easy setup via Home Assistant UI
- HACS integration support

### Features
- Real-time temperature monitoring and control
- HVAC mode support: heat, cool, dry, fan_only, off
- Fan speed control: auto, low, medium, high  
- Device discovery and automatic entity creation
- TCP listener for real-time updates
- Options flow for temperature range configuration

### Supported Hardware
- Zhong Hong VRF Aqara version gateway
- Wide range of AC brands (Hitachi, Daikin, Mitsubishi, Gree, etc.)
- Protocol converters and specialized HVAC systems
