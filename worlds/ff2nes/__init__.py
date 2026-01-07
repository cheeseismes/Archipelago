from typing import Dict, ClassVar, List

from BaseClasses import Item, Location, MultiWorld, Tutorial, ItemClassification, Region
from worlds.AutoWorld import World, WebWorld

from .Items import ALL_ITEMS, FF2_KEY_ITEMS, FF2_FILLER_ITEMS, get_item_name_to_id
from .Locations import FF2_LOCATIONS, get_location_name_to_id, get_locations_by_region
from .Rules import set_rules as set_world_rules


class FF2NESWebWorld(WebWorld):
    theme = "ice"
    tutorials = [Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up Final Fantasy II NES for Archipelago multiworld.",
        "English",
        "setup_en. md",
        "setup/en",
        ["cheeseismes"]
    )]


class FF2NESWorld(World):
    """
    Final Fantasy II for the NES (1988) - Join Firion and the Wild Rose Rebellion
    in their fight against the Palamecian Empire. This randomizer shuffles key items,
    dungeons, and progression across the multiworld.
    """

    game = "Final Fantasy II NES"
    web = FF2NESWebWorld()

    item_name_to_id: ClassVar[Dict[str, int]] = get_item_name_to_id()
    location_name_to_id: ClassVar[Dict[str, int]] = get_location_name_to_id()

    def __init__(self, multiworld: MultiWorld, player: int):
        super().__init__(multiworld, player)

    def create_item(self, name: str) -> Item:
        """Create an item for this world."""
        item_data = ALL_ITEMS.get(name)
        if item_data:
            return Item(name, item_data.classification, item_data.code, self.player)
        return Item(name, ItemClassification.filler, None, self.player)

    def create_items(self) -> None:
        """Add items to the multiworld pool."""
        item_pool: List[Item] = []

        # Add all key items
        for item_name in FF2_KEY_ITEMS.keys():
            item_pool.append(self.create_item(item_name))

        # Calculate how many filler items we need
        num_locations = len(FF2_LOCATIONS)
        num_key_items = len(FF2_KEY_ITEMS)
        num_filler_needed = num_locations - num_key_items

        # Add filler items
        filler_items = list(FF2_FILLER_ITEMS.keys())
        for i in range(num_filler_needed):
            filler_name = filler_items[i % len(filler_items)]
            item_pool.append(self.create_item(filler_name))

        self.multiworld.itempool += item_pool

    def create_regions(self) -> None:
        """Create the game's regions and locations."""
        menu_region = Region("Menu", self.player, self.multiworld)
        self.multiworld.regions.append(menu_region)

        locations_by_region = get_locations_by_region()

        created_regions: Dict[str, Region] = {}
        for region_name in locations_by_region.keys():
            region = Region(region_name, self.player, self.multiworld)
            created_regions[region_name] = region
            self.multiworld.regions.append(region)

            for loc_name in locations_by_region[region_name]:
                loc_data = FF2_LOCATIONS[loc_name]
                location = Location(self.player, loc_name, loc_data.code, region)
                region.locations.append(location)

        # Connect menu to starting region
        if "Altair" in created_regions:
            menu_region.connect(created_regions["Altair"])

        # Connect all regions to Altair (rules handle access requirements)
        for region_name, region in created_regions.items():
            if region_name != "Altair":
                created_regions["Altair"].connect(region)

    def set_rules(self) -> None:
        """Set access rules for locations."""
        set_world_rules(self)

    def get_filler_item_name(self) -> str:
        """Return a random filler item name."""
        return self.multiworld.random.choice(list(FF2_FILLER_ITEMS.keys()))