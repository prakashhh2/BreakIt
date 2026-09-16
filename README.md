# BreakTheCode backend

This small API uses LangChain to explain C++ code in simple language.

## Run it

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirement.txt
```

Create `backend/.env`:

```env
OPENAI_API_KEY=your-api-key
OPENAI_MODEL=gpt-4o-mini
```

Start the server:

```bash
uvicorn main:app --reload
```

Send C++ code to `POST /explain`:

```json
{
  "code": "#include <iostream>\nint main() { std::cout << \"Hello\"; }"
}
```
