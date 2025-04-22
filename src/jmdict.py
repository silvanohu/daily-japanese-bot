from lxml import etree
import random

tree = etree.parse('../JMdict_e')
entries = tree.xpath('//entry')

random_entries = random.sample(entries, 5)

for entry in random_entries:
    kebs = entry.xpath('./k_ele/keb/text()')
    rebs = entry.xpath('./r_ele/reb/text()')
    glosses = entry.xpath('./sense/gloss/text()')

    print("Kanji:", ", ".join(kebs) if kebs else "(no kanji)")
    print("Reading:", ", ".join(rebs))
    print("Meaning(s):", ", ".join(glosses))
    print("-" * 40)
