from typing import Dict, NamedTuple
from BaseClasses import ItemClassification


class FF2ItemData(NamedTuple):
    code: int
    classification: ItemClassification


# Base ID for FF2 NES items - using a unique range
FF2_BASE_ID = 0xFF2000

FF2_KEY_ITEMS: Dict[str, FF2ItemData] = {
    # Vehicles
    "Canoe": FF2ItemData(FF2_BASE_ID + 1, ItemClassification.progression),
    "Ship": FF2ItemData(FF2_BASE_ID + 2, ItemClassification.progression),
    "Airship": FF2ItemData(FF2_BASE_ID + 3, ItemClassification.progression),

    # Masks for Tropical Island
    "White Mask": FF2ItemData(FF2_BASE_ID + 4, ItemClassification.progression),
    "Black Mask": FF2ItemData(FF2_BASE_ID + 5, ItemClassification.progression),

    # Dungeon Access Items
    "Crystal Rod": FF2ItemData(FF2_BASE_ID + 6, ItemClassification.progression),
    "Goddess Bell": FF2ItemData(FF2_BASE_ID + 7, ItemClassification.progression),
    "Egil's Torch": FF2ItemData(FF2_BASE_ID + 8, ItemClassification.progression),
    "Sunfire": FF2ItemData(FF2_BASE_ID + 9, ItemClassification.progression),

    # Story Items
    "Mithril": FF2ItemData(FF2_BASE_ID + 10, ItemClassification.progression),
    "Pendant": FF2ItemData(FF2_BASE_ID + 11, ItemClassification.progression),
    "Ring": FF2ItemData(FF2_BASE_ID + 12, ItemClassification.progression),
    "Wyvern Egg": FF2ItemData(FF2_BASE_ID + 13, ItemClassification.progression),

    # Endgame Items
    "White Dragon": FF2ItemData(FF2_BASE_ID + 14, ItemClassification.progression),
    "Black Dragon": FF2ItemData(FF2_BASE_ID + 15, ItemClassification.progression),
}

# Filler items - consumables that fill extra locations
FF2_FILLER_ITEMS: Dict[str, FF2ItemData] = {
    "Potion": FF2ItemData(FF2_BASE_ID + 100, ItemClassification.filler),
    "Hi-Potion": FF2ItemData(FF2_BASE_ID + 101, ItemClassification.filler),
    "Ether": FF2ItemData(FF2_BASE_ID + 102, ItemClassification.filler),
    "Phoenix Down": FF2ItemData(FF2_BASE_ID + 103, ItemClassification.filler),
    "Antidote": FF2ItemData(FF2_BASE_ID + 104, ItemClassification.filler),
    "Cross": FF2ItemData(FF2_BASE_ID + 105, ItemClassification.filler),
    "Mallet": FF2ItemData(FF2_BASE_ID + 106, ItemClassification.filler),
    "Maiden's Kiss": FF2ItemData(FF2_BASE_ID + 107, ItemClassification.filler),
    "Gold Needle": FF2ItemData(FF2_BASE_ID + 108, ItemClassification.filler),
    "Cottage": FF2ItemData(FF2_BASE_ID + 109, ItemClassification.filler),
    "Elixir": FF2ItemData(FF2_BASE_ID + 110, ItemClassification.useful),
    "Gil 100": FF2ItemData(FF2_BASE_ID + 111, ItemClassification.filler),
    "Gil 500": FF2ItemData(FF2_BASE_ID + 112, ItemClassification.filler),
    "Gil 1000": FF2ItemData(FF2_BASE_ID + 113, ItemClassification.filler),
}

# Combined dictionary for easy lookup
ALL_ITEMS: Dict[str, FF2ItemData] = {
    **FF2_KEY_ITEMS,
    **FF2_FILLER_ITEMS,
}


def get_item_name_to_id() -> Dict[str, int]:
    """Returns a dictionary mapping item names to their IDs."""
    return {name: data.code for name, data in ALL_ITEMS.items()}