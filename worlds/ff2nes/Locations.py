from typing import Dict, NamedTuple, List


class FF2LocationData(NamedTuple):
    code: int
    region: str


# Base ID for FF2 NES locations
FF2_LOCATION_BASE_ID = 0xFF2100

FF2_LOCATIONS: Dict[str, FF2LocationData] = {
    # === ALTAIR (Starting Town) ===
    "Altair - Secret Room": FF2LocationData(FF2_LOCATION_BASE_ID + 1, "Altair"),

    # === FYNN ===
    "Fynn Castle - Throne Room": FF2LocationData(FF2_LOCATION_BASE_ID + 10, "Fynn"),
    "Fynn Castle - Basement Chest 1": FF2LocationData(FF2_LOCATION_BASE_ID + 11, "Fynn"),
    "Fynn Castle - Basement Chest 2": FF2LocationData(FF2_LOCATION_BASE_ID + 12, "Fynn"),

    # === SALAMAND ===
    "Salamand - Mithril Quest": FF2LocationData(FF2_LOCATION_BASE_ID + 20, "Salamand"),

    # === SEMITT FALLS ===
    "Semitt Falls - B1 Chest 1": FF2LocationData(FF2_LOCATION_BASE_ID + 30, "Semitt Falls"),
    "Semitt Falls - B1 Chest 2": FF2LocationData(FF2_LOCATION_BASE_ID + 31, "Semitt Falls"),
    "Semitt Falls - B2 Chest 1": FF2LocationData(FF2_LOCATION_BASE_ID + 32, "Semitt Falls"),
    "Semitt Falls - Mithril Room": FF2LocationData(FF2_LOCATION_BASE_ID + 33, "Semitt Falls"),

    # === BAFSK CAVE ===
    "Bafsk Cave - Chest 1": FF2LocationData(FF2_LOCATION_BASE_ID + 40, "Bafsk Cave"),
    "Bafsk Cave - Chest 2": FF2LocationData(FF2_LOCATION_BASE_ID + 41, "Bafsk Cave"),
    "Bafsk Cave - Pass Reward": FF2LocationData(FF2_LOCATION_BASE_ID + 42, "Bafsk Cave"),

    # === KASHUAN KEEP ===
    "Kashuan Keep - Egil's Torch Chest": FF2LocationData(FF2_LOCATION_BASE_ID + 50, "Kashuan Keep"),
    "Kashuan Keep - Goddess Bell Chest": FF2LocationData(FF2_LOCATION_BASE_ID + 51, "Kashuan Keep"),
    "Kashuan Keep - Sunfire": FF2LocationData(FF2_LOCATION_BASE_ID + 52, "Kashuan Keep"),

    # === DREADNOUGHT ===
    "Dreadnought - Engine Room": FF2LocationData(FF2_LOCATION_BASE_ID + 60, "Dreadnought"),
    "Dreadnought - Chest 1": FF2LocationData(FF2_LOCATION_BASE_ID + 61, "Dreadnought"),
    "Dreadnought - Chest 2": FF2LocationData(FF2_LOCATION_BASE_ID + 62, "Dreadnought"),

    # === DEIST ===
    "Deist - Wyvern Egg": FF2LocationData(FF2_LOCATION_BASE_ID + 70, "Deist"),
    "Deist Cavern - Chest 1": FF2LocationData(FF2_LOCATION_BASE_ID + 71, "Deist"),
    "Deist Cavern - Pendant": FF2LocationData(FF2_LOCATION_BASE_ID + 72, "Deist"),

    # === COLISEUM ===
    "Coliseum - Victory Reward": FF2LocationData(FF2_LOCATION_BASE_ID + 80, "Coliseum"),

    # === TROPICAL ISLAND ===
    "Tropical Island - Black Mask Chest": FF2LocationData(FF2_LOCATION_BASE_ID + 90, "Tropical Island"),
    "Tropical Island - White Mask Chest": FF2LocationData(FF2_LOCATION_BASE_ID + 91, "Tropical Island"),

    # === MYSIDIAN TOWER ===
    "Mysidian Tower - 1F Chest": FF2LocationData(FF2_LOCATION_BASE_ID + 100, "Mysidian Tower"),
    "Mysidian Tower - 2F Chest": FF2LocationData(FF2_LOCATION_BASE_ID + 101, "Mysidian Tower"),
    "Mysidian Tower - Crystal Rod": FF2LocationData(FF2_LOCATION_BASE_ID + 102, "Mysidian Tower"),
    "Mysidian Tower - White Dragon": FF2LocationData(FF2_LOCATION_BASE_ID + 103, "Mysidian Tower"),
    "Mysidian Tower - Black Dragon": FF2LocationData(FF2_LOCATION_BASE_ID + 104, "Mysidian Tower"),

    # === CASTLE PALAMECIA ===
    "Castle Palamecia - Chest 1": FF2LocationData(FF2_LOCATION_BASE_ID + 110, "Castle Palamecia"),
    "Castle Palamecia - Chest 2": FF2LocationData(FF2_LOCATION_BASE_ID + 111, "Castle Palamecia"),
    "Castle Palamecia - Sun Blade": FF2LocationData(FF2_LOCATION_BASE_ID + 112, "Castle Palamecia"),

    # === PANDAEMONIUM (Final Dungeon) ===
    "Pandaemonium - Chest 1": FF2LocationData(FF2_LOCATION_BASE_ID + 120, "Pandaemonium"),
    "Pandaemonium - Chest 2": FF2LocationData(FF2_LOCATION_BASE_ID + 121, "Pandaemonium"),
    "Pandaemonium - Masamune": FF2LocationData(FF2_LOCATION_BASE_ID + 122, "Pandaemonium"),

    # === VICTORY ===
    "Emperor Defeated": FF2LocationData(FF2_LOCATION_BASE_ID + 200, "Pandaemonium"),
}


def get_location_name_to_id() -> Dict[str, int]:
    """Returns a dictionary mapping location names to their IDs."""
    return {name: data.code for name, data in FF2_LOCATIONS.items()}


def get_locations_by_region() -> Dict[str, List[str]]:
    """Returns locations grouped by region."""
    regions: Dict[str, List[str]] = {}
    for name, data in FF2_LOCATIONS.items():
        if data.region not in regions:
            regions[data.region] = []
        regions[data.region].append(name)
    return regions