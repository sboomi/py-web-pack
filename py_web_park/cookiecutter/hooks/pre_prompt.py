import docker
from loguru import logger
import subprocess


def check_docker():
    try:
        docker.from_env()
    except docker.errors.DockerException as e:
        logger.error(f"Docker is neither installed nor activated: {e}")


def check_pyenv():
    try:
        subprocess.run(["pyenv", "--version"], shell=True, check=True)
    except subprocess.CalledProcessError:
        logger.error("pyenv not found. Install pyenv.")


if __name__ == "__main__":
    check_docker()
    check_pyenv()
