#!/usr/bin/env python3
# lib/debug.py

from models.__init__ import CONN, CURSOR
from models.artist import Artist
from models.work import Work
import ipdb

def reset_database():
    Artist.drop_table()
    Work.drop_table()
    Artist.create_table()
    Work.create_table()

    Artist.create("Van Gogh", "Dutch", "Post-Impressionism")
    Artist.create("Claude Monet", "French", "Impressionism")
    Artist.create("Katsushika Hokusai", "Japanese", "Ukiyo-e")
    # Work.create("Starry Night", 1889, "Oil on canvas", 1)


reset_database()
ipdb.set_trace()
