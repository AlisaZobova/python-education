"""Context manager for working with files"""
from loggers import logger


class Open:
    """Context manager class"""
    def __init__(self, file_name, method):
        try:
            self.file = open(file_name, method)
            self.copy_file = self.file
        except FileNotFoundError:
            logger.error("No such file or directory!")
        except ValueError:
            logger.error("Incorrect method!")

    def __enter__(self):
        try:
            return self.copy_file
        except AttributeError:
            logger.error("Something went wrong during initialization!")

    def __exit__(self, exc_type, exc_value, exc_traceback):
        try:
            if exc_type is None:
                self.file = self.copy_file
                self.file.close()
                logger.info("The file was processed successfully. "
                            "The file has been closed.")
            else:
                logger.error("Exception: %s.", exc_value)
        except AttributeError:
            logger.error("Something went wrong during initialization!")

        return True


logger.info("First example:")
with Open('test.txt', 'w') as file:
    file.write("Nick")
    file.read()

logger.info("Second example:")
with Open('test.txt', 'r') as file:
    file.write("Nick")
    file.read()

logger.info("Third example:")
with Open('test.txt', 'j') as file:
    file.write("Nick")

logger.info("Fourth example:")
with Open('test.txt', 'w') as file:
    file.write("Nick")

logger.info("Fifth example:")
with Open('test.txt', 'r') as file:
    logger.info(file.read())

logger.info("Sixth example:")
with Open('test1.txt', 'r') as file:
    logger.info(file.read())
