import os
from dotenv import load_dotenv
from groq import Groq
from rich import print

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# ===== THE TOOL (act): message in -> red flags out =====
def scan_for_red_flags(message):
    scam_words = ["pin", "urgent", "prize", "claim", "winner", "otp", "password", "suspended", "verify"]
    text = message.lower()
    flags = [w for w in scam_words if w in text]
    return flags

# ===== THE INSTRUCTIONS =====
system_prompt = """You help everyday people in Kenya spot scam messages.
When given a message, FIRST reply with exactly: TOOL: scan
You will then be told which red flags were found.
THEN reply starting with VERDICT: SAFE or VERDICT: LIKELY SCAM,
and explain warmly in simple words, with one piece of advice."""

# ===== NEW: ask the REAL PERSON for their message 👇 =====
print("[bold cyan]Paste the suspicious message you want to check:[/bold cyan]")
suspicious = input("> ")

messages = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": "Check this message: " + suspicious},
]

# ===== THE LOOP (think -> act -> look -> repeat) =====
for step in range(5):
    answer = client.chat.completions.create(
        model="llama-3.3-70b-versatile", messages=messages
    ).choices[0].message.content
    print("[dim]AI:[/dim]", answer)

    if answer.startswith("TOOL:"):
        found = scan_for_red_flags(suspicious)
        print("[yellow]tool found:[/yellow]", found)
        messages.append({"role": "assistant", "content": answer})
        messages.append({"role": "user", "content": "Red flags found: " + str(found)})
    else:
        print("[bold green]--- FINAL VERDICT ---[/bold green]")
        print(answer)
        break
