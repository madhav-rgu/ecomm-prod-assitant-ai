from logger.custom_logger import CustomLogger

# Create a single shared logger instance
GLOBAL_LOGGER = CustomLogger().get_logger("prod_assistant")