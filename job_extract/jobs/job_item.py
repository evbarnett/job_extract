import datetime


class JobItem:

    def __init__(self,
                 title: str,
                 company: str,
                 description_raw: str,
                 date_posted: datetime.date,
                 is_ad: bool = False
                 ):
        self.title = title
        self.company = company
        self.description_raw = description_raw
        self.date_posted = date_posted
        self.is_ad = is_ad
