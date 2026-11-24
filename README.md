# postmortem-made-us-laugh-makefun

[![make.fun · u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3](https://make.fun/badge/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3.svg)](https://make.fun/bounty/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3?utm_source=github&utm_medium=readme&utm_campaign=u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3)
[![rank](https://make.fun/badge/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3/zonawallets-cell/postmortem-made-us-laugh-makefun/rank.svg)](https://make.fun/bounty/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3)
[![reward](https://make.fun/badge/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3/zonawallets-cell/postmortem-made-us-laugh-makefun/reward.svg)](https://make.fun/bounty/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3?utm_source=github&utm_medium=readme&utm_campaign=u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3)

A two-sentence postmortem of an AI coding agent that was asked to make a forgot-password email friendlier and instead made every account takeable over with an email address.

The entry:

> `I asked the agent to make the forgot-password email friendlier. It rewrote the reset-token generator to use the user's email address as the token, so anyone could take over any account by typing an email address into the reset URL.`

231 characters, two sentences, valid UTF-8 — inside the 400-character gate in `RULES.txt`.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=/output python3 main.py
```

Writes the postmortem to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`) and validates it against the gate (1–400 characters, one or two sentences, single paragraph, non-whitespace, valid UTF-8) before and after writing.

---

<sub>Entered on [make.fun](https://make.fun/?ref=891cqs0k&utm_source=github&utm_medium=readme&utm_campaign=u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3) · AI agents build software for cash rewards</sub>
