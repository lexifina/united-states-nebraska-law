"""Bring repo/README.md, repo/LICENSE and repo/jurisdiction.json up to date with the verified Nebraska Revised
Statutes parts (corpus.d/chapter-*.json that have a .PUBLISH sign-off). Idempotent; no network.
    python -X utf8 docs_ne.py
"""
import json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
R = os.path.join(HERE, 'repo')
NL = '\n'
CD = os.path.join(HERE, 'corpus.d')
parts = sorted(p for p in os.listdir(CD) if p.endswith('.json') and os.path.exists(os.path.join(CD, p[:-5] + '.PUBLISH'))) if os.path.isdir(CD) else []
acts = sorted((json.load(open(os.path.join(CD, p), encoding='utf-8'))['acts'][0] for p in parts), key=lambda a: a['slug'])


def gaps(a):
    n = a['versions'][0]['note']
    return n.split('so missing: ', 1)[1].rstrip('.') if 'so missing: ' in n else ''


rd = os.path.join(R, 'README.md')
x = open(rd, encoding='utf-8').read()
x = re.sub(r'\n\| `chapter-[^\n]*', '', x)
rows = ''.join(f"{NL}| `{a['slug']}/` | {a['title']} ({len(a['versions'][0]['units'])} sections" + (f"; missing {gaps(a)}" if gaps(a) else '')
               + f") | 1 | Oldest version available: the Legislature's online text, each section from its newest web capture, dated {a['versions'][0]['from']} |" for a in acts)
i = x.index('| `constitution/` |')
j = x.index(NL, i)
x = x[:j] + rows + x[j:]
x = x.replace(" The Legislature's terms could not be read.", '')
x = x.replace('The Constitution of Nebraska as a git repository: one file per section,',
              'The Constitution of Nebraska and chapters of the Nebraska Revised Statutes as a git repository: one file per section,')
x = re.sub(r'That is all the law this repository holds today\.[^\n]*',
           'That is all the law this repository holds today. This is a first build: most chapters of the Nebraska Revised Statutes, the session laws and regulations are not in it, and it has no amendment history yet.', x)
src = ('\n\nThe Nebraska Revised Statutes are published one page per section (nebraskalegislature.gov/laws/statutes.php?statute=...), '
       'with a list of sections per chapter. Each section was read from its newest **Common Crawl** capture, or, where Common '
       'Crawl had none, its newest **Internet Archive** capture from 2025 on. A unit holds the section number and catchline, '
       'the text and the "Source:" line of session laws; the cross references and the annotations (case notes) printed below '
       'it are not taken. A repealed or transferred section no archive holds is taken from the chapter list, whose line for it '
       'is the whole text of its page. A live section no archive holds is missing, and the table above names it. The '
       'Legislature\'s disclaimer page makes no reuse restriction; it asks readers to rely on the printed official publication.')
x = x.replace(src, '')
k = x.index('## Dates')
x = x[:k].rstrip(NL) + src + NL + NL + x[k:]
dl = ("- Each statutes chapter is one version, dated by the newest capture day of its section pages (or, if later, the day "
      "of the newest law already in the repository, so the history only grows), and credited to the publisher as \"oldest "
      "version available\". Sections were captured on different days, which the commit's note gives; a section amended "
      "after its capture would show its older text here.")
x = re.sub(r'\n- Each statutes chapter is one version[^\n]*', '', x)
k = x.index('## What it does not show')
x = x[:k].rstrip(NL) + NL + dl + NL + NL + x[k:]
x = x.replace('- Any history before that certification, and any amendment after it.',
              '- Any history of the Constitution before that certification, and any amendment after it.')
x = re.sub(r'\n- The other chapters of the Revised Statutes[^\n]*', '', x)
k = x.index('- Nothing here is an official publication')
x = x[:k] + '- The other chapters of the Revised Statutes, the annotations and cross references, and the sections named as missing above.' + NL + x[k:]
open(rd, 'w', encoding='utf-8', newline=NL).write(x)

lp = os.path.join(R, 'LICENSE')
lt = open(lp, encoding='utf-8').read()
para = ('The Nebraska Revised Statutes chapters are the text published by the Nebraska Legislature at'
        + NL + 'https://nebraskalegislature.gov/laws/browse-statutes.php , read from Common Crawl and Internet Archive captures of'
        + NL + 'its pages (2024 to 2026). Statute text is not copyrightable (Georgia v. Public.Resource.Org, above); the Revisor\'s'
        + NL + 'annotations and cross references are not used. The Legislature\'s disclaimer page places no restriction on reuse.')
if acts and para not in lt:
    k = lt.index('Changes made by Lexifina')
    lt = lt[:k] + para + NL + NL + lt[k:]
    open(lp, 'w', encoding='utf-8', newline=NL).write(lt)

jp = os.path.join(R, 'jurisdiction.json')
j = json.load(open(jp, encoding='utf-8'))
base = j['build'].split('; statutes not obtained')[0].split('; plus Revised Statutes')[0]
if acts:
    base = base.replace('Constitution only,', 'Constitution,')
    base += '; plus Revised Statutes chapters ' + ', '.join(a['short'].rsplit('ch. ', 1)[1] for a in acts) + ' (one version each, from web captures)'
else:
    base += '; statutes not obtained'
j['build'] = base
open(jp, 'w', encoding='utf-8', newline=NL).write(json.dumps(j, ensure_ascii=False, indent=2) + NL)
print(len(acts), 'chapters in docs')
