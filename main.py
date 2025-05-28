import zconfig
import ai
import log
import sys
from prompt_toolkit import prompt




def deal(u)->bool:
    text = prompt("Q:")
    con = u.post(text)
    print(f"A:{con.strip()}")


def do_it(config:zconfig.ZConfig):
    running = True
    u = ai.ZAi(config.api_url, config.api_key, config.ai_model, config.log_file)

    
    while running:
        deal(u)


if __name__ == "__main__":
    config = zconfig.ZConfig()
    logger = log.Log(config.log_file, __name__)
    try:
        do_it(config)
    except Exception as e:
        logger.error(f"{e}")
