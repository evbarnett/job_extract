class IndeedCursor(JobCursor):

    def __init__(self, title: str, location: str, radius: int = 25):
        base_url = "https://www.indeed.com/jobs?"
        self._title = title
        self._location = location
        title_esc = ul.quote(self._title, safe='')
        location_esc = ul.quote(self._location, safe='')
        req_url = base_url + "q={}&l={}".format(title_esc, location_esc)
        # TODO
