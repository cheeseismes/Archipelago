-- Final Fantasy II Archipelago Connector
-- This script runs in BizHawk and communicates with Archipelago

local socket = require("socket. core")
local json = require("json")

-- ============================================
-- MEMORY ADDRESSES (TODO: These need research!)
-- ============================================
-- These are placeholder addresses - you'll need to find the real ones
-- using BizHawk's RAM Search or an FF2 NES memory map

local ADDR = {
    -- Key Items (each bit might represent a different item)
    KEY_ITEMS = 0x6000,        -- Placeholder!

    -- Chest flags (bits indicating which chests are opened)
    CHEST_FLAGS_START = 0x6100, -- Placeholder!
    CHEST_FLAGS_END = 0x6120,   -- Placeholder!

    -- Player data
    GOLD = 0x601C,              -- Placeholder!

    -- Game state
    CURRENT_MAP = 0x0048,       -- Placeholder!
    IN_BATTLE = 0x00A0,         -- Placeholder!
}

-- ============================================
-- ITEM MAPPING
-- ============================================
-- Maps Archipelago item IDs to how to give them in-game

local ITEM_ID_BASE = 0xFF2000

local KEY_ITEM_FLAGS = {
    [ITEM_ID_BASE + 1] = {addr = 0x6000, bit = 0},   -- Canoe
    [ITEM_ID_BASE + 2] = {addr = 0x6000, bit = 1},   -- Ship
    [ITEM_ID_BASE + 3] = {addr = 0x6000, bit = 2},   -- Airship
    [ITEM_ID_BASE + 4] = {addr = 0x6000, bit = 3},   -- White Mask
    [ITEM_ID_BASE + 5] = {addr = 0x6000, bit = 4},   -- Black Mask
    [ITEM_ID_BASE + 6] = {addr = 0x6000, bit = 5},   -- Crystal Rod
    [ITEM_ID_BASE + 7] = {addr = 0x6000, bit = 6},   -- Goddess Bell
    [ITEM_ID_BASE + 8] = {addr = 0x6000, bit = 7},   -- Egil's Torch
    -- Add more as needed
}

-- ============================================
-- LOCATION MAPPING
-- ============================================
-- Maps chest/event memory to Archipelago location IDs

local LOCATION_ID_BASE = 0xFF2100

local CHEST_LOCATIONS = {
    -- {memory_addr, bit, location_id}
    {0x6100, 0, LOCATION_ID_BASE + 1},   -- Altair - Secret Room
    {0x6100, 1, LOCATION_ID_BASE + 10},  -- Fynn Castle - Throne Room
    -- Add more as you research them
}

-- ============================================
-- STATE TRACKING
-- ============================================

local checked_locations = {}
local received_items = {}
local connection = nil
local game_complete = false

-- ============================================
-- HELPER FUNCTIONS
-- ============================================

local function read_u8(addr)
    return memory.read_u8(addr)
end

local function write_u8(addr, value)
    memory.write_u8(addr, value)
end

local function test_bit(value, bit)
    return (value & (1 << bit)) ~= 0
end

local function set_bit(addr, bit)
    local value = read_u8(addr)
    value = value | (1 << bit)
    write_u8(addr, value)
end

local function is_in_game()
    -- TODO: Implement check for "is the game actually running"
    -- Return false during title screen, menus, etc.
    return true
end

-- ============================================
-- ARCHIPELAGO COMMUNICATION
-- ============================================

local function check_locations()
    -- Check each chest/event location
    for _, loc in ipairs(CHEST_LOCATIONS) do
        local addr, bit, loc_id = loc[1], loc[2], loc[3]

        if not checked_locations[loc_id] then
            local value = read_u8(addr)
            if test_bit(value, bit) then
                checked_locations[loc_id] = true
                print("Location checked: " .. loc_id)
                -- This will be sent to Archipelago
            end
        end
    end
end

local function give_item(item_id)
    -- Give an item received from Archipelago
    local item_data = KEY_ITEM_FLAGS[item_id]

    if item_data then
        set_bit(item_data.addr, item_data.bit)
        print("Received item: " .. item_id)
    else
        print("Unknown item:  " .. item_id)
    end
end

local function process_received_items(items)
    for _, item in ipairs(items) do
        if not received_items[item. index] then
            received_items[item.index] = true
            give_item(item.item)
        end
    end
end

-- ============================================
-- MAIN LOOP
-- ============================================

local function main()
    print("FF2 NES Archipelago Connector loaded!")
    print("NOTE: Memory addresses are placeholders - research needed!")

    while true do
        if is_in_game() then
            check_locations()
        end

        -- Yield to emulator
        emu.frameadvance()
    end
end

-- Start the connector
main()