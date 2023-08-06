#!/usr/bin/env python3
import os
from jlclient import jarvisclient
from jlclient.jarvisclient import *
from dotenv import load_dotenv

# AI START
import argparse

# Create the parser
parser = argparse.ArgumentParser(description="Create a new instance")

# Add the arguments
parser.add_argument(
    "--gpu_type",
    type=str,
    help="The type of NVIDIA GPU",
    choices=["RTX5000", "A100"],
    default="A100",
)
parser.add_argument(
    "--num_gpus",
    choices=[1, 2, 4, 8],
    type=int,
    help="The number of GPUs",
    default=1,
)
parser.add_argument(
    "--hdd", type=int, help="The hard disk drive capacity (multiples of 10)", default=50
)
parser.add_argument("--name", help="The name of the instance", default="Dev")
parser.add_argument(
    "--is_spot",
    help="Do not reserve instance",
    default=True,
    action="store_false",
)
# This argument lets the user choose to destroy the instance
parser.add_argument(
    "--destroy",
    help="Destroy the instance rather than create it",
    action="store_true",
)
# This argument lets the user input a file path for a setup script
parser.add_argument(
    "--script_path",
    type=str,
    help="The path to the setup script",
    default="utils/LatentBlending.sh",
)

args = parser.parse_args()
# AI END

load_dotenv()  # take environment variables from .env.

jarvisclient.token = os.environ.get(f"JARVISLABS_API_KEY")
jarvisclient.user_id = os.environ.get(f"JARVISLABS_USER")

if jarvisclient.token == None or jarvisclient.user_id == None:
    print("Please set JARVISLABS_API_KEY and JARVISLABS_USER environment variables!")
    exit()

if __name__ == "__main__":
    scripts = User.get_script()
    script_id = ""
    script_name = args.script_path.split("utils/")[1].split(".sh")[0]

    if scripts["success"] != False:
        for script in scripts["script_meta"]:
            if script["script_name"] == script_name:
                script_id = script["script_id"]
                print("Script already exists!")
                break
    else:
        print("Creating script...")
        script_id = User.add_script(
            script_path=args.script_path,
            script_name=script_name,
        )

    # Lists instances
    instances = User.get_instances()
    for instance in instances:
        if instance.name == args.name:
            print(f"Status: {instance.status}")
            if args.destroy == True:
                print(f"Destroying {args.name} instance...")
                instance.destroy()
                if User.get_instance(instance.machine_id) != None:
                    print(f"Unable to destroy {args.name}!")
                else:
                    print(f"Destroyed {args.name}!")

                exit()

            if instance.status == "Running":
                print(f"Connect to {instance.name} with:\n\n\t{instance.ssh_str}\n")
                exit()

            if instance.status == "Paused":
                print(f"Resuming {instance.name} instance...")
                instance.resume()
                exit()

    if args.destroy == True:
        exit()

    # Creates a new colmap instance
    print(
        f"Creating {args.name} instance with {args.num_gpus} {args.gpu_type} GPUs and {args.hdd}GB of storage..."
    )
    # AI START
    instance = Instance.create(
        gpu_type=args.gpu_type,
        num_gpus=args.num_gpus,
        hdd=args.hdd,
        name=args.name,
        script_id=script_id,
        is_reserved=(not args.is_spot),
    )
    # AI END

    instances = User.get_instances()
    for instance in instances:
        if instance.name == args.name:
            print(f"Instance {instance.name} created!")
            if instance.status == "Running":
                print(f"Connect to {instance.name} with:\n\n\t{instance.ssh_str}\n")
                exit()
            elif instance.status == "Starting":
                print(f"Waiting for {instance.name} to start...")
                exit()

    print(f"Unable to start {args.name} instance!")
