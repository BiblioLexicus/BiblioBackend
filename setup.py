import argparse
import logging
import os
import re
import sys
from urllib import request

from django.core.management.utils import get_random_secret_key
from git import Repo, rmtree
from PyInquirer import prompt


def main():
    # Set up Project for testing and deployment

    # Constants
    output_file = ".env"
    html_mover_helper = "https://raw.githubusercontent.com/BBArikL/move_django_html/master/mv_django_html.py"
    mover_helper_file = "mv_helper.py"
    project_path = "./"
    project_name = "Backend"
    operation = "move_to"
    default_html_repository = (
        "https://github.com/BiblioLexicus/BiblioFront.git"  # Private repository for now
    )
    html_repo_path = "./Frontend/"

    # Parse user inputs
    parser = argparse.ArgumentParser(
        description="Setup BiBlioLexicus project.",
        prog="setup.py",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        prefix_chars="-",
    )
    # Project specific
    parser.add_argument(
        "--DB_ENGINE",
        dest="ENGINE",
        type=str,
        default="django.db.backends.mysql",
        help=f"The engine of the databse.{default()}",
    )
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
    parser.add_argument(
        "--DB_PASSWORD",
        type=str,
        default="",
        help=f"the password of the database.{default()}",
    )
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
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "--deploy",
        dest="DEPLOY",
        nargs="?",
        const=True,
        default=False,
        help=f"needed when the application is meant for deployment.{default()}",
    )
    group.add_argument(
        "--debug",
        dest="DEBUG",
        nargs="?",
        const=True,
        default=False,
        help=f"needed when the application is meant for debugging.{default()}",
    )
    parser.add_argument(
        "--auto",
        dest="AUTO",
        nargs="?",
        const=True,
        default=False,
        help=f"uses default variables. Use --DB_PASSWORD <password> at the same time.{default()}",
    )
    parser.add_argument(  # Do not use pretty prompts in CI-CD environment
        "--ci_test",
        dest="CI_TEST",
        nargs="?",
        const=True,
        default=False,
        help=f"Only to be used in a CI environment.{default()}",
    )
    parser.add_argument(
        "--skip_pages",
        dest="SKIP_PAGES",
        nargs="?",
        const=True,
        default=False,
        help=f"if to skip moving html files from another repository.{default()}",
    )
    pages_group = parser.add_mutually_exclusive_group()
    pages_group.add_argument(
        "--default_rep",
        dest="DEFAULT_REP",
        nargs="?",
        const=True,
        default=False,
        help=f"if to clone pages from the default repository.{default()}",
    )
    pages_group.add_argument(
        "--custom_rep",
        dest="CUSTOM_REP",
        nargs="?",
        const=True,
        default=False,
        help=f"if to clone pages from a custom repository.{default()}",
    )
    pages_group.add_argument(
        "--local_rep",
        dest="LOCAL_REP",
        nargs="?",
        const=True,
        default=False,
        help=f"if to get pages from a local repository.{default()}",
    )

    # General
    parser.add_argument(
        "--verbose",
        "-v",
        dest="VERBOSE",
        nargs="?",
        const=True,
        default=False,
        help=f"be verbose.{default()}",
    )
    parser.add_argument("--version", action="version", version="%(prog)s 0.1")

    args = parser.parse_args()

    # Setup logging
    log_level = logging.INFO
    if args.VERBOSE:
        log_level = logging.DEBUG

    logging.basicConfig(stream=sys.stdout, level=log_level, format="%(message)s")
    log = logging.getLogger()

    # Check for good setup
    if args.DEBUG == args.DEPLOY:
        log.error("Please choose between `--deploy` or `--debug` before proceeding!")
        exit(1)

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

    if os.path.exists(output_file) and not args.CI_TEST:
        question = [
            {
                "type": "confirm",
                "name": "overwrite",
                "message": f"The file {output_file} already exist. Do you want to overwrite it?",
                "default": False,
            }
        ]
        if not prompt(question)["overwrite"]:
            log.info("Permission denied to overwrite `.env` file. Terminating setup...")
            exit(0)

    # Set envs
    log.debug("\nSetting up environment variables...")
    envs = {
        "ENGINE": "",
        "DB_NAME": "",
        "DB_USER_ADMIN": "",
        "DB_PASSWORD": "",
        "DB_HOST": "",
        "DB_PORT": "",
        "ORGANISATION_NAME": "",
    }

    # Loop and set env variables
    for env in envs:
        var = getattr(args, env)
        if not args.AUTO and not args.CI_TEST:
            # Manual input for environment variables
            if not env == "ENGINE":
                question = [
                    {
                        "type": "input",
                        "name": "environ",
                        "message": f"Enter the {env} (Default: {var}):",
                        "default": str(var),
                    }
                ]
                var = prompt(question)["environ"]
            else:
                # Engine specific question
                question = [
                    {
                        "type": "list",
                        "name": "ENGTYP",
                        "message": "This project was made specifically for SQL engines, more particularly MariaDB. What engine do you want to use?",
                        "choices": ["MariadB / MySQL engine", "PostgreSQL", "Other"],
                    },
                    {
                        "type": "input",
                        "name": "ENGTYP_NOSQSL",
                        "message": "What other backend do you want to use? (Please type the full django backend)",
                        "when": lambda answers: answers["ENGTYP"] == "Other",
                    },
                ]
                result = prompt(question)

                # For mariadB / MysQL, the engine is already specified
                if result["ENGTYP"] == "PostgreSQL":
                    var = "django.db.backends.postgresql_psycopg2"
                elif result["ENGTYP"] == "Other":
                    var = result["ENGTYP_NOSQSL"]

        envs[env] = var

    # Compile output
    output = "\n".join(
        [f"SECRET_KEY={get_random_secret_key()}"]
        + [f"DEBUG={getattr(args, 'DEBUG')}"]
        + [f"{envv}={envs[envv]}" for envv in envs]
    )

    if not args.CI_TEST:  # No need to verify in CI-CD environment
        # Confirm final envs
        log.info("\nFinal `.env` file output:\n")
        log.info(output + "\n")
        question = [
            {
                "type": "confirm",
                "name": "confirmed",
                "message": "Is this configuration correct?",
                "default": True,
            }
        ]
        answer = prompt(question)

        if not answer[
            "confirmed"
        ]:  # If there was an error in the configuration and the person interrupts the setup
            log.info(
                "\nConfiguration was marked as incorrect, terminating."
                "\nYou can rerun this script with :"
                "\npython setup.py"
                "\nand enter the correct details."
            )
            exit(1)

    log.debug("\nWriting to `.env` file....")  # Write env file
    with open(".env", "w") as f:
        f.write(output)

    # Move html files from other repository / folder
    if not args.SKIP_PAGES and not args.CI_TEST:
        # Getting the html mover
        log.debug("\nGetting the html mover script...")
        log.debug(
            f"This script can be obtained at {html_mover_helper}"
            " for further use in development or other reasons."
        )
        mv_helper = bytes.decode(request.urlopen(html_mover_helper).read())
        log.debug(f"Writing mover file to {mover_helper_file}")
        with open(mover_helper_file, "w") as f:
            f.write(mv_helper)
        log.debug("Write successful!\n")

        if not args.DEFAULT_REP and not args.CUSTOM_REP and not args.LOCAL_REP:
            # Getting the html source
            question = [
                {
                    "type": "list",
                    "name": "html_source",
                    "message": "Where do you want to take the html files from?:",
                    "choices": [
                        "Clone the default repository",
                        "Clone a different repository",
                        "From a local path",
                    ],
                }
            ]

            answer = prompt(question)["html_source"]
        else:
            answer = ""

        # Choose source and clone files if needed
        if answer == "Clone the default repository" or args.DEFAULT_REP:
            log.debug("\nCloning default repo....")
            html_repo = default_html_repository
            os.makedirs(html_repo_path, exist_ok=True)
            Repo.clone_from(html_repo, html_repo_path)
            log.debug("Clone successful!")
        elif answer == "Clone a different repository" or args.CUSTOM_REP:
            question = [
                {
                    "type": "input",
                    "name": "repo",
                    "message": "Enter the link of the repo (ending in `.git`):",
                }
            ]
            html_repo = prompt(question)["repo"]
            log.debug(f"\nCloning repo {html_repo} ...")
            os.makedirs(html_repo_path, exist_ok=True)
            Repo.clone_from(html_repo, html_repo_path)
            log.debug("Cloning successful!")
        elif answer == "From a local path" or args.LOCAL_REP:
            question = [
                {
                    "type": "input",
                    "name": "path",
                    "message": "Enter the path of the folder containing the html files (this path should include a "
                    "folder "
                    "called `html`):",
                    "validate": lambda val: os.path.exists(val),
                }
            ]
            html_repo_path = prompt(question)["path"]
            log.debug(f"\nHTML repo set to {html_repo_path} !")

        html_repo_path += "html/"  # Mover script
        command = (
            f"python {mover_helper_file} --project_path {project_path} --project_name {project_name} "
            f"--operation {operation} --local {html_repo_path} --no_confirm"
        )

        log.info("\nStarting mover script...")
        log.info("> " + command)
        os.system(
            command
        )  # This code is safe. It will only copy the files from the html repository to the project.
        # It can be seen here https://github.com/BBArikL/move_django_html/blob/master/mv_django_html.py
        log.info("Mover script done!")

        log.debug("\nDeleting non-necessary files...")
        # Delete non-necessary files
        os.remove(mover_helper_file)
        if answer != "From a local path" or not args.LOCAL_REP:
            rmtree(re.sub("html/", "", html_repo_path))
        log.debug("Deleting done!")

    # End
    log.info("\nAll done!")


def default():
    return " (default: %(default)s) "


if __name__ == "__main__":
    main()
