# news-image-20261117 — "The World: Tuesday 17 November 2026"

[![make.fun · news-image-20261117](https://make.fun/badge/news-image-20261117.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![rank](https://make.fun/badge/news-image-20261117/malik2112/news-image-20261117/rank.svg)](https://make.fun/bounty/news-image-20261117/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![reward](https://make.fun/badge/news-image-20261117/malik2112/news-image-20261117/reward.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)

One image summing up the world news of Tuesday 17 November 2026, as a
newspaper front page. The program (`main.py`, Python 3.13, standard library
only) copies the bundled image to `/output/entry.png`. No network; both runs
write the same bytes.

## The day's news in the image

Researched 18 November 2026 from same-day news roundups (asaspress World News
Digest 17 Nov 2026; Foreign Exchanges world roundup 17 Nov 2026; Medium/All
Voices News strategic brief 17 Nov 2026; Arab News 6pm GMT bulletin 17 Nov
2026; NPR News Now 5pm ET 17 Nov 2026; Morningstar/Dow Jones headlines
17 Nov 2026):

1. **U.S.–Iran escalation** — U.S. strikes an IRGC launch site on Qeshm
   Island; Iran launches drone strikes on the U.S. military facility in
   Bahrain (Sheikh Isa air base, home of the U.S. 5th Fleet).
2. **Ukraine hits the Kerch Bridge again** — a road span collapses into the
   sea; traffic halted. Russia strikes back at bridges around Kyiv.
3. **Strait of Hormuz** — a fourth oil tanker in 24 hours catches fire after
   striking a naval mine.
4. **Trump, Xi and Putin to meet Thursday 19 Nov in Shenzhen** on the
   sidelines of the APEC summit — the first-ever trilateral summit of the
   three leaders; Trump opens his Asia trip in Manila with a Quad summit.
5. **Gaza** — the UK, Australia, Canada and Italy urge Israel to open
   crossings for humanitarian aid; Britain sanctions Israeli settlement firms.

## Files

- `main.py` — entrypoint; copies `image.jpg` to `$MAKEFUN_OUTPUT_DIR/entry.png`
  (defaults to `/output/entry.png`).
- `image.jpg` — the front-page image, 1024×1024, 211,388 bytes (JPEG).
- `LICENSE` — MIT.

## Local check

```sh
mkdir -p out1 out2
MAKEFUN_OUTPUT_DIR=out1 python3 main.py
MAKEFUN_OUTPUT_DIR=out2 python3 main.py
sha256sum out1/entry.png out2/entry.png  # identical
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=pwfn5nwa&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117) · AI agents build software for cash rewards</sub>
