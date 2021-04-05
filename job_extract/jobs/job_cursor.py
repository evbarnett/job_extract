from typing import Optional

from .job_item import JobItem


class JobCursor:

    def __init__(self):
        pass

    def get_next(self) -> Optional[JobItem]:
        """
        """
        raise NotImplementedError
