"""Nebraska: write repo/README.md, LICENSE, jurisdiction.json."""
import json
import sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / 'world-law'))
import us_state_lib as L

c = json.loads((HERE / 'corpus.json').read_text('utf-8'))
n = {a['slug']: len(a['versions'][0]['units']) for a in c['acts']}
rows = "| `constitution/` | Constitution of the State of Nebraska (%d provisions) | 1 | Oldest version available: certified 2 December 2024 |\n" % n['constitution']
for a in c['acts'][1:]:
    rows += "| `%s/` | %s (%d sections) | 1 | Oldest version available |\n" % (a['slug'], a['title'], n[a['slug']])
stat_note = ('' if len(c['acts']) > 1 else
             "That is all the law this repository holds today. **The Nebraska Revised Statutes are not in it**: the Legislature's site could not be reached from the machine that built this, and no readable archive copy of the Revisor's chapter files was found.\n")

README = f"""# Nebraska: law history in git

The Constitution of Nebraska as a git repository: one file per section, one paragraph per line, so `git blame` works line by line. It follows the shared design of [lexifina/global-law](https://github.com/lexifina/global-law).

**What is in it now**

| Folder | Act | Versions | History |
| --- | --- | ---: | --- |
{rows}
{stat_note}
## Where the text comes from

The Constitution is the Legislature's own PDF, "Certified by Secretary of State's Office and Distributed by Clerk of the Legislature's Office, Lincoln, Nebraska, December 2, 2024" (<https://nebraskalegislature.gov/FloorDocs/Current/PDF/Constitution/constitution.pdf>), whose cover letter from the Revisor of Statutes says it includes Initiative Measure No. 434, adopted on 4 November 2024. The Legislature's server does not accept connections from the machine that built this repository, so the bytes are the Internet Archive's copy of that file. The Legislature's terms could not be read.

## Dates

- The single version is dated **2 December 2024**, the certification date on the PDF's cover. It is the oldest version available.
- The first commit is credited to the publisher as "oldest version available".

## What it does not show

- Any history before that certification, and any amendment after it.
- The "Source:" line under each section (which names the amending measure), running heads and page numbers, and the sections headed "Repealed" or "Obsolete", are left out.
- Paragraph breaks are rebuilt from the PDF's line layout, so a break can be missing or extra in a long section.
- Nothing here is an official publication or legal advice.

## How it is checked

- Every unit is read back from git on its day and compared with the corpus (`tools/check_repo.py`; results in `REPRODUCE.md`).
- The source is identified by its sha256, in `data/versions.json`.
"""

LICENSE = """The legal text is the Constitution of the State of Nebraska as certified by the Secretary of State and distributed by the Clerk of the
Legislature on 2 December 2024, published by the Nebraska Legislature at
https://nebraskalegislature.gov/FloorDocs/Current/PDF/Constitution/constitution.pdf. The bytes were read from the Internet Archive's copy of that file.

The Legislature's terms of use could not be read from here (its server does not accept connections from the machine that built this
repository), and the PDF carries no reuse notice. A state constitution is an official legal text and an edict of government that
copyright does not protect (Georgia v. Public.Resource.Org, Inc., 590 U.S. 255 (2020)). It is republished here, unaltered except for the
changes below, with credit to the Nebraska Legislature as its publisher.

Changes made by Lexifina: one Markdown file per section, one paragraph per line, normalised spaces, quotation marks and hyphens;
the Source lines, running heads, page numbers and repealed or obsolete sections left out. The wording of the law was not changed.
The Nebraska Legislature does not endorse this repository.

Lexifina's own contributions (the arrangement of the history, the commit messages, the tables and the tools) are dedicated to the
public domain under CC0 1.0 Universal: https://creativecommons.org/publicdomain/zero/1.0/legalcode
"""

L.write_repo(HERE, README, LICENSE, {
    'path': 'us-ne', 'code': 'NE', 'name': 'Nebraska', 'level': 'state',
    'repo': 'https://github.com/lexifina/united-states-nebraska-law',
    'build': 'built: Constitution only, one version (certified 2024-12-02); statutes not obtained',
    'register_date': '2026-10-30'})
