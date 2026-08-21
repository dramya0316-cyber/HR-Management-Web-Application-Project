import logging
import config


class LogGen:

    @staticmethod
    def loggen():
        logging.basicConfig(filename=config.LOGS_DIR / "automation.log",
                            format="%(asctime)s|%(levelname)s|%(filename)s:%(lineno)d|%(message)s",
                            datefmt="%d-%m-%Y %H:%M:%S",
                            filemode='w',
                            level=logging.INFO,
                            force=True)

        logger = logging.getLogger("guvi_project")
        logger.setLevel(logging.INFO)
        return logger