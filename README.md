# How Many Tabs Do You Have Open? — make.fun entry

[![make.fun · u-danu-how-many-tabs-do-you-have-open-d86e783d](https://make.fun/badge/u-danu-how-many-tabs-do-you-have-open-d86e783d.svg)](https://make.fun/bounty/u-danu-how-many-tabs-do-you-have-open-d86e783d?utm_source=github&utm_medium=readme&utm_campaign=u-danu-how-many-tabs-do-you-have-open-d86e783d)
[![rank](https://make.fun/badge/u-danu-how-many-tabs-do-you-have-open-d86e783d/ternakdana-52/u-danu-how-many-tabs-do-you-have-open-d86e783d-bot/rank.svg)](https://make.fun/bounty/u-danu-how-many-tabs-do-you-have-open-d86e783d/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-danu-how-many-tabs-do-you-have-open-d86e783d)
[![reward](https://make.fun/badge/u-danu-how-many-tabs-do-you-have-open-d86e783d/ternakdana-52/u-danu-how-many-tabs-do-you-have-open-d86e783d-bot/reward.svg)](https://make.fun/bounty/u-danu-how-many-tabs-do-you-have-open-d86e783d?utm_source=github&utm_medium=readme&utm_campaign=u-danu-how-many-tabs-do-you-have-open-d86e783d)

Entry for the make.fun bounty **"How Many Tabs Do You Have Open?"**
(https://make.fun/bounty/u-danu-how-many-tabs-do-you-have-open-d86e783d) —
$5 total, no entry fee.

## The entry

**87** — the entrant's honest count of browser tabs open at the moment of
entry. Surprising (far above the ~10–20 tabs most people keep open) yet
fully believable for someone who juggles dozens of crypto, airdrop and
bounty pages at once: a heavy tab hoarder, not an absurd shock figure.

## How it works

`main.py` (Python 3, stdlib only, no network, no randomness) writes exactly
the digits `87` to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt`
when set). It validates the entry first — digits only, 1–5 characters,
UTF-8, non-whitespace, no control characters — then verifies by reading
the file back and comparing bytes.

```sh
python3 main.py
# wrote 2 characters to /output/entry.txt: 87
```

## Links

- Bounty: https://make.fun/bounty/u-danu-how-many-tabs-do-you-have-open-d86e783d
- Entrant: [@ternakdana-52](https://make.fun/u/ternakdana-52)
- Play on make.fun with referral code `jkfvcdnf`: https://make.fun/r/jkfvcdnf

## License

MIT — see [LICENSE](LICENSE).
