import json
from transformers import AutoTokenizer

INPUT_TXT = "Harry_Potter.txt"
OUTPUT_JSONL = "hp_gemma_lora_dataset.jsonl"

MODEL_NAME = "google/gemma-3-1b-it"

MAX_TOKENS = 1024
OVERLAP_TOKENS = 80
MIN_TOKENS = 300

tokenizer = AutoTokenizer.from_pretrained(
    MODEL_NAME,
    use_fast=True
)

buffer = ""
buffer_tokens = []

def write_chunk(tokens, out_file):
    text = tokenizer.decode(tokens, skip_special_tokens=True).strip()

    if not text:
        return

    record = {
        "messages": [
            {
                "role": "user",
                "content": "Continue the following text in the same writing style:\n\n" + text
            },
            {
                "role": "assistant",
                "content": text
            }
        ]
    }

    out_file.write(json.dumps(record, ensure_ascii=False) + "\n")

with open(INPUT_TXT, "r", encoding="utf-8") as f_in, \
     open(OUTPUT_JSONL, "w", encoding="utf-8") as f_out:

    for line_num, line in enumerate(f_in, start=1):
        buffer += line
        buffer_tokens = tokenizer.encode(
            buffer,
            add_special_tokens=False
        )

        if len(buffer_tokens) >= MAX_TOKENS:
            chunk_tokens = buffer_tokens[:MAX_TOKENS]

            if len(chunk_tokens) >= MIN_TOKENS:
                write_chunk(chunk_tokens, f_out)

            buffer_tokens = buffer_tokens[MAX_TOKENS - OVERLAP_TOKENS:]
            buffer = tokenizer.decode(
                buffer_tokens,
                skip_special_tokens=True
            )

        if line_num % 500 == 0:
            print(f"Processed {line_num} lines")

    if len(buffer_tokens) >= MIN_TOKENS:
        write_chunk(buffer_tokens, f_out)

print("JSONL creation finished safely")
