"""
JMdict parser module for handling Japanese-English dictionary entries.
Provides functionality to extract and format random entries from the JMdict XML file.
"""
from lxml import etree
import random
import logging


logger = logging.getLogger(__name__)

def get_random_jmdict_entry(filepath='../JMdict_e'):
    """Get a random entry from the JMdict XML file."""
    logger.info("Getting random JMdict entry.")
    tree = etree.parse(filepath)
    entries = tree.xpath('//entry')
    entry = random.choice(entries)
    logger.info("Successfully got random JMdict entry.")

    # Extract kanji (keb), reading (reb), glosses
    logger.info("Extracting kanji, reading, and glosses from JMdict entry.")
    kebs = entry.xpath('./k_ele/keb/text()')
    rebs = entry.xpath('./r_ele/reb/text()')
    glosses = entry.xpath('./sense/gloss/text()')
    logger.info("Successfully extracted kanji, reading, and glosses from JMdict entry.")

    return {
        'kanji': kebs if kebs else None,
        'reading': rebs,
        'meanings': glosses
    }


def format_jmdict_entry(entry):
    """Format a JMdict entry into a string."""
    logger.info("Formatting JMdict entry.")
    kanji = ", ".join(entry['kanji']) if entry['kanji'] else "(no kanji)"
    reading = ", ".join(entry['reading'])
    meanings = ", ".join(entry['meanings'])

    result = f"Kanji: {kanji}\n"
    result += f"Reading: {reading}\n"
    result += f"Meanings: {meanings}"
    logger.info("Successfully formatted JMdict entry.")

    return result
