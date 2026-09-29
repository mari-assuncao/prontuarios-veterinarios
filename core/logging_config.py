import logging
import logging.config
from pathlib import Path

import yaml

#trabalhando com logs no sistama

BASE_DIR = Path(__file__).resolve().parent.parent
LOGGING_FILE = BASE_DIR / "config.yaml"


with open(LOGGING_FILE, "r", encoding="utf-8") as file:
    config = yaml.safe_load(file)


config["handlers"]["file"]["filename"] = str(BASE_DIR / "app.log")


logging.config.dictConfig(config)

logger = logging.getLogger("cofre-digital-veterinario-main")
logger.info("sistema de logging init")


