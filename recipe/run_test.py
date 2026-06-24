import subprocess
import sys


def main():
    subprocess.check_call(["waf", "--help"])
    subprocess.check_call(["waf", "configure"])
    subprocess.check_call(["waf", "build"])


if __name__ == "__main__":
    main()
