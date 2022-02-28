import argparse
import logging
import os
import sys

from django.core.management.utils import get_random_secret_key


def main():
    # Set up Project for testing and deployment
    # TODO: Automatic moving of html files with https://github.com/BBArikL/move_django_html

    # Constants
    output_file = ".env"

    # Parse user inputs
    parser = argparse.ArgumentParser(
        description="Setup BiBlioLexicus project.",
        prog="BiblioLexicus Setup",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        prefix_chars="-",
    )
    # Project specific
    parser.add_argument(
        "--DB_NAME",
        type=str,
        default="BiblioLexicusDB",
        help=f"the name of the database.{default()}",
    )
    parser.add_argument(
        "--DB_USER_ADMIN",
        type=str,
        default="DB_ADMIN",
        help=f"the name of the admin of the database.{default()}",
    )
    parser.add_argument("--DB_PASSWORD", type=str, help="the password of the database.")
    parser.add_argument(
        "--DB_HOST",
        type=str,
        default="localhost",
        help=f"the host of the database.{default()}",
    )
    parser.add_argument(
        "--DB_PORT",
        type=int,
        default=3306,
        help=f"the port where the database is listening on.{default()}",
    )
    parser.add_argument(
        "--ORG_NAME",
        dest="ORGANISATION_NAME",
        type=str,
        default="BiblioLexicus",
        help=f"The name of the organisation.{default()}",
    )
    parser.add_argument(
        "--deploy",
        dest="DEBUG",
        nargs="?",
        const=False,
        default=True,
        help=f"needed when the application is meant for deployment.{default()}",
    )
    parser.add_argument(
        "--auto",
        nargs="?",
        const=True,
        default=False,
        help="uses default variables. Use --DB_PASSWORD <password> at the same time.",
    )

    # General
    parser.add_argument(
        "--verbose", "-v", nargs="?", const=True, default=False, help="be verbose"
    )
    parser.add_argument("--version", action="version", version="%(prog)s 0.1")

    args = parser.parse_args()

    # Setup logging
    log_level = logging.INFO
    if args.verbose:
        log_level = logging.DEBUG

    logging.basicConfig(stream=sys.stdout, level=log_level, format="%(message)s")
    log = logging.getLogger()

    # Start of configuration
    log.info(
        """
     ____  _ _     _ _       _              _
    | __ )(_| |__ | (_) ___ | |    _____  _(_) ___ _   _ ___
    |  _ \\| | '_ \\| | |/ _ \\| |   / _ \\ \\/ | |/ __| | | / __|
    | |_) | | |_) | | | (_) | |__|  __/>  <| | (__| |_| \\__ \\
    |____/|_|_.__/|_|_|\\___/|_____\\___/_/\\_|_|\\___|\\__,_|___/
    
    Welcome to the BiblioLexicus' setup script! This script will setup the project base configuration files.
    \n
    """
    )

    if os.path.exists(output_file):
        choice = input(
            f"The file {output_file} already exist. Do you want to overwrite it? (y/n): "
        )
        if len(choice) < 1 or choice[0].lower() != "y":
            log.info("Terminating setup...")
            exit(0)

    # Set envs
    log.debug("\nSetting up environnement variables...")
    envs = {
        "DB_NAME": "",
        "DB_USER_ADMIN": "",
        "DB_PASSWORD": "",
        "DB_HOST": "",
        "DB_PORT": "",
        "ORGANISATION_NAME": "",
    }

    for env in envs:
        var = getattr(args, env)
        if not args.auto:
            # Manual input for environnements variables
            var = input(f"Enter the {env} (Default : {getattr(args, env)}): ")

            if var == "":
                var = getattr(args, env)

        envs[env] = var

    output = "\n".join(
        [f"SECRET_KEY={get_random_secret_key()}"]
        + [f"DEBUG={getattr(args, 'DEBUG')}"]
        + [f"{envv}={envs[envv]}" for envv in envs]
    )

    log.debug("\nWriting to `.env` file....")
    with open(".env", "w") as f:
        f.write(output)

    # End
    log.info("All done!")


def default():
    return " (default: %(default)s) "


if __name__ == "__main__":
    main()
