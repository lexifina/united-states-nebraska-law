# How this repository was made (Nebraska)

This file is written by the build on 2026-10-30, the day the source data was retrieved.

## Sources

| Source | Address | Retrieved | Licence |
| --- | --- | --- | --- |
| Constitution of the State of Nebraska (Nebraska Legislature PDF, archive.org copy) | <https://nebraskalegislature.gov/FloorDocs/Current/PDF/Constitution/constitution.pdf> | 2026-10-30 | no reuse terms could be read; official text of a state constitution |
| Nebraska Legislature | <https://nebraskalegislature.gov/laws/browse-chapters.php?chapter=21> | 2026-10-30 | Statute text is not copyrightable in the United States (Georgia v. Public.Resource.Org, 590 U.S. 255 (2020)). The Revisor's annotations and cross references on the pages are not used. |
| Nebraska Legislature | <https://nebraskalegislature.gov/laws/browse-chapters.php?chapter=25> | 2026-10-30 | Statute text is not copyrightable in the United States (Georgia v. Public.Resource.Org, 590 U.S. 255 (2020)). The Revisor's annotations and cross references on the pages are not used. |
| Nebraska Legislature | <https://nebraskalegislature.gov/laws/browse-chapters.php?chapter=28> | 2026-10-30 | Statute text is not copyrightable in the United States (Georgia v. Public.Resource.Org, 590 U.S. 255 (2020)). The Revisor's annotations and cross references on the pages are not used. |
| Nebraska Legislature | <https://nebraskalegislature.gov/laws/browse-chapters.php?chapter=76> | 2026-10-30 | Statute text is not copyrightable in the United States (Georgia v. Public.Resource.Org, 590 U.S. 255 (2020)). The Revisor's annotations and cross references on the pages are not used. |

Every word of law in this repository comes from these sources. Lexifina reads them and records each act's dated versions, and the laws that made each change, in one corpus file. This repository is built from that file.

## What is in it

| Act | Title | Versions | Span |
| --- | --- | ---: | --- |
| `constitution` | Constitution of the State of Nebraska (1875, as amended) | 1 | 2024-12-02 to 2024-12-02 |
| `chapter-0021` | Nebraska Revised Statutes, Chapter 21: Corporations and other companies | 1 | 2026-10-29 to 2026-10-29 |
| `chapter-0025` | Nebraska Revised Statutes, Chapter 25: Courts; civil procedure | 1 | 2026-10-28 to 2026-10-28 |
| `chapter-0028` | Nebraska Revised Statutes, Chapter 28: Crimes and punishments | 1 | 2026-10-16 to 2026-10-16 |
| `chapter-0076` | Nebraska Revised Statutes, Chapter 76: Real property | 1 | 2026-10-28 to 2026-10-28 |

The build made 5 commits:

| Commits | Kind |
| ---: | --- |
| 5 | first version of an act |
| 0 | one law on its in-force day |
| 0 | changes no amendment note explains, credited to the publisher |

Other counts:
- 0 commits on the branch `future`: laws not yet in force on 2026-10-30.
- 0 commits dated 1 January 1970: in force before 1970, with the real day in their `In-force` trailer.
- 0 laws in the record.
- 5 tags.

## Dates

Each commit is dated at noon (America/Chicago) on the day the change took effect. The other dates, enacted and published, are trailers.

When a law gives no date of its own, the default rule applies: Neb. Const. art. III, sec. 27: an act takes effect three calendar months after the Legislature adjourns, unless passed with an emergency clause. https://nebraskalegislature.gov/FloorDocs/Current/PDF/Constitution/constitution.pdf

## How the history is built

`tools/build.py` turns the corpus into this history in one pass: one commit per law, on the day it took effect. The same corpus always gives the same commit hashes. `tools/check_repo.py` reads every version back from git and compares it with the corpus. `tools/on.py` shows the law as it stood on any date. The corpus format is described in `tools/SCHEMA.md`.

- Corpus: sha256 `a9128fc6736dc496e0965aa8c67772058338785fdea3c5b6c26460edeb4cb2da` (5439377 bytes).
- Builder blob hashes (`git hash-object`): `build.py` `a97ff7ea62c3c7595c5668a297d533da0b74373c`, `check.py` `3e59cb6f05eccb94a9ec14431a7f6781221e83ef`, `on.py` `644a6c0857fbcc72562032b58d57aa113fee0641`.
- Python 3.12.10; git version 2.46.0.windows.1.

## Checks

5 versions of 5 acts read back from git on the day each took effect and on the day before: 0 mismatches. Trailers: 0 commits whose trailers git cannot parse. Health: 0 merge commits on main, 0 commit dates that go backwards, 0 commits dated after the build.

No second build of this corpus has been compared yet.

## Decisions made by hand

- The bytes are archive.org's copies of the Legislature's own PDF files, read through the shared archive client; the archive URL is recorded as each version's source_url.
- The Constitution is the PDF "Certified by Secretary of State's Office and Distributed by Clerk of the Legislature's Office, Lincoln, Nebraska, December 2, 2024". That day is the version date. It includes Initiative Measure No. 434 adopted at the 4 November 2024 general election.
- The Source lines under each section (the amendment history), running heads and page numbers are left out. Sections headed "Repealed" or "Obsolete" are left out. Paragraph breaks are rebuilt from the PDF's line layout: a break before an (a)- or (1)-style marker and after a short line ending in a full stop.
- The Nebraska Revised Statutes were not obtained. This build holds the Constitution only.
- Nebraska Revised Statutes chapter 21: one unit per section named in the chapter list, including sections shown as repealed or transferred: the number and catchline, the text (a table row per line), and the Source line of session laws. The cross references and annotations (case notes) printed after the Source line are left out.
- Sections were read from different web captures (2025-02-10 to 2026-10-16), so the single version is dated 2026-10-29, the newest capture day (or, if later, the day of the newest law already in the repository, or the day after it when the chapter would otherwise sort before it, so the history only grows); a section amended between its capture and that day would show its older text.
- Repealed and transferred sections whose page no archive holds (1: 21-29,128) are taken from the chapter list, whose line for such a section is the whole text of its page.
- Missing from chapter 21: sections 21-289, 21-290, 21-2,134, 21-2,137, 21-2,139. they will be added as a later version when a copy can be read.
- Nebraska Revised Statutes chapter 25: one unit per section named in the chapter list, including sections shown as repealed or transferred: the number and catchline, the text (a table row per line), and the Source line of session laws. The cross references and annotations (case notes) printed after the Source line are left out.
- Sections were read from different web captures (2025-02-12 to 2026-10-28), so the single version is dated 2026-10-28, the newest capture day (or, if later, the day of the newest law already in the repository, or the day after it when the chapter would otherwise sort before it, so the history only grows); a section amended between its capture and that day would show its older text.
- Repealed and transferred sections whose page no archive holds (3: 25-1267.06, 25-1267.42, 25-2120) are taken from the chapter list, whose line for such a section is the whole text of its page.
- Missing from chapter 25: sections 25-542, 25-2133, 25-2134, 25-21,157, 25-21,287, 25-21,291, 25-21,304, 25-21,305, 25-21,306, 25-3108, 25-3109. they will be added as a later version when a copy can be read.
- Nebraska Revised Statutes chapter 28: one unit per section named in the chapter list, including sections shown as repealed or transferred: the number and catchline, the text (a table row per line), and the Source line of session laws. The cross references and annotations (case notes) printed after the Source line are left out.
- Sections were read from different web captures (2024-11-07 to 2026-10-16), so the single version is dated 2026-10-16, the newest capture day (or, if later, the day of the newest law already in the repository, or the day after it when the chapter would otherwise sort before it, so the history only grows); a section amended between its capture and that day would show its older text.
- Repealed and transferred sections whose page no archive holds (23: 28-426, 28-448, 28-1432, 28-1433, 28-1434, 28-1435, 28-1437, 28-1438.01, 28-1439, 28-1441, 28-1442, 28-1443, 28-1445, 28-1451, 28-1452, 28-1454, 28-1455, 28-1456, 28-1457, 28-1458, 28-1460, 28-1461, 28-1462) are taken from the chapter list, whose line for such a section is the whole text of its page.
- Missing from chapter 28: sections 28-433, 28-434, 28-435, 28-435.01, 28-449, 28-450, 28-627.04, 28-907.01, 28-1903. they will be added as a later version when a copy can be read.
- Nebraska Revised Statutes chapter 76: one unit per section named in the chapter list, including sections shown as repealed or transferred: the number and catchline, the text (a table row per line), and the Source line of session laws. The cross references and annotations (case notes) printed after the Source line are left out.
- Sections were read from different web captures (2024-12-13 to 2026-10-22), so the single version is dated 2026-10-28, the newest capture day (or, if later, the day of the newest law already in the repository, or the day after it when the chapter would otherwise sort before it, so the history only grows); a section amended between its capture and that day would show its older text.
- Repealed and transferred sections whose page no archive holds (3: 76-217.05, 76-221, 76-1014) are taken from the chapter list, whose line for such a section is the whole text of its page.
- Missing from chapter 76: sections 76-217.01, 76-272, 76-602, 76-1431.02, 76-1431.03, 76-1431.04, 76-2005, 76-2205.02, 76-2804, 76-3802, 76-3803, 76-3804, 76-3805, 76-3806, 76-3807, 76-3808, 76-3809. they will be added as a later version when a copy can be read.

## What AI did and did not do

The scripts that read the sources and build this repository were written by Claude Code running Claude Opus 5.5 (`claude-opus-5-5`) under Lexifina's direction.

No model wrote, translated or corrected legal text. No model runs at build time. Every word of law in this repository comes from the official sources above.

The commit messages are written by `build.py` from the source data.

Model use at data-build time:
- Claude Code wrote the fetch and parse scripts; it wrote or changed no legal text. The scripts are deterministic and run no model.
- Claude Code wrote the code and chose the source; it did not write or alter any legal text. The code is deterministic and runs no model.
- Claude Code wrote the code and chose the source; it did not write or alter any legal text. The code is deterministic and runs no model.
- Claude Code wrote the code and chose the source; it did not write or alter any legal text. The code is deterministic and runs no model.
- Claude Code wrote the code and chose the source; it did not write or alter any legal text. The code is deterministic and runs no model.
