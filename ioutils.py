import signal
import sys

from logging import print_sigint_message

def prime_sigint_handler():
    def signal_handler(sig, frame):
        print_sigint_message()
        sys.exit(0)

    signal.signal(signal.SIGINT, signal_handler)