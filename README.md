# Palworld Pal Editor

## What is this?

***This is a WIP Palworld pal editor, still in very early stage.***

***I've only tested this tool on my save, it may not work properly for you.***

***Always backup your save in case corruption happens.***

***Thankfully, this tool will not modify things you'd never asked for, and you can always inspect raw pal data.***

## How to use

1. Install Python 3.11+
2. Clone/Download the code
3. In the project directory, run `setup_and_run.ps1` for Windows Powershell, or `setup_and_run.sh` on Unix-like OS.

- There is also a pre-built binary for Windows.

### What You Can Do

#### Safe

- [x] List Players and Pals
- [x] Inspect Pal Stats
- [x] Change Pal Gender
- [x] Toggle BOSS / Rare
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

#### Not Yet Available

- [ ] Remove Pal Sicks
- [ ] Food Buff?
- [ ] GUI

### Change Language?

- You can modify the script to have it run with --lang=zh-CN
- Or you can run lang("zh-CN") anytime after the initial save loading

## Video

(old, but you get the idea) <https://github.com/KrisCris/Palworld-Pal-Editor/assets/38860226/02284dda-f1d7-40af-b12d-6b4ae11d4113>

## Roadmap

***This tool is still in early stage, and only works in an Python interactive mode.***

- [ ] Remove Pal Sicks
- [ ] Food Buff?
- [ ] GUI
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
2. For practicing of my 2-year-untouched Python skills.
3. After PR'd several times to PalEdit (and MagicBear's fork, which eventually merged to the upstream), I just don't feel like contributing to that project anymore. ***Reasons?***
   1. I've helped enough bug fixings, but there're always severe bugs popping up in the ***release*** build, and no ASAP hotfixs for most of the time.
   2. I am tired of dealing with badly structured code. Without reconstructing the entire project, I am literally adding extra layers of shit to it.
   3. I've never been credited for fixing those game-breaking bugs, but I never cared. However the author treated me like a dumb fuck when I pointed out an obvious bug on Discord, even after I PR'd a fix, and clarified the reason with video and screenshots. They just never borther check it :/ Update: After I convinced this guy that the bug was true, they fixed it sliently after a week, leaving my PR open, even though the changes are exact the same, interesting.
