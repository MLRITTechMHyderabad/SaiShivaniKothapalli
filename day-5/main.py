import json
import logging
from authorization import LaunchAuthorizationSystem

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class Warhead:
    def __init__(self, warhead_id, type, yield_kt):
        self.warhead_id = warhead_id
        self.type = type
        self.yield_kt = yield_kt

    def get_info(self):
        return f"Warhead {self.warhead_id}: Type {self.type}, Yield {self.yield_kt}kt"

class Submarine:
    MAX_ATTEMPTS = 3

    def __init__(self, name, warhead_data):
        self.name = name
        self.warheads = [Warhead(**w) for w in warhead_data]
        self.failed_attempts = 0

    def authorize_launch(self, code):
        logger.info(f"Launch request received for {self.name}.")

        if LaunchAuthorizationSystem.validate_code(code):
            self.failed_attempts = 0
            logger.info(f"Launch authorized for {self.name}. Preparing to launch SLBM...")
            self.launch_missile()
        else:
            self.failed_attempts += 1
            logger.error("Launch Authorization Failed! Access Denied.")

            if self.failed_attempts >= Submarine.MAX_ATTEMPTS:
                logger.critical("SELF-DESTRUCT PROTOCOL ACTIVATED")
                self.self_destruct()

    def launch_missile(self):
        if self.warheads:
            warhead = self.warheads[0]
            logger.info(f"Missile launched carrying {warhead.get_info()}!")
        else:
            logger.warning("No warheads loaded.")

    def self_destruct(self):
        logger.critical(f"{self.name} has self-destructed due to multiple unauthorized attempts!")

warhead_json = '''
[
    {"warhead_id": "W001", "type": "Thermonuclear", "yield_kt": 1000},
    {"warhead_id": "W002", "type": "Tactical", "yield_kt": 300}
]
'''
warhead_data = json.loads(warhead_json)
sub = Submarine("INS Arihant", warhead_data)
sub.authorize_launch("WRONG-CODE-001")
sub.authorize_launch("INVALID-ATTEMPT")
sub.authorize_launch("AUTH-XYZ123-4567-SECURE")
