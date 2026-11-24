# Criterion scoring (1-5 per criterion; weights C1x5 C2x4 C3x3 C4x2 C5x1, max 75)
# C1 final text from a dying phone, phone's own voice, AND funny (gate: a message any healthy phone could send loses)
# C2 the joke lands: real turn, surprise, or specific detail — laugh out loud, not a polite smile
# C3 the voice is the phone's own: personality with a stake in dying, consistent first word to last
# C4 reads like a real text: short, punchy, no wasted words, nothing needing a second read
# C5 fresh: dodges obvious low-battery puns and the lines a hundred other entrants will write
# Manual scoring only — OpenRouter free key returns 402 until Nov 25 07:00 WIB.
# No judge numbers are invented here; these are internal rubric scores used to pick one line.

| id | line (short) | C1 | C2 | C3 | C4 | C5 | total | note |
|----|----|----|----|----|----|----|-------|------|
| c01 | I'm done. 47 tabs, 3am doomscrolls | 4 | 4 | 4 | 4 | 3 | 59 | "4% and a prayer" is good; tabs/brightness/3am are common ingredients |
| c02 | I quit. cleaning-rug videos at 3am | 5 | 5 | 5 | 4 | 5 | 73 | "videos of people cleaning rugs" is the funniest single specific detail in the set; "I hope you're happy" a great bitter kicker; 133 chars is long for a tie-break |
| c03 | two minutes' notice | 4 | 4 | 4 | 5 | 4 | 62 | "two minutes' notice" is a clever turn but one-note; resignation voice is slightly off a dying phone |
| c04 | screen time snitch | 5 | 5 | 5 | 5 | 5 | 75 | three distinct joke beats (screen-time snitch, "I kept receipts", "died a snitch"); specific detail (11 hours a day); shortest of the top 3 (113 chars) |
| c05 | walked past the charger on purpose | 5 | 4 | 5 | 5 | 5 | 71 | dark spite turn is strong; the laugh is a chuckle, not laugh-out-loud |
| c06 | Low Power Mode was hospice | 4 | 5 | 4 | 4 | 3 | 63 | hospice metaphor is genuinely fresh, but "Tell the charger I loved her" is the rejected R2 cliche verbatim |
| c07 | Low Power Mode waiting room | 4 | 4 | 4 | 4 | 4 | 60 | good metaphor, one beat, less laugh-out-loud than c06 |
| c08 | charger was three feet away | 4 | 4 | 4 | 4 | 3 | 59 | "Three. Feet." is punchy; charger-apology is a mild cliche |
| c09 | updates unforgiven / she knows | 4 | 4 | 4 | 4 | 4 | 60 | "she knows what she did" is meme-y; updates-as-killer is fresh |
| c10 | ducking hell / autocorrect | 5 | 5 | 5 | 4 | 5 | 73 | "ducking hell" + "Autocorrect kept me polite my whole life" are both phone-specific and funny; slightly one-note (both beats are autocorrect) and "this is how it ends" closes flat |
| c11 | one percent is a rumor / begging | 3 | 3 | 3 | 4 | 3 | 47 | good line ("a rumor") but it is a plea to survive, not a final text — fails C1's finality |
| c12 | cut off mid-sentence (scro—) | 5 | 4 | 4 | 3 | 4 | 63 | the cut-off device is the joke; needs a beat to parse the truncation |
| c13 | "I saw everything" cut off | 5 | 4 | 4 | 3 | 4 | 63 | "I saw everything" is a strong turn; same parse cost as c12 |
| c14 | I chose the void | 4 | 4 | 5 | 3 | 4 | 61 | dramatic and fresh; "This is what dying on your own terms looks like" is wordy for a text |

## Decision

**Winner: c04** — 75/75, the only candidate scoring 5 on every criterion.

> 1%. Before I go: your screen time this week was 11 hours a day. I kept receipts. Tell my charger I died a snitch.

113 chars / 113 bytes, one line, ASCII.

Lexicographic check (the judge decides on the first criterion where two entries differ):
- c04 vs c02: C1 5=5, C2 5=5, C3 5=5, C4 5>4 — c04 wins on punchiness/brevity, and is 20 chars shorter (tie-break favours smaller text).
- c04 vs c10: C1 5=5, C2 5=5, C3 5=5, C4 5>4 — c04 wins; three distinct beats vs two autocorrect beats, and no meme knowledge required.

Why c04 wins, criterion by criterion:
- C1: "1%." + "Before I go" + "I died a snitch" — unmistakably a dying phone's final text; no healthy phone sends this.
- C2: three beats, each a turn — the phone snitches on the owner's screen time (specific: 11 hours a day), "I kept receipts", then the punchline "died a snitch".
- C3: one consistent voice throughout — the phone as a witness with a grudge, using its last words to tell on its owner.
- C4: 113 chars, three short sentences, parses in a single read, no wasted words.
- C5: no browser history, no charger-as-lover, no brightness blame, no battery pun — the snitch angle is fresh.

Rejected cliches (criterion 5): "delete my browser history" (R1), "tell my charger I loved her" (R2), brightness blame (R3), low-battery puns (R4), generic warning as joke (R5). c06 was docked for carrying R2 verbatim.
