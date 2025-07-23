import subprocess
import os
from colorama import init, Fore
from flask_socketio import SocketIO

from WebsocketHelper.MessageEmitter import MessageEmitter
from WebsocketHelper.MessageSender import MessageSender

# Initialize colorama
init()

path_to_scripts = "<PATH TO SCRIPTS>"
timeout_seconds = 3
os.environ["ADB_PATH"] = "<PATH TO ADB>"
os.environ["DPATH"] = "<PATH TO LOGS>"

class AdbToolsV2:
    def __init__(self, socketio: SocketIO):
        self.emitter = MessageEmitter(socketio)  # Pass the socketio instance
        self.sender = MessageSender(self.emitter)

    # -------------------------
    # DCM version check
    # -------------------------
    def version_check(self):
        """ Checks the DCM version"""
        try:
            header = "DCM Version Check"
            separator = "*" * len(header)

            self.sender.send_message(separator)
            self.sender.send_green_message(header)
            self.sender.send_message(separator)

            result = subprocess.run(
                [path_to_scripts + "version_check.bat"],
                env=os.environ,
                timeout=timeout_seconds,
                shell=True,
                capture_output=True,
                text=True,
                check=True
            )

            self.sender.send_message(result.stdout)
            self.sender.send_green_message("Version check completed successfully")

        except subprocess.TimeoutExpired:
            self.sender.send_error(f"Error: Version check command timed out after {timeout_seconds} seconds.")
            self.sender.send_error(f"Please ensure the ignition is on for DCM.")
            self.sender.send_warning(f"Version check completed with errors.")
        except subprocess.CalledProcessError as e:
            self.sender.send_error(f"Error: Command '{e.cmd}' failed with return code {e.returncode}.")
            self.sender.send_error(f"Error message: {e.stderr.strip()}")
            self.sender.send_warning(f"Version check completed with errors.")
        except Exception as e:
            self.sender.send_error(f"An unexpected error occurred: {e}")
            self.sender.send_warning(f"Version check completed with errors.")


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

