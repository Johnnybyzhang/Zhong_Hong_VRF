# ADR-20250819: Migrate to ConfigEntry.runtime_data

## Status

Accepted

## Context

The Zhong Hong VRF integration was using the legacy `hass.data[DOMAIN][entry_id]` pattern to store integration runtime data (coordinator instances). Home Assistant has introduced `ConfigEntry.runtime_data` as the recommended approach for storing per-entry runtime data, providing better type safety and memory management.

### Current Implementation Issues

- Uses global `hass.data` dictionary with domain/entry_id keys
- No type hints for stored data structure
- Potential memory leaks if cleanup is incomplete
- Not following Home Assistant best practices for 2024+

## Decision

Migrate from `hass.data[DOMAIN][entry_id]` to `ConfigEntry.runtime_data` using a typed dataclass approach.

### Implementation

1. **Define typed runtime data structure**:
   ```python
   @dataclass
   class ZhongHongRuntimeData:
       coordinator: ZhongHongDataUpdateCoordinator
   ```

2. **Update async_setup_entry**:
   - Store coordinator in `entry.runtime_data` instead of `hass.data`
   - Use typed dataclass for better IDE support and runtime validation

3. **Update async_unload_entry**:
   - Access coordinator via `entry.runtime_data`
   - Cleaner shutdown without manual dictionary cleanup

4. **Update platform setup**:
   - Access coordinator via `entry.runtime_data` in climate platform
   - Maintain backward compatibility during transition

## Alternatives Considered

1. **Keep current hass.data approach**
   - ❌ Not following HA best practices
   - ❌ No type safety
   - ❌ Manual memory management required

2. **Use TypedDict instead of dataclass**
   - ❌ Less type safety at runtime
   - ❌ No IDE autocompletion benefits

3. **Store client directly without coordinator wrapper**
   - ❌ Would require larger refactoring
   - ❌ Loses data update coordination benefits

## Consequences

### Positive

- ✅ Follows Home Assistant 2024+ best practices
- ✅ Better type safety with dataclass typing
- ✅ Automatic memory management by Home Assistant core
- ✅ Cleaner code with fewer manual dictionary operations
- ✅ Better IDE support and autocompletion

### Negative

- ⚠️ Requires updating all platform files (climate.py)
- ⚠️ Potential compatibility issues with older HA versions
- ⚠️ Need to ensure all tests are updated

### Migration Impact

- **Files Modified**: `__init__.py`, `climate.py`, `runtime_data.py` (new)
- **Breaking Changes**: None for users, internal API change only
- **Testing**: Config flow tests, platform setup tests updated

## Rollback Plan

If issues arise, revert changes by:

1. Remove `runtime_data.py` module
2. Restore `hass.data[DOMAIN][entry_id] = coordinator` pattern
3. Update platform files to use `hass.data` access
4. Remove type hints related to runtime_data

Emergency rollback snippet:
```python
# In async_setup_entry
hass.data.setdefault(DOMAIN, {})
hass.data[DOMAIN][entry.entry_id] = coordinator

# In climate platform  
coordinator = hass.data[DOMAIN][entry.entry_id]
```

## References

- [Home Assistant Integration Development](https://developers.home-assistant.io/docs/creating_integration_manifest/)
- [ConfigEntry API Documentation](https://developers.home-assistant.io/docs/config_entries_config_flow_handler/)
- [Home Assistant Architecture ADR](https://github.com/home-assistant/architecture/blob/master/adr/0006-config-flow-handler.md)
