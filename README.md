# Scam Spotter Agent

An AI agent that detects scam messages using an agentic **think -> act -> look** loop.

Built as a hands-on project to learn how agentic AI works from the ground up:
tools, the reasoning loop, and the difference between an AI that only talks
and one that can actually *act*.

## What it does

You paste a suspicious message (e.g. a fake M-Pesa SMS). The agent:

1. **Thinks** - decides it needs to inspect the message
2. **Acts** - runs a scanner tool that checks the text for scam indicators
3. **Looks** - reads the scanner's findings and reasons about them
4. **Answers** - gives a verdict (SAFE / LIKELY SCAM) with a plain-language explanation

## How it works

- **The tool** (scan_for_red_flags) checks a message for known scam keywords and returns any it finds.
- **The AI** (via the Groq API) decides when to call the tool, interprets the results, and delivers a human-friendly verdict.
- **The loop** wires these together so the AI can act, observe, and respond - the core pattern behind all agentic AI.

## Running it

Install dependencies, then run: python agent.py
Requires a Groq API key in a .env file as GROQ_API_KEY=... (gitignored, never committed).

## Known limitation (and next steps)

The current tool uses keyword matching, which is deliberately simple and has a real weakness: a scam that avoids the listed words can slip through. For example, "kindly share the code sent to your phone" is a classic scam but contains none of the flagged keywords.

The next iteration moves from keyword-based detection to meaning-based detection - letting the AI judge the intent of a message rather than matching exact words, the way real phishing and spam filters work.

## What I learned

- How an agent differs from a plain LLM call (a loop + the ability to act)
- How tools return data the AI can reason over
- Why keyword detection is brittle and why semantic detection matters
- Safe handling of API keys (.env + .gitignore)
