"""
JMdict parser module for handling Japanese-English dictionary entries.
Provides functionality to extract and format random entries from the JMdict XML file.
"""
from lxml import etree
import random

def get_random_jmdict_entry(filepath='../JMdict_e'):
    tree = etree.parse(filepath)
    entries = tree.xpath('//entry')
    entry = random.choice(entries)

    # Extract kanji (keb), reading (reb), glosses
    kebs = entry.xpath('./k_ele/keb/text()')
    rebs = entry.xpath('./r_ele/reb/text()')
    glosses = entry.xpath('./sense/gloss/text()')

    return {
        'kanji': kebs if kebs else None,
        'reading': rebs,
        'meanings': glosses
    }


def format_jmdict_entry(entry):
    kanji = ", ".join(entry['kanji']) if entry['kanji'] else "(no kanji)"
    reading = ", ".join(entry['reading'])
    meanings = ", ".join(entry['meanings'])

    result = f"Kanji: {kanji}\n"
    result += f"Reading: {reading}\n"
    result += f"Meanings: {meanings}"

    return result
