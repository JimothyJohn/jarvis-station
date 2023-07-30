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
    default="RTX5000",
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
parser.add_argument("--name", type=str, help="The name of the instance", default="Dev")
parser.add_argument(
    "--is_reserved", type=bool, help="Reserve instance or spot instance", default=False
)
# This argument lets the user choose to destroy the instance
parser.add_argument(
    "--destroy",
    type=bool,
    help="Destroy the instance rather than create it",
    default=False,
)
# This argument lets the user input a file path for a setup script
parser.add_argument(
    "--script",
    type=str,
    help="The path to the setup script",
    default="utils/LatentBlending.sh",
)

args = parser.parse_args()
# AI END

load_dotenv()  # take environment variables from .env.

jarvisclient.token = os.environ.get(f"JARVISLABS_API_KEY")
jarvisclient.user_id = os.environ.get(f"JARVISLABS_USER")

if __name__ == "__main__":
    print(f"{User.get_script()}")
    script_id = ""
    if User.get_script()["success"] != False:
        for script in User.get_script()["script_meta"]:
            if script["script_name"] == args.script:
                script_id = script["script_id"]
                print("Script already exists!")
                break
    else:
        print("Creating script...")
        script_id = User.add_script(
            script_path=args.script,
            script_name=args.script.split("utils/")[1].split(".sh")[0],
        )

    # print(f"{User.get_script()['script_meta'][0]}")
    # Lists instances
    instances = User.get_instances()
    for instance in instances:
        if instance.name == args.name:
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
        is_reserved=args.is_reserved,
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
