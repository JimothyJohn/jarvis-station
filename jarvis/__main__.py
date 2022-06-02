import os
import argparse
from jlclient import jarvisclient
from jlclient.jarvisclient import *

TOKEN = os.environ.get(f"JARVIS_TOKEN")
USER = os.environ.get(f"JARVIS_USER")

jarvisclient.token = TOKEN
jarvisclient.user_id = USER

if __name__ == "__main__":
    # Lists instances that are in Running, Paused, Resuming and Pausing states.
    User.get_instances()

    """
    # Creates a new instance
    instance = Instance.create(
        gpu_type='RTX5000',
        num_gpus=1,
        hdd=20,
        framework_id=0,
        name='Dev',
        script_id=1,
        is_reserved=False
    )
    """
