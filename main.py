import os
import argparse
from dotenv import load_dotenv
from settings import Settings
import yaml
import subprocess


def export_envs(environment: str = "dev") -> None:
    env_file = f"config/.env.{environment}"
    if not os.path.exists(env_file):
        raise ValueError(f"Environment file {env_file} does not exist")
    load_dotenv(env_file)


def load_secrets() -> None:
    secrets_file = "secrets.yaml"
    if not os.path.exists(secrets_file):
        raise ValueError(f"{secrets_file} does not exist")

    subprocess.run(["sops", "--decrypt", "--in-place", secrets_file], check=True)

    with open(secrets_file) as f:
        secrets = yaml.safe_load(f)

    for key, value in secrets.items():
        os.environ[key] = value


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Load environment variables from .env and secrets.yaml"
    )
    parser.add_argument(
        "--environment",
        type=str,
        default="dev",
        help="The environment to load (dev, test, prod)",
    )
    args = parser.parse_args()

    export_envs(args.environment)
    load_secrets()

    settings = Settings()

    print("APP_NAME:", settings.APP_NAME)
    print("ENVIRONMENT:", settings.ENVIRONMENT)
    print("API_KEY:", os.environ.get("API_KEY"))
    print("DB_PASSWORD:", os.environ.get("DB_PASSWORD"))
