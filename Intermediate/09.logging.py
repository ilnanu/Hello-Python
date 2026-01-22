import logging

logging.basicConfig(filename="sample_log.txt", level=logging.WARNING)
print("Logging started")
logging.debug("Debug Information")
logging.info("info Information")
logging.warning("warning Information")
logging.error("error Information")
logging.critical("critical Information")
print("Logging end")

import logging

logging.basicConfig(filename="sample_log2.txt", level=logging.DEBUG)
print("Logging started")
logging.debug("Debug Information")
logging.info("info Information")
logging.warning("warning Information")
logging.error("error Information")
logging.critical("critical Information")
print("Logging end")

import logging

logging.basicConfig()
print("Logging started")
logging.debug("Debug Information")
logging.info("info Information")
logging.warning("warning Information")
logging.error("error Information")
logging.critical("critical Information")
print("Logging end")

import logging

logging.basicConfig(format="%(levelname)s")
print("Logging started")
logging.debug("Debug Information")
logging.info("info Information")
logging.warning("warning Information")
logging.error("error Information")
logging.critical("critical Information")
print("Logging end")

import logging

logging.basicConfig(format="%(levelname)s:%(message)s")
print("Logging started")
logging.debug("Debug Information")
logging.info("info Information")
logging.warning("warning Information")
logging.error("error Information")
logging.critical("critical Information")
print("Logging end")

import logging

logging.basicConfig(format="%(asctime)s:%(levelname)s:%(message)s")
print("Logging started")
logging.debug("Debug Information")
logging.info("info Information")
logging.warning("warning Information")
logging.error("error Information")
logging.critical("critical Information")
print("Logging end")

import logging

logging.basicConfig(
    format="%(asctime)s:%(levelname)s:%(message)s", datefmt="%d/%m/%Y %I:%M:%S %p"
)
print("Logging started")
logging.debug("Debug Information")
logging.info("info Information")
logging.warning("warning Information")
logging.error("error Information")
logging.critical("critical Information")
print("Logging end")

import logging

logging.basicConfig(
    filename="demo.txt",
    level=logging.INFO,
    format="%(asctime)s:%(levelname)s:%(message)s",
    datefmt="%d/%m/%Y%I:%M:%S %p",
)
logging.info("A new Request Came")
try:
    x = int(input("Enter First Number:"))
    y = int(input("Enter Second Number:"))
    print("The Result:", x / y)
except ZeroDivisionError as msg:
    print("Cannot divide with zero")
    logging.exception(msg)
except ValueError as msg:
    print("Please provide int values only")
    logging.exception(msg)
logging.info("Request Processing Completed")

# Customized Logging in Python
import logging


class LoggerDemoConsole:
    def testLog(self):
        logger = logging.getLogger("demologger")
        logger.setLevel(logging.INFO)
        consoleHandler = logging.StreamHandler()
        consoleHandler.setLevel(logging.INFO)
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s%(levelname)s: %(message)s",
            datefmt="%m/%d/%Y %I:%M:%S%p",
        )
        consoleHandler.setFormatter(formatter)
        logger.addHandler(consoleHandler)
        logger.debug("debug message")
        logger.info("info message")
        logger.warn("warn message")
        logger.error("error message")
        logger.critical("critical message")


demo = LoggerDemoConsole()
demo.testLog()

import logging


class LoggerDemoConsole:
    def testLog(self):
        # logger = logging.getLogger('demologger')
        logger = logging.getLogger(LoggerDemoConsole.__name__)
        logger.setLevel(logging.INFO)
        consoleHandler = logging.StreamHandler()
        consoleHandler.setLevel(logging.INFO)
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s%(levelname)s: %(message)s",
            datefmt="%m/%d/%Y %I:%M:%S%p",
        )
        consoleHandler.setFormatter(formatter)
        logger.addHandler(consoleHandler)
        logger.debug("debug message")
        logger.info("info message")
        logger.warn("warn message")
        logger.error("error message")
        logger.critical("critical message")


demo = LoggerDemoConsole()
demo.testLog()

import logging


class LoggerDemoConsole:
    def testLog(self):
        # logger = logging.getLogger('demologger')
        logger = logging.getLogger(LoggerDemoConsole.__name__)
        logger.setLevel(logging.INFO)
        fileHandler = logging.FileHandler("demo.log", mode="a")
        fileHandler.setLevel(logging.INFO)
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s%(levelname)s: %(message)s",
            datefmt="%m/%d/%Y %I:%M:%S%p",
        )
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        logger.debug("debug message")
        logger.info("info message")
        logger.warn("warn message")
        logger.error("error message")
        logger.critical("critical message")


demo = LoggerDemoConsole()
demo.testLog()
print("Done")
