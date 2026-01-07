from typing import TYPE_CHECKING
from worlds.generic.Rules import set_rule

if TYPE_CHECKING:
    from . import FF2NESWorld


def has_ship(state, player: int) -> bool:
    return state.has("Ship", player)


def has_airship(state, player: int) -> bool:
    return state.has("Airship", player)


def has_goddess_bell(state, player: int) -> bool:
    return state.has("Goddess Bell", player)


def has_dreadnought_access(state, player: int) -> bool:
    return state.has("Sunfire", player) and state.has("Egil's Torch", player)


def has_tropical_island_access(state, player: int) -> bool:
    return (has_ship(state, player) and
            state.has("White Mask", player) and
            state.has("Black Mask", player))


def has_mysidian_tower_access(state, player: int) -> bool:
    return has_ship(state, player) and state.has("Crystal Rod", player)


def set_rules(world: "FF2NESWorld") -> None:
    player = world.player
    multiworld = world.multiworld

    # === KASHUAN KEEP ===
    # Requires Goddess Bell to enter
    for loc_name in ["Kashuan Keep - Egil's Torch Chest",
                     "Kashuan Keep - Goddess Bell Chest",
                     "Kashuan Keep - Sunfire"]:
        set_rule(multiworld.get_location(loc_name, player),
                 lambda state, p=player: has_goddess_bell(state, p))

    # === DREADNOUGHT ===
    # Requires Sunfire and Egil's Torch
    for loc_name in ["Dreadnought - Engine Room",
                     "Dreadnought - Chest 1",
                     "Dreadnought - Chest 2"]:
        set_rule(multiworld.get_location(loc_name, player),
                 lambda state, p=player: has_dreadnought_access(state, p))

    # === DEIST ===
    # Requires Ship to reach
    for loc_name in ["Deist - Wyvern Egg",
                     "Deist Cavern - Chest 1",
                     "Deist Cavern - Pendant"]:
        set_rule(multiworld.get_location(loc_name, player),
                 lambda state, p=player: has_ship(state, p))

    # === COLISEUM ===
    # Requires Ship to reach
    set_rule(multiworld.get_location("Coliseum - Victory Reward", player),
             lambda state, p=player: has_ship(state, p))

    # === TROPICAL ISLAND ===
    # Requires Ship + both Masks
    for loc_name in ["Tropical Island - Black Mask Chest",
                     "Tropical Island - White Mask Chest"]:
        set_rule(multiworld.get_location(loc_name, player),
                 lambda state, p=player: has_tropical_island_access(state, p))

    # === MYSIDIAN TOWER ===
    # Requires Ship + Crystal Rod
    for loc_name in ["Mysidian Tower - 1F Chest",
                     "Mysidian Tower - 2F Chest",
                     "Mysidian Tower - Crystal Rod",
                     "Mysidian Tower - White Dragon",
                     "Mysidian Tower - Black Dragon"]:
        set_rule(multiworld.get_location(loc_name, player),
                 lambda state, p=player: has_mysidian_tower_access(state, p))

    # === CASTLE PALAMECIA ===
    # Requires Airship
    for loc_name in ["Castle Palamecia - Chest 1",
                     "Castle Palamecia - Chest 2",
                     "Castle Palamecia - Sun Blade"]:
        set_rule(multiworld.get_location(loc_name, player),
                 lambda state, p=player: has_airship(state, p))

    # === PANDAEMONIUM ===
    # Requires Airship (final dungeon)
    for loc_name in ["Pandaemonium - Chest 1",
                     "Pandaemonium - Chest 2",
                     "Pandaemonium - Masamune"]:
        set_rule(multiworld.get_location(loc_name, player),
                 lambda state, p=player: has_airship(state, p))

    # === COMPLETION CONDITION ===
    # Must be able to reach Pandaemonium and have beaten the game
    multiworld.completion_condition[player] = \
        lambda state: has_airship(state, player)