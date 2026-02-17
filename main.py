import os

from earning_api import get_transcripts
from system_prompt import SYSTEM_PROMPT


# Define system prompt
_ = SYSTEM_PROMPT

# Select company to analyze (get from front-end user input)
symbol = os.getenv("ALPHAVANTAGE_SYMBOL", "MSFT")

# Connect to earnings call API and get most recent transcripts
transcript_new, transcript_old = get_transcripts(symbol)
# print(transcript_new)
# print(transcript_old)
print(transcript_new.get("quarter"), transcript_new.get("symbol"))
print(transcript_old.get("quarter"), transcript_old.get("symbol"))

# print(transcript_new.keys())

# Pass system prompt and earning call JSONs to LLM
#combine systmem prompt earning call transcripts
llm_input = (
    f"{SYSTEM_PROMPT}\n\nMost recent transcript:\n"
    f"{transcript_new.get('transcript_text', '')}\n\nPrior transcript:\n"
    f"{transcript_old.get('transcript_text', '')}"
)

#call LLM

llm_output = " "


# Pass output to front end
