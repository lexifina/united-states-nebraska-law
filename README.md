# Nebraska: law history in git

The Constitution of Nebraska and chapters of the Nebraska Revised Statutes as a git repository: one file per section, one paragraph per line, so `git blame` works line by line. It follows the shared design of [lexifina/global-law](https://github.com/lexifina/global-law).

**What is in it now**

| Folder | Act | Versions | History |
| --- | --- | ---: | --- |
| `constitution/` | Constitution of the State of Nebraska (207 provisions) | 1 | Oldest version available: certified 2 December 2024 |
| `chapter-0021/` | Nebraska Revised Statutes, Chapter 21: Corporations and other companies (1555 sections; missing 21-289, 21-290, 21-2,134, 21-2,137, 21-2,139) | 1 | Oldest version available: the Legislature's online text, each section from its newest web capture, dated 2026-10-29 |
| `chapter-0025/` | Nebraska Revised Statutes, Chapter 25: Courts; civil procedure (1545 sections; missing 25-542, 25-2133, 25-2134, 25-21,157, 25-21,287, 25-21,291, 25-21,304, 25-21,305, 25-21,306, 25-3108, 25-3109) | 1 | Oldest version available: the Legislature's online text, each section from its newest web capture, dated 2026-10-28 |
| `chapter-0028/` | Nebraska Revised Statutes, Chapter 28: Crimes and punishments (780 sections; missing 28-433, 28-434, 28-435, 28-435.01, 28-449, 28-450, 28-627.04, 28-907.01, 28-1903) | 1 | Oldest version available: the Legislature's online text, each section from its newest web capture, dated 2026-10-16 |
| `chapter-0076/` | Nebraska Revised Statutes, Chapter 76: Real property (1131 sections; missing 76-217.01, 76-272, 76-602, 76-1431.02, 76-1431.03, 76-1431.04, 76-2005, 76-2205.02, 76-2804, 76-3802, 76-3803, 76-3804, 76-3805, 76-3806, 76-3807, 76-3808, 76-3809) | 1 | Oldest version available: the Legislature's online text, each section from its newest web capture, dated 2026-10-28 |

That is all the law this repository holds today. This is a first build: most chapters of the Nebraska Revised Statutes, the session laws and regulations are not in it, and it has no amendment history yet.

## Where the text comes from

The Constitution is the Legislature's own PDF, "Certified by Secretary of State's Office and Distributed by Clerk of the Legislature's Office, Lincoln, Nebraska, December 2, 2024" (<https://nebraskalegislature.gov/FloorDocs/Current/PDF/Constitution/constitution.pdf>), whose cover letter from the Revisor of Statutes says it includes Initiative Measure No. 434, adopted on 4 November 2024. The Legislature's server does not accept connections from the machine that built this repository, so the bytes are the Internet Archive's copy of that file.

The Nebraska Revised Statutes are published one page per section (nebraskalegislature.gov/laws/statutes.php?statute=...), with a list of sections per chapter. A unit holds the section number and catchline, the text and the "Source:" line of session laws; the cross references and the annotations (case notes) printed below it are not taken. A repealed or transferred section no archive holds is taken from the chapter list, whose line for it is the whole text of its page. A live section no archive holds is missing, and the table above names it. The Legislature's disclaimer page makes no reuse restriction; it asks readers to rely on the printed official publication.

## Dates

- The single version is dated **2 December 2024**, the certification date on the PDF's cover. It is the oldest version available.
- The first commit is credited to the publisher as "oldest version available".
- Each statutes chapter is one version, dated by the newest capture day of its section pages (or, if later, the day of the newest law already in the repository, so the history only grows), and credited to the publisher as "oldest version available". Sections were captured on different days, which the commit's note gives; a section amended after its capture would show its older text here.

## What it does not show

- Any history of the Constitution before that certification, and any amendment after it.
- The "Source:" line under each section (which names the amending measure), running heads and page numbers, and the sections headed "Repealed" or "Obsolete", are left out.
- Paragraph breaks are rebuilt from the PDF's line layout, so a break can be missing or extra in a long section.
- The other chapters of the Revised Statutes, the annotations and cross references, and the sections named as missing above.
- Nothing here is an official publication or legal advice.

## How it is checked

- Every unit is read back from git on its day and compared with the corpus (`tools/check_repo.py`; results in `REPRODUCE.md`).
- The source is identified by its sha256, in `data/versions.json`.
