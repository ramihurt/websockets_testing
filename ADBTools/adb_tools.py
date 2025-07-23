import subprocess
import os
from colorama import init, Fore

from WebsocketHelper.MessageEmitter import MessageEmitter
from WebsocketHelper.MessageSender import MessageSender
from flask_socketio import SocketIO

# Initialize colorama
init()

path_to_scripts = "<PATH TO SCRIPTS>"
timeout_seconds = 3
os.environ["ADB_PATH"] = "<PATH TO ADB>"
os.environ["DPATH"] = "<PATH TO LOGS>"

class AdbTools:
    def __init__(self, socketio: SocketIO):
        self.emitter = MessageEmitter(socketio)  # Pass the socketio instance
        self.sender = MessageSender(self.emitter)

    def trigger_message(self, message):
        """ Prints message black on frontend and white on backend terminal"""
        colored_message = { "text": message, "color":"#000000"} # Black for white background on frontend
        print(f"{Fore.WHITE} {message} {Fore.RESET}") # White for black terminal
        self.sender.send_message(colored_message)

    def trigger_green_message(self, message):
        """ Prints message green on frontend and green on backend terminal"""
        colored_message = { "text": message, "color":"#00bf0c" }
        print(f"{Fore.GREEN} {message} {Fore.RESET}")
        self.sender.send_message(colored_message)

    def trigger_warning(self, message):
        """ Prints warning message orange on frontend and yellow on backend terminal"""
        colored_message = { "text": message, "color":"#ffc80d"} # Orange
        print(f"{Fore.YELLOW} {message} {Fore.RESET}")
        self.sender.send_message(colored_message)

    def trigger_error(self, message):
        """ Prints error message red on frontend and red on backend terminal"""
        colored_message = { "text": message, "color": "#df0000"} # Red
        print(f"{Fore.RED} {message} {Fore.RESET}")
        self.sender.send_message(colored_message)

    # -------------------------
    # DCM version check
    # -------------------------
    def version_check(self):
        """ Checks the DCM version"""
        try:
            header = "DCM Version Check"
            separator = "*" * len(header)

            self.trigger_message(separator)
            self.trigger_green_message(header)
            self.trigger_message(separator)

            result = subprocess.run(
                [path_to_scripts + "version_check.bat"],
                env=os.environ,
                timeout=timeout_seconds,
                shell=True,
                capture_output=True,
                text=True,
                check=True
            )

            self.trigger_message(result.stdout)
            self.trigger_green_message("Version check completed successfully")

        except subprocess.TimeoutExpired:
            self.trigger_error(f"Error: Version check command timed out after {timeout_seconds} seconds.")
            self.trigger_error(f"Please ensure the ignition is on for DCM.")
            self.trigger_warning(f"Version check completed with errors.")
        except subprocess.CalledProcessError as e:
            self.trigger_error(f"Error: Command '{e.cmd}' failed with return code {e.returncode}.")
            self.trigger_error(f"Error message: {e.stderr.strip()}")
            self.trigger_warning(f"Version check completed with errors.")
        except Exception as e:
            self.trigger_error(f"An unexpected error occurred: {e}")
            self.trigger_warning(f"Version check completed with errors.")


def ppi_check():
    try:
        header = f"{Fore.GREEN}Checking PPI Settings{Fore.RESET}"
        separator = "*" * len(header)

        print(separator)
        print(header)
        print(separator)

        result = subprocess.run(
            [path_to_scripts + "ppi_check.bat"],
            env=os.environ,
            timeout=timeout_seconds,
            shell=True,
            capture_output=True,
            text=True,
            check=True
        )

        print(result.stdout)  # Print the standard output of the command
        print(f"{Fore.GREEN}PPI check complete.{Fore.RESET}")

    except subprocess.TimeoutExpired:
        print(f"{Fore.RED}Error: PPI check command timed out after {timeout_seconds} seconds.{Fore.RESET}")
        print(f"{Fore.RED}Please ensure the ignition is on for DCM.{Fore.RESET}")
        print(f"{Fore.YELLOW}PPI check completed with errors.{Fore.RESET}")
    except subprocess.CalledProcessError as e:
        print(f"{Fore.RED}Error: Command '{e.cmd}' failed with return code {e.returncode}.{Fore.RESET}")
        print(f"{Fore.RED}Error message: {e.stderr.strip()}{Fore.RESET}")
        print(f"{Fore.YELLOW}PPI check completed with errors.{Fore.RESET}")
    except Exception as e:
        print(f"{Fore.RED}An unexpected error occurred: {e}{Fore.RESET}")
        print(f"{Fore.YELLOW}PPI check completed with errors.{Fore.RESET}")


def ppi_set():
    try:
        header = f"{Fore.GREEN}Setting PPI Settings{Fore.RESET}"
        separator = "*" * len(header)

        print(separator)
        print(header)
        print(separator)

        result = subprocess.run(
            [path_to_scripts + "ppi_set.bat"],
            env=os.environ,
            timeout=timeout_seconds,
            shell=True,
            capture_output=True,
            text=True,
            check=True
        )

        print(result.stdout)  # Print the standard output of the command
        print(f"{Fore.GREEN}PPI set complete.{Fore.RESET}")

    except subprocess.TimeoutExpired:
        print(f"{Fore.RED}Error: PPI set command timed out after {timeout_seconds} seconds.{Fore.RESET}")
        print(f"{Fore.RED}Please ensure the ignition is on for DCM.{Fore.RESET}")
        print(f"{Fore.YELLOW}PPI set completed with errors.{Fore.RESET}")
    except subprocess.CalledProcessError as e:
        print(f"{Fore.RED}Error: Command '{e.cmd}' failed with return code {e.returncode}.{Fore.RESET}")
        print(f"{Fore.RED}Error message: {e.stderr.strip()}{Fore.RESET}")
        print(f"{Fore.YELLOW}PPI set completed with errors.{Fore.RESET}")
    except Exception as e:
        print(f"{Fore.RED}An unexpected error occurred: {e}{Fore.RESET}")
        print(f"{Fore.YELLOW}PPI set completed with errors.{Fore.RESET}")


def antenna_check():
    try:
        header = f"{Fore.GREEN}Checking Antenna{Fore.RESET}"
        separator = "*" * len(header)

        print(separator)
        print(header)
        print(separator)

        result = subprocess.run(
            [path_to_scripts + "antenna_check.bat"],
            env=os.environ,
            timeout=timeout_seconds,
            shell=True,
            capture_output=True,
            text=True,
            check=True
        )

        print(result.stdout)  # Print the standard output of the command
        print(f"{Fore.GREEN}Antenna check complete.{Fore.RESET}")

    except subprocess.TimeoutExpired:
        print(f"{Fore.RED}Error: Antenna check command timed out after {timeout_seconds} seconds.{Fore.RESET}")
        print(f"{Fore.RED}Please ensure the ignition is on for DCM.{Fore.RESET}")
        print(f"{Fore.YELLOW}Antenna check completed with errors.{Fore.RESET}")
    except subprocess.CalledProcessError as e:
        print(f"{Fore.RED}Error: Command '{e.cmd}' failed with return code {e.returncode}.{Fore.RESET}")
        print(f"{Fore.RED}Error message: {e.stderr.strip()}{Fore.RESET}")
        print(f"{Fore.YELLOW}Antenna check completed with errors.{Fore.RESET}")
    except Exception as e:
        print(f"{Fore.RED}An unexpected error occurred: {e}{Fore.RESET}")
        print(f"{Fore.YELLOW}Antenna check completed with errors.{Fore.RESET}")


def prod_pull_all_logs():
    try:
        header = f"{Fore.GREEN}Pulling All Production Logs{Fore.RESET}"
        separator = "*" * len(header)

        print(separator)
        print(header)
        print(separator)

        result = subprocess.run(
            [path_to_scripts + "prod_pull_all_logs.bat"],
            env=os.environ,
            timeout=timeout_seconds,
            shell=True,
            capture_output=True,
            text=True,
            check=True
        )

        print(result.stdout)  # Print the standard output of the command
        print(f"{Fore.GREEN}Pull all production logs complete.{Fore.RESET}")

    except subprocess.TimeoutExpired:
        print(
            f"{Fore.RED}Error: Pull all production logs command timed out after {timeout_seconds} seconds.{Fore.RESET}")
        print(f"{Fore.RED}Please ensure the ignition is on for DCM.{Fore.RESET}")
        print(f"{Fore.YELLOW}Pull all production logs completed with errors.{Fore.RESET}")
    except subprocess.CalledProcessError as e:
        print(f"{Fore.RED}Error: Command '{e.cmd}' failed with return code {e.returncode}.{Fore.RESET}")
        print(f"{Fore.RED}Error message: {e.stderr.strip()}{Fore.RESET}")
        print(f"{Fore.YELLOW}Pull all prod logs completed with errors.{Fore.RESET}")
    except Exception as e:
        print(f"{Fore.RED}An unexpected error occurred: {e}{Fore.RESET}")
        print(f"{Fore.YELLOW}Pull all production logs completed with errors.{Fore.RESET}")

