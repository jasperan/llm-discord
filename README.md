# llm-discord

Fine-tune an LLM to create a Discord bot that behaves like your friends.

The repo has three parts:

1. **`discord_bot.py`**: a Discord bot that logs every message it can see to a local SQLite database (`messages.db`).
2. **Dataset scripts**: turn those messages (or public medical Q&A datasets) into JSON you can fine-tune on.
3. **[`hands-on/`](hands-on/guide.md)**: a walkthrough of LoRA fine-tuning with text-generation-webui, plus a [low-VRAM guide](hands-on/run_low_vram.md) (written July 2023, so upstream tools have changed since).

## Quick start

Requires [uv](https://docs.astral.sh/uv/). It installs Python 3.12 for you if needed.

```bash
git clone https://github.com/jasperan/llm-discord.git
cd llm-discord
uv sync
cp config.example.yaml config.yaml   # then paste your bot token into it
uv run discord_bot.py
```

Bot setup in the [Discord Developer Portal](https://discord.com/developers/applications):

- Create an application, add a bot, and copy its token into `config.yaml` as `API_TOKEN`. `config.yaml` is gitignored, so don't commit your token.
- Under **Bot → Privileged Gateway Intents**, enable **Presence**, **Server Members** and **Message Content**. The bot requests all intents, and it fails to connect if these are off.
- Invite the bot to your server with permission to read messages and message history.

Each message the bot sees is printed to the console and appended to the `messages` table (`author`, `content`) in `messages.db`.

## Build a fine-tuning dataset from your messages

```bash
uv run --with pandas compose_llm.py
```

The script reads `messages.db`, removes duplicate and empty messages, and writes:

- `messages.csv`, the cleaned messages;
- `output.json`, a list of `{"question": <message n-1>, "response": <message n>}` pairs.

## Medical datasets (optional)

These scripts were used to build an example dataset for the hands-on session. They need extra packages, which `uv run --with` pulls in without touching the project environment.

- **[MedQuAD](https://github.com/abachaa/MedQuAD)** (XML) to Alpaca-style JSON (`instruction` / `input` / `output`):

  ```bash
  git clone https://github.com/abachaa/MedQuAD.git
  uv run --with beautifulsoup4 --with lxml medquad/parse_xml.py MedQuAD   # writes output_<folder>.json
  uv run medquad/compose_json.py                                           # merges them into unique_file.json
  ```

- **[Medical Question Pairs](https://github.com/curai/medical-question-pair-dataset)**: put `mqp.csv` in the repo root, then run:

  ```bash
  uv run --with pandas create_new_question_jsonl.py   # writes medical.jsonl, one {"question": ...} per line
  ```

## License

[GPL-3.0](LICENSE)
