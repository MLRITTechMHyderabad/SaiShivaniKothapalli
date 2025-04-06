import re
import logging

logger = logging.getLogger(__name__)

class LaunchAuthorizationSystem:
    """Handles nuclear launch authorization validation."""
    AUTH_PATTERN = r'^AUTH-[A-Z0-9]+-\d{4}-SECURE$'

    @staticmethod
    def validate_code(code):
        if re.match(LaunchAuthorizationSystem.AUTH_PATTERN, code):
            logger.info("Authorization Code Validated Successfully!")
            return True
        else:
            logger.warning("Invalid Authorization Code!")
            return False
