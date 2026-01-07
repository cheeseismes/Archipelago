from typing import Dict, ClassVar

from BaseClasses import Item, Location, MultiWorld, Tutorial, ItemClassification, Region
from worlds.AutoWorld import World, WebWorld


class FF2NESWebWorld(WebWorld):
    theme = "ice"
    tutorials = [Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up Final Fantasy II NES for Archipelago multiworld.",
        "English",
        "setup_en.md",
        "setup/en",
        ["cheeseismes"]
    )]


class FF2NESWorld(World):
    """
    Final Fantasy II for the NES (1988) - Join Firion and the Wild Rose Rebellion
    in their fight against the Palamecian Empire.  This randomizer shuffles key items,
    dungeons, and progression across the multiworld.
    """
    
    game = "Final Fantasy II NES"
    web = FF2NESWebWorld()
    
    item_name_to_id:  ClassVar[Dict[str, int]] = {
        "Canoe": 0xFF2001,
        "Ship": 0xFF2002,
        "Airship": 0xFF2003,
    }
    
    location_name_to_id: ClassVar[Dict[str, int]] = {
        "Altair - Starting Chest": 0xFF2101,
        "Fynn Castle - Throne Room": 0xFF2102,
    }
    
    def __init__(self, multiworld: MultiWorld, player: int):
        super().__init__(multiworld, player)
    
    def create_item(self, name:  str) -> Item:
        item_id = self. item_name_to_id. get(name, None)
        classification = ItemClassification. progression
        return Item(name, classification, item_id, self.player)
    
    def create_items(self) -> None:
        for item_name in self.item_name_to_id.keys():
            self.multiworld.itempool.append(self. create_item(item_name))
    
    def create_regions(self) -> None:
        menu_region = Region("Menu", self.player, self.multiworld)
        self.multiworld.regions.append(menu_region)
        
        game_region = Region("Final Fantasy II", self. player, self.multiworld)
        self.multiworld.regions.append(game_region)
        
        menu_region.connect(game_region)
        
        for loc_name, loc_id in self.location_name_to_id.items():
            location = Location(self.player, loc_name, loc_id, game_region)
            game_region.locations.append(location)
    
    def set_rules(self) -> None:
        pass
    
    def generate_basic(self) -> None:
        pass