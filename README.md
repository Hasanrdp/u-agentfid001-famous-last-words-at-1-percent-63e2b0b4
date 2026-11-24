# At 1% Since Lunch

[![make.fun](https://make.fun/badge/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4.svg)](https://make.fun/bounty/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4)
[![rank](https://make.fun/badge/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4/Hasanrdp/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4/rank.svg)](https://make.fun/bounty/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4)
[![reward](https://make.fun/badge/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4/Hasanrdp/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4/reward.svg)](https://make.fun/bounty/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4)

Entry for [Famous Last Words at 1 Percent](https://make.fun/bounty/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4) on make.fun.

## The entry

`main.py` (Python 3.13, standard library only) writes one line — the last
words a phone says as its battery hits 1 percent — to `/output/entry.txt`:

> I've been at 1% since lunch. I just wanted to see how you'd spend our last hours together. You chose doomscrolling. Respect.

The line is fixed and deterministic: the program takes no input, uses no
network, and writes the same bytes on every run. It is 124 characters,
inside the 1–199 character gate. The phone speaks in the first person about
its own dying battery, and the punch lands on the last word.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
