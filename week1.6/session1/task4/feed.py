# Week 1.6, Session 1: Task 4

import csv
from urllib.request import urlopen

VALID_LEVELS = {"all", "1.0", "2.5", "4.5", "significant"}
VALID_PERIODS = {"hour", "day", "week", "month"}

URL = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/{}_{}.csv"


class QuakeFeed:
    """
    A specific USGS earthquake data feed.

    The feed is specified by its significance level and time period.
    """

    def __init__(self, level, period):
        """
        Creates a QuakeFeed for the given level & period.
        """
        if level not in VALID_LEVELS:
            raise ValueError(f"invalid level: must be one of {VALID_LEVELS}")

        if period not in VALID_PERIODS:
            raise ValueError(f"invalid period: must be one of {VALID_PERIODS}")

        self.level = level
        self.period = period
        self.url = URL.format(level, period)

    def __str__(self):
        """
        Returns a string representation of this feed (the last part of its URL).
        """
        index = self.url.rindex("/") + 1
        return self.url[index:]

    def reader(self):
        """
        Returns a DictReader that can be used to access data from this feed.
        """
        with urlopen(self.url) as source:
            lines = [line.decode() for line in source]
        return csv.DictReader(lines)
