from typing import Optional, Literal

from .base import (
    BasePlayer,
    BaseChatEvent,
    BasePlayerCommandEvent,
    BaseDeathEvent,
    BaseJoinEvent,
    BaseQuitEvent
)


class Player(BasePlayer):
    """Fabric Player"""
    uuid: Optional[str] = None
    ip: Optional[str] = None
    display_name: Optional[str] = None
    movement_speed: Optional[float] = None

    block_x: Optional[int] = None
    block_y: Optional[int] = None
    block_z: Optional[int] = None

    is_creative: Optional[bool] = None
    is_spectator: Optional[bool] = None
    is_sneaking: Optional[bool] = None
    is_sleeping: Optional[bool] = None
    is_climbing: Optional[bool] = None
    is_swimming: Optional[bool] = None


class FabricServerMessageEvent(BaseChatEvent):
    """Fabric FabricServerMessageEvent API"""
    event_name: Literal["FabricServerMessageEvent"]
    player: Player
    message: str


class FabricServerCommandMessageEvent(BasePlayerCommandEvent):
    """Fabric FabricServerCommandMessageEvent API"""
    event_name: Literal["FabricServerCommandMessageEvent"]
    player: Player
    message: str


class FabricServerLivingEntityAfterDeathEvent(BaseDeathEvent):
    """Fabric FabricServerLivingEntityAfterDeathEvent API"""
    event_name: Literal["FabricServerLivingEntityAfterDeathEvent"]
    player: Player
    message: str


class FabricServerPlayConnectionJoinEvent(BaseJoinEvent):
    """Fabric FabricServerPlayConnectionJoinEvent API"""
    event_name: Literal["FabricServerPlayConnectionJoinEvent"]
    player: Player


class FabricServerPlayConnectionDisconnectEvent(BaseQuitEvent):
    """Fabric FabricServerPlayConnectionDisconnectEvent API"""
    event_name: Literal["FabricServerPlayConnectionDisconnectEvent"]
    player: Player
