""" Creates Screenshots of a website in a headless fashion
"""

# Imports
import argparse
import os
from selenium import webdriver

# Configurations
options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--disable-gpu")

parser = argparse.ArgumentParser(
    description="Script to create a headless screenshot of a webpage"
)
parser.add_argument(
    "--page", type=str, required=True, help="URL of the desired webpage"
)
parser.add_argument(
    "--shot_name", type=str, required=True, help="Name you want for the screenshot"
)
parser.add_argument(
    "--path",
    type=str,
    default="../tmp",
    help="Path where to store the screenshots -> Default is ../tmp",
)
args = parser.parse_args()


# Methods
def directory_check():
    """Method that makes sure that path does exist"""
    if args.path == "../tmp":
        if not os.path.exists(args.path):
            os.makedirs(args.path)
            print("Temporary directory created, since it was missing")
    else:
        if not os.path.exists(args.path):
            raise FileNotFoundError(
                f"The provided args.path {args.path} does not exist."
            )


def take_the_shot():
    """Takes the screenshot of the requested page"""
    browser = webdriver.Chrome(options=options)
    try:
        browser.get(args.page)
        browser.save_screenshot(f"{args.path}/{args.shot_name}.png")
        print("Shot was taken successfully")
    finally:
        browser.quit()


# Main Method
if __name__ == "__main__":
    directory_check()
    take_the_shot()
