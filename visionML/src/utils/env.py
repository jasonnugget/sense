import os
from pathlib import Path

from dotenv import load_dotenv

REQUIRED_VARS = ["DATA_DIR"]
OPTIONAL_DEFAULTS = {
    "RUNS_DIR": "./runs",
    "PROJECT_NAME": "visionml",
    "DEVICE": "0",
}


def load_env(env_file: str | None = ".env") -> dict:
    """Load .env file and return env mapping with defaults applied."""
    if env_file:
        load_dotenv(env_file)

    missing = [var for var in REQUIRED_VARS if not os.getenv(var)]
    if missing:
        raise EnvironmentError(f"Missing required env var(s): {', '.join(missing)}")

    env = {}
    env.update(OPTIONAL_DEFAULTS)
    for key in REQUIRED_VARS + list(OPTIONAL_DEFAULTS.keys()) + ["WANDB_API_KEY"]:
        if os.getenv(key) is not None:
            env[key] = os.getenv(key)

    # Normalize paths
    env["DATA_DIR"] = str(Path(env["DATA_DIR"]).expanduser().resolve())
    env["RUNS_DIR"] = str(Path(env["RUNS_DIR"]).expanduser())
    return env
