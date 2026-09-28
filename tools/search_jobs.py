#!/usr/bin/env python3
"""Find job postings published in the last N hours on Greenhouse, Lever and Ashby boards.

Usage: python3 tools/search_jobs.py [--hours 24] [--companies tools/companies.txt]

Filters (from career-context.md): titles in any target track, location Montreal / Remote Canada /
Remote North America. Prints one line per match plus a list of slugs that didn't resolve.
Needs network access to boards-api.greenhouse.io, api.lever.co and api.ashbyhq.com.
"""
import argparse, json, re, sys, urllib.request, urllib.error
from datetime import datetime, timedelta, timezone

TITLE_IN = re.compile(r"product manager|product owner|product operations|product ops|"
                      r"customer success|implementation|solutions (manager|consultant|engineer)|"
                      r"onboarding|lifecycle|product specialist|technical account manager", re.I)
TITLE_OUT = re.compile(r"marketing|intern\b|director|\bvp\b|vice president|head of|principal|"
                       r"\bstaff\b|designer|sales development|account executive", re.I)
LOC_IN = re.compile(r"montr[eé]al|qu[eé]bec|canada|north america|\bnamer\b|americas|toronto|vancouver|"
                    r"calgary|ottawa|waterloo|edmonton|ontario|alberta|british columbia", re.I)
REMOTE = re.compile(r"remote|anywhere|distributed", re.I)
US_ONLY = re.compile(r"\b(us|usa|united states|u\.s\.)\b( only)?", re.I)


def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": "career-search"})
    with urllib.request.urlopen(req, timeout=20) as r:
        return json.load(r)


def greenhouse(slug):
    for j in get(f"https://boards-api.greenhouse.io/v1/boards/{slug}/jobs").get("jobs", []):
        ts = j.get("first_published") or j.get("updated_at")
        yield j["title"], (j.get("location") or {}).get("name", ""), ts, j["absolute_url"]


def lever(slug):
    for j in get(f"https://api.lever.co/v0/postings/{slug}?mode=json"):
        ts = datetime.fromtimestamp(j["createdAt"] / 1000, timezone.utc).isoformat()
        cats = j.get("categories", {})
        loc = " / ".join(filter(None, [cats.get("location"), j.get("workplaceType")] + cats.get("allLocations", [])))
        yield j["text"], loc, ts, j["hostedUrl"]


def ashby(slug):
    for j in get(f"https://api.ashbyhq.com/posting-api/job-board/{slug}").get("jobs", []):
        loc = " / ".join(filter(None, [j.get("location"), "Remote" if j.get("isRemote") else ""] +
                                [s.get("location", "") for s in j.get("secondaryLocations", [])]))
        yield j["title"], loc, j.get("publishedAt"), j["jobUrl"]


def location_ok(loc):
    if re.search(r"montr[eé]al", loc, re.I):
        return True
    if REMOTE.search(loc) and LOC_IN.search(loc):
        return True
    if re.fullmatch(r"\W*canada\W*", loc, re.I):
        return True  # "Canada" alone usually means anywhere in Canada
    if REMOTE.search(loc) and not re.sub(r"remote|anywhere|distributed|\W", "", loc, flags=re.I):
        return True  # bare "Remote": keep, verdict step checks eligibility
    return False


def parse(ts):
    if not ts:
        return None
    return datetime.fromisoformat(ts.replace("Z", "+00:00"))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--hours", type=float, default=24)
    ap.add_argument("--companies", default="tools/companies.txt")
    a = ap.parse_args()
    cutoff = datetime.now(timezone.utc) - timedelta(hours=a.hours)
    slugs = [l.strip() for l in open(a.companies) if l.strip() and not l.startswith("#")]
    hits, dead, blocked = [], [], False
    for slug in slugs:
        found = False
        for name, fn in (("greenhouse", greenhouse), ("lever", lever), ("ashby", ashby)):
            try:
                for title, loc, ts, url in fn(slug):
                    found = True
                    t = parse(ts)
                    if t and t >= cutoff and TITLE_IN.search(title) and not TITLE_OUT.search(title) \
                            and location_ok(loc):
                        hits.append((t, slug, title, loc, name, url))
            except urllib.error.HTTPError:
                continue
            except (urllib.error.URLError, OSError):
                blocked = True
                continue
        if not found:
            dead.append(slug)
    if blocked and not hits and len(dead) == len(slugs):
        sys.exit("Network blocked: allow boards-api.greenhouse.io, api.lever.co, api.ashbyhq.com")
    for t, slug, title, loc, src, url in sorted(hits, reverse=True):
        print(f"{t:%Y-%m-%d %H:%M} | {slug} | {title} | {loc} | {src} | {url}")
    print(f"\n{len(hits)} match(es) in the last {a.hours:g}h across {len(slugs) - len(dead)} boards.")
    if dead:
        print("No board found for:", ", ".join(dead))


if __name__ == "__main__":
    main()
