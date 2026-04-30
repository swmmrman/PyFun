#!/usr/bin/python
import pyautogui
import sys
import time
targ = (2560 / 2, 1440 / 2)
time.sleep(1)
if len(sys.argv) > 1:
    gear_type = 'cheat'
else:
    gear_type = 'regular'
gear = {
    "cheat": {
        "head": "netherite_helmet{Enchantments:[{id:protection,lvl:255},{id:thorns,lvl:255},{id:mending,lvl:1}]}",
        "chest": "netherite_chestplate{Enchantments:[{id:protection,lvl:255},{id:thorns,lvl:255},{id:mending,lvl:1}]}",
        "legs": "netherite_leggings{Enchantments:[{id:protection,lvl:255},{id:thorns,lvl:255},{id:mending,lvl:1}]}",
        "feet": "netherite_boots{Enchantments:[{id:protection,lvl:255},{id:feather_falling,lvl:255},{id:thorns,lvl:255},{id:mending,lvl:1}]}",
        "sword": "netherite_sword{Enchantments:[{id:sharpness,lvl:255},{id:knockback,lvl:75},{id:mending,lvl:1},{id:looting,lvl:255}]}",
        "extra": "netherite_sword{display:{Name:'[{\"text\":\"Ender Remover\",\"italic\":true,\"color\":\"dark_red\",\
                                    \"bold\":true}]'}, Enchantments:[{id:sharpness,lvl:1},{id:knockback,lvl:75}]}",
        "bow": "bow{Enchantments:[{id:power,lvl:255},{id:punch,lvl:200}]}",
    },
    "regular": {
        "head": "iron_helmet",
        "chest": "iron_chestplate",
        "legs": "iron_leggings",
        "feet": "iron_boots",
        "sword": "iron_sword",
        "extra": "stone 64",
        "bow": "bow"
    },
}
pyautogui.press("t")
pyautogui.write(f"/give swmmrman {gear[gear_type]['head']}")
pyautogui.press("enter")
pyautogui.sleep(.4)
pyautogui.rightClick()
pyautogui.press("t")
pyautogui.write(f"/give swmmrman {gear[gear_type]['chest']}")
pyautogui.press("enter")
pyautogui.sleep(.4)
pyautogui.rightClick()
pyautogui.press("t")
pyautogui.write(f"/give swmmrman {gear[gear_type]['legs']}")
pyautogui.press("enter")
pyautogui.sleep(.4)
pyautogui.rightClick()
pyautogui.press("t")
pyautogui.write(f"/give swmmrman {gear[gear_type]['feet']}")
pyautogui.press("enter")
pyautogui.sleep(.4)
pyautogui.rightClick()
pyautogui.press("t")
pyautogui.write("/give swmmrman shield")
pyautogui.press("enter")
pyautogui.sleep(.4)
pyautogui.press("f")
pyautogui.press("t")
pyautogui.write(f"/give swmmrman {gear[gear_type]['sword']}")
pyautogui.press("enter")
pyautogui.press("t")
pyautogui.write(f"/give swmmrman {gear[gear_type]['bow']}")
pyautogui.press("enter")
pyautogui.press("t")
pyautogui.write("/give swmmrman netherite_pickaxe{Enchantments:[{id:efficiency,lvl:5},{id:fortune,lvl:255}]}")
pyautogui.press("enter")
pyautogui.press("t")
pyautogui.write("/give swmmrman arrow 128")
pyautogui.press("enter")
pyautogui.press("t")
pyautogui.write("/give swmmrman ender_pearl 16")
pyautogui.press("enter")
pyautogui.press("t")
pyautogui.write("/give swmmrman water_bucket")
pyautogui.press("enter")
pyautogui.press("9")
pyautogui.sleep(.4)
pyautogui.press("t")
pyautogui.write(f"/give swmmrman {gear[gear_type]['extra']}")
pyautogui.press("enter")

pyautogui.press("t")
pyautogui.write("/give swmmrman cooked_beef 64")
pyautogui.press("enter")
pyautogui.sleep(1)
pyautogui.press("1")
pyautogui.press("t")
pyautogui.write("/fill ~1 ~-1 ~ ~2 ~-1 ~ end_portal")
pyautogui.press("enter")
pyautogui.press("t")
pyautogui.write("/fill ~3 ~-1 ~-1 ~5 ~-1 ~1 end_portal")
pyautogui.press("enter")
