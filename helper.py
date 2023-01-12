import vpk

mods = [
    'scripts/items/items_game.txt', 
    'particles/generic_gameplay/radiant_fountain_regen.vpcf_c',
    'particles/items2_fx/teleport_start.vpcf_c',
    'particles/items2_fx/teleport_end.vpcf_c',
    'particles/items_fx/blink_dagger_start.vpcf_c',
    'particles/items_fx/blink_dagger_end.vpcf_c',
    'particles/items_fx/force_staff.vpcf_c',
    'particles/items_fx/cyclone.vpcf_c',
    'particles/items_fx/bottle.vpcf_c',
    'particles/generic_hero_status/hero_levelup.vpcf_c',
    'particles/items2_fx/radiance_owner.vpcf_c',
    'particles/items2_fx/radiance.vpcf_c',
    'particles/items2_fx/mekanism.vpcf_c',
    'particles/items2_fx/mekanism_recipient.vpcf_c',
    'particles/items_fx/chain_lightning.vpcf_c',
    'particles/items2_fx/mjollnir_shield.vpcf_c',
    'particles/econ/attack/attack_modifier_empty.vpcf_c',
    'particles/items4_fx/scepter_aura.vpcf_c',
    'particles/items2_fx/phase_boots.vpcf_c',
    'particles/items2_fx/shivas_guard_active.vpcf_c',
    'particles/items2_fx/shivas_guard_impact.vpcf_c',
    ]

def trimExtension(path):
    path = path.replace("vpcf_c", "vpcf")
    return path

def addExtension(path):
    path = path.replace("vpcf", "vpcf_c")
    return path

def vpkExtractor(pak01_dir, path, save_dir):
    pak1 = vpk.open(pak01_dir)
    pakfile = pak1.get_file(path)
    pakfile.save(save_dir)

def vpkCreator(dir):
    newpak = vpk.new(dir)
    newpak.save('pak01_dir.vpk')