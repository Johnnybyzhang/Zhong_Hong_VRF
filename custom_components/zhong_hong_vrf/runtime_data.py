"""Runtime data models for Zhong Hong VRF integration."""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .coordinator import ZhongHongDataUpdateCoordinator


@dataclass
class ZhongHongRuntimeData:
    """Runtime data for Zhong Hong VRF integration."""

    coordinator: ZhongHongDataUpdateCoordinator
