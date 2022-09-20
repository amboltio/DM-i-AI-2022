from pydantic import BaseSettings
from argparse import ArgumentParser
from utilities.singleton import singleton
from dotenv import load_dotenv

@singleton
class Environment(BaseSettings):
    ENVIRONMENT: str = 'production'

    HOST_IP: str
    CONTAINER_PORT: int

def load_env():
    # Let the script caller define the .env file to use, e.g.:  python api.py --env .prod.env
    parser = ArgumentParser()
    parser.add_argument('-e', '--env', default='.env',
                        help='Sets the environment file')

    args = parser.parse_args()
    load_dotenv(args.env)