import argparse

from palworld_pal_editor.utils import LOGGER
from palworld_pal_editor.config import Config
from palworld_pal_editor.data_provider import I18N_LIST


def setup_config_from_args():
    parser = argparse.ArgumentParser(description="Your application description here.")
    parser.add_argument('--lang', type=str, help=f'Language for the application, options: {", ".join(I18N_LIST)}..', default='en')
    parser.add_argument('--cli', action='store_true', help='Enable CLI mode.', default=True) # TODO remove default=True
    parser.add_argument('--debug', action='store_true', help='Debug option, mimic interactive mode for VSCode debug launch.')
    parser.add_argument('--path', type=str, help='Path to the save folder, the one contains Level.sav', default=None)
    # Unused:
    parser.add_argument('--gui', action='store_true', help='Enable GUI mode.')
    parser.add_argument('--web', action='store_true', help='Enable WebUI.')
    parser.add_argument('--port', type=int, help='Port used for WebUI mode.', default=58080)

    args = parser.parse_args()

    Config.i18n = args.lang
    Config.cli = args.cli
    Config.gui = args.gui
    Config.web = args.web
    Config.port = args.port
    Config.debug = args.debug
    Config.path = args.path

    if args.lang not in I18N_LIST:
        Config.i18n = I18N_LIST[0]

def main():
    setup_config_from_args()
    print(f"Language: {Config.i18n}, CLI mode: {Config.cli}")
    if Config.cli:
        from palworld_pal_editor.cli import main as cli_main
        globals().update(cli_main())
    elif Config.gui:
        raise NotImplementedError("No GUI Mode Yet, Run with --cli.")
    elif Config.web:
        raise NotImplementedError("No WebUI Mode Yet, Run with --cli.")
    else:
        raise NotImplementedError("Unimplemented Mode.")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        LOGGER.error(f"Exception caught on __main__: {e}")
