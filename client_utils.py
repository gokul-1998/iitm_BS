import hashlib
import platform
import uuid


def get_machine_id():
    # Collect machine-specific details
    node = uuid.getnode()  # MAC-based node ID
    system_info = platform.uname()
    unique_data = f"{node}-{system_info.system}-{system_info.node}-{system_info.release}-{system_info.version}"
    # Create a hash to form a unique identifier
    machine_id = hashlib.sha256(unique_data.encode()).hexdigest()
    return machine_id
