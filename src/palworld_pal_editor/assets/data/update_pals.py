# https://paldb.cc/cn/Pals_Table
# https://paldb.cc/cn/NPCs_Table
# const items = document.querySelectorAll('a[data-hover]')
# const list = []
# for (const item of items) {
#     list.push(item.innerHTML)
# }

# check if the number of BOSS_ variant is the same as that of the non-BOSS version.
# remove BOSS_
import json

pal_list = [
    "RAID_NightLady",
    "RAID_NightLady_Dark",
    "RAID_NightLady_Dark_2",
    "GYM_BlackGriffon",
    "GYM_ElecPanda",
    "GYM_Horus",
    "GYM_LilyQueen",
    "GYM_ThunderDragonMan",
    "BadCatgirl",
    "BlueberryFairy",
    "BrownRabbit",
    "ElecLion",
    "FeatherOstrich",
    "GoldenHorse",
    "PinkKangaroo",
    "ScorpionMan",
    "SifuDog",
    "TentacleTurtle",
    "WingGolem",
    "BeardedDragon",
    "WaterLizard",
    "GuardianDog",
    "GrassDragon",
    "Anubis",
    "Baphomet",
    "Baphomet_Dark",
    "Bastet",
    "Bastet_Ice",
    "Boar",
    "Carbunclo",
    "ColorfulBird",
    "Deer",
    "Deer_Ground",
    "DrillGame",
    "Eagle",
    "ElecPanda",
    "Ganesha",
    "Garm",
    "Gorilla",
    "Gorilla_Ground",
    "Hedgehog",
    "Hedgehog_Ice",
    "Kirin",
    "Kitsunebi",
    "LittleBriarRose",
    "Mutant",
    "Penguin",
    "RaijinDaughter",
    "SharkKid",
    "SharkKid_Fire",
    "SheepBall",
    "Umihebi",
    "Umihebi_Fire",
    "Werewolf",
    "WindChimes",
    "WindChimes_Ice",
    "Suzaku",
    "Suzaku_Water",
    "FireKirin",
    "FireKirin_Dark",
    "FairyDragon",
    "FairyDragon_Water",
    "SweetsSheep",
    "WhiteTiger",
    "Alpaca",
    "Serpent",
    "Serpent_Ground",
    "DarkCrow",
    "BlueDragon",
    "PinkCat",
    "NegativeKoala",
    "FengyunDeeper",
    "VolcanicMonster",
    "VolcanicMonster_Ice",
    "GhostBeast",
    "RobinHood",
    "RobinHood_Ground",
    "LazyDragon",
    "LazyDragon_Electric",
    "AmaterasuWolf",
    "LizardMan",
    "LizardMan_Fire",
    "BluePlatypus",
    "BlackFurDragon",
    "BirdDragon",
    "BirdDragon_Ice",
    "ChickenPal",
    "FlowerDinosaur",
    "FlowerDinosaur_Electric",
    "ElecCat",
    "IceHorse",
    "IceHorse_Dark",
    "GrassMammoth",
    "GrassMammoth_Ice",
    "CatVampire",
    "SakuraSaurus",
    "SakuraSaurus_Water",
    "Horus",
    "KingBahamut",
    "KingBahamut_Dragon",
    "BerryGoat",
    "IceDeer",
    "BlackGriffon",
    "WhiteMoth",
    "CuteFox",
    "FoxMage",
    "FoxMage_Dark",
    "PinkLizard",
    "WizardOwl",
    "Kelpie",
    "Kelpie_Fire",
    "NegativeOctopus",
    "CowPal",
    "Yeti",
    "Yeti_Grass",
    "VioletFairy",
    "HawkBird",
    "FlowerRabbit",
    "LilyQueen",
    "LilyQueen_Dark",
    "QueenBee",
    "SoldierBee",
    "CatBat",
    "GrassPanda",
    "GrassPanda_Electric",
    "FlameBuffalo",
    "ThunderDog",
    "CuteMole",
    "BlackMetalDragon",
    "GrassRabbitMan",
    "IceFox",
    "JetDragon",
    "DreamDemon",
    "Monkey",
    "Manticore",
    "Manticore_Dark",
    "KingAlpaca",
    "KingAlpaca_Ice",
    "PlantSlime",
    "PlantSlime_Flower",
    "DarkMutant",
    "MopBaby",
    "MopKing",
    "CatMage",
    "CatMage_Fire",
    "PinkRabbit",
    "ThunderBird",
    "HerculesBeetle",
    "HerculesBeetle_Ground",
    "SaintCentaur",
    "NightFox",
    "CaptainPenguin",
    "WeaselDragon",
    "WeaselDragon_Fire",
    "SkyDragon",
    "SkyDragon_Grass",
    "HadesBird",
    "HadesBird_Electric",
    "RedArmorBird",
    "Ronin",
    "Ronin_Dark",
    "FlyingManta",
    "BlackCentaur",
    "FlowerDoll",
    "NaughtyCat",
    "CuteButterfly",
    "DarkScorpion",
    "DarkScorpion_Ground",
    "ThunderDragonMan",
    "WoolFox",
    "LazyCatfish",
    "LavaGirl",
    "FlameBambi",
    "NightLady",
    "NightLady_Dark",
    "VolcanoDragon",
    "DarkAlien",
    "DarkMechaDragon",
    "LeafPrincess",
    "GhostRabbit",
    "NightBlueHorse",
    "WhiteAlienDragon",
    "WhiteShieldDragon",
    "MushroomDragon",
    "MushroomDragon_Dark",
    "SmallArmadillo",
    "BlackPuppy",
    "KendoFrog",
    "CandleGhost",
    "WhiteDeer",
    "KingWhale",
    "MysteryMask",
    "HoodGhost",
    "Sekhmet",
    "ElecLizard",
    "MoonQueen",
    "GrimGirl",
    "PurpleSpider",
    "BlueThunderHorse",
    "RockBeast"
]

human = [
    "TestNPC",
    "Hunter_Rifle",
    "Hunter_Handgun",
    "Hunter_Shotgun",
    "Hunter_RocketLauncher",
    "Hunter_Bat",
    "Hunter_Grenade",
    "Hunter_FlameThrower",
    "Hunter_Fat_GatlingGun",
    "Police_Rifle",
    "Police_Handgun",
    "Police_Shotgun",
    "MobuCitizen",
    "MobuVillager",
    "QuestMan",
    "SalesPerson",
    "VisitingMerchant",
    "WeaponsDealer",
    "PalDealer",
    "Inspector",
    "PalTrader",
    "GoodwillAmbassador",
    "Robbery_Leader",
    "Robbery_Minion",
    "Guard_Rifle",
    "Guard_Shotgun",
    "TestAssassin",
    "Visitor_Hunter_Rifle",
    "Visitor_Present",
    "SecurityDrone",
    "FireCult_Rifle",
    "FireCult_FlameThrower",
    "Believer_Bat",
    "Believer_CrossBow",
    "Male_People02",
    "Male_People03",
    "Female_People02",
    "Female_People03",
    "Male_Trader01",
    "Male_Trader02",
    "Male_Trader03",
    "Male_DarkTrader01",
    "Male_DesertPeople01",
    "Female_DesertPeople02",
    "MobuCitizen_Male",
    "Male_Soldier01",
    "Female_Soldier01",
    "Male_Police_old",
    "Male_Scientist01_LaserRifle",
    "Scientist_FlameThrower",
    "SalesPerson_Desert",
    "SalesPerson_Desert2",
    "PalDealer_Desert",
    "SalesPerson_Volcano",
    "SalesPerson_Volcano2",
    "PalDealer_Volcano",
    "SalesPerson_Wander",
    "RandomEventShop",
    "Hunter_Rifle_Invader",
    "Hunter_Handgun_Invader",
    "Hunter_Shotgun_Invader",
    "Hunter_RocketLauncher_Invader",
    "Hunter_Bat_Invader",
    "Hunter_Grenade_Invader",
    "Hunter_FlameThrower_Invader",
    "Hunter_Fat_GatlingGun_Invader",
    "Believer_Bat_Invader",
    "Believer_CrossBow_Invader",
    "FireCult_Rifle_Invader",
    "FireCult_FlameThrower_Invader",
    "Male_Scientist01_LaserRifle_Invader",
    "Scientist_FlameThrower_Invader",
    "Believer_Fat_GatlingGun",
    "Male_Soldier02",
    "Female_Soldier02",
    "Male_Soldier03",
    "Female_Soldier03",
    "Male_Soldier04",
    "Female_Soldier04"
]


with open("./pal_data.json", "r", encoding="utf-8") as pal_file:
    pal_data: dict = json.load(pal_file)

current_pals = []
current_human = []
for pal in pal_data:
    if pal_data[pal].get("Human", False):
        current_human.append(pal)
    else:
        current_pals.append(pal)

        
print("\n\n#### current_pals - new_pal: ")
print(set(current_pals) - set(pal_list))

print("\n\n#### new_pal - current_pals: ")
print("\n".join(set(pal_list) - set(current_pals)))

print("\n\n#### current_human - new_human: ")
print("\n".join(set(current_human) - set(human)))

print("\n\n#### new_human - current_human : ")
print("\n".join(set(human) - set(current_human)))