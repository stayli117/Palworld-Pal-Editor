# Palworld Pal Editor

## What is this?

### A Palworld Pal Editor developed by _connlost with ❤️ ~~(yeah i don't too lazy to change github username)~~

***I've only tested this tool on my save, it may not work properly for you.***

***Always backup your save in case corruption happens. (The tool does backup files for you.)***

***LET ME KNOW IF ANY BUG PRESENTS.***

## How to use

### 1. Directly Run the Code

1. Install Python 3.11+
2. Clone / Download the code
3. In the project directory, run `setup_and_run.ps1` for Windows Powershell, or `setup_and_run.sh` on Unix-like OS.
4. Optional Params:
   - `--password yourPW` Login Auth, you may want this if you are running web mode.
   - `--mode <gui | web | cli>` You can launch the program in either `gui`, `web` or `cli` mode.
   - `--path /path/to/save/folder` Provide the path to the folder containing Level.sav.
   - `--port 8080` Port for web mode.
   - `--lang <zh-CN | en>` Currently supporting `zh-CN` and `en`. (Currrently hardcoded UI texts are English only.)
   - `--i` for enable interactive mode, you may want to use with `cli` mode.
5. You can change language in `cli` mode by calling `lang($LANG_CODE)`.

### 2. Use Pre-Built Binary

1. Download from GitHub Release Page, may not be bundled with the latest code.
2. Also support command line arguments mentioned above.

### 3. Docker Container

1. Clone the code.
2. You may want to take a look at `./docker/docker-compose.yml`, and do some modification.
3. Run `./build_and_run_docker.sh`, or just manually run the commends if you are using Windows.

### What You Can Do

- [x] List Players and Pals
- [x] Inspect Pal Stats
- [x] Change Pal Gender
- [x] Toggle BOSS / Rare / Tower
- [x] Change Pal NickName
- [x] Add / Remove Pal Learned Attacks
- [x] Add / Remove Pal Equipped Attacks
- [x] Change Pal Level / Exp
- [x] Change Pal Condenser Level
- [x] Change Pal Soul Levels
- [x] Change CharacterID (Pal Species)
- [x] Change Pal Passive Skills
- [x] Change Pal IV
- [x] Calculate MaxHP
- [x] Remove Pal Sicks
- [x] Edit Food Buff Timer (Only if the pal has food buff, and cli only)

## Video

- CLI:
  - (old, but you get the idea) <https://github.com/KrisCris/Palworld-Pal-Editor/assets/38860226/02284dda-f1d7-40af-b12d-6b4ae11d4113>
- GUI / WEB
  - 

## Possible Roadmap? (NO ETA)

- [ ] Improve WebUI (I am bad at frontend dev, sorry! Contribution appreciated.)
- [ ] Real GUI, or maybe just a Terminal GUI using [Textual](https://textualize.io/).
- [ ] Add / Remove Pal (I mean, you can just catch a pal and set it to something else.)
- [ ] Move Pal to Different Slots?
- [ ] More Stuff...

## Thanks

- Fast game save loading code by [MagicBear](https://github.com/magicbear).
- Save conversion between GVAS and `.sav` by [palworld-save-tools](https://github.com/cheahjs/palworld-save-tools).
- Inspired by [MagicBear](https://github.com/magicbear)'s awesome [Palworld-Server-Toolkit](https://github.com/magicbear/palworld-server-toolkit).
- Inspired by [EternalWraith](https://github.com/EternalWraith)'s [PalEdit](https://github.com/EternalWraith/PalEdit).

## Why?

**Q: There is already a pal editor called PalEdit, is there any need to make another one?**

**A: I made this tool for many reasons:**

1. I made the tool for my friends who spent time playing this game with me ❤.
2. For practicing my 2-year-untouched Python skills.
3. I don't want to answer it. And you probably don't want to hear my shit talk.
