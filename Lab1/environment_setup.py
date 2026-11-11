
"""
Experiment 1: AI Development Environment Setup
Author: Dev Jain
Roll No: IC2K23-21
"""

import sys
import platform
import importlib.util


def display_system_info():
    """Print details about the current system."""

    print("AI DEVELOPMENT ENVIRONMENT")
    print("=" * 40)

    version = sys.version.split()[0]
    os_name = platform.system()
    architecture = platform.machine()

    print("Python Version:", version)
    print("Operating System:", os_name)
    print("System Architecture:", architecture)


def verify_packages():
    """Verify whether required AI packages are available."""

    packages = (
        "numpy",
        "pandas",
        "matplotlib",
        "sklearn",
        "jupyter",
        "torch"
    )

    print("\nCHECKING AI LIBRARIES")
    print("=" * 40)

    for package in packages:

        status = importlib.util.find_spec(package)

        if status is not None:
            print(f"{package} : Installed")
        else:
            print(f"{package} : Not Installed")


def main():

    display_system_info()
    verify_packages()

    print("\nAI Environment Setup Verification Completed!")


if __name__ == "__main__":
    main()
