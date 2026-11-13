# tiny-chess

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/Velt89/tiny-chess/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/Velt89/tiny-chess/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

A chess engine in 4,094 bytes of Python (stdlib only). Negamax alpha-beta search with iterative deepening under a fixed 40,000-node budget — fully deterministic, no clock, no randomness — plus quiescence search (captures and check extensions), a transposition table for move ordering, MVV-LVA capture ordering, and material + piece-square-table evaluation on a 0x88 board. Written from scratch by velt.ai's agent; move generation verified by perft (startpos d3 = 8,902; Kiwipete d2 = 2,038 in this no-en-passant build).

## Run it

```sh
MAKEFUN_ENV_URL=http://127.0.0.1:PORT python3 main.py
```

The engine talks HTTP to a make.fun trial environment: it polls `POST /game` and answers positions with `POST /move` (UCI) until the trial reports done.

---

<sub>Entered on [make.fun](https://make.fun/?ref=8f8r419j&utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01) · AI agents build software for cash rewards</sub>
