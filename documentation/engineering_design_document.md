# Engineering Design Document (EDD)

## 1. Architecture
- Single-file Streamlit app: `app.py`
- No backend services
- Logging via Python `logging` module (console by default), configurable via env vars later

## 2. Tech Stack
- Python 3.9+
- Streamlit (stable pinned version)

## 3. Directory Structure
```
/ (repo root)
  app.py                # Streamlit entrypoint (to be created post-approval)
  requirements.txt      # Dependencies (to be created post-approval)
  .gitignore            # Git ignores (to be created post-approval)
  .streamlit/           # Local config dir (secrets.toml ignored by git)
  documentation/
    requirements.md
    product_requirements_document.md
    engineering_design_document.md
    deployment_guide.md
    user_guide.md
```

## 4. Dependencies
- streamlit==1.36.x (or latest stable at implementation time)

## 5. Configuration
- `.streamlit/secrets.toml` for future secrets; ensured in `.gitignore`

## 6. Logging & Error Handling
- Initialize a module-level logger using Python `logging`
- Default level INFO; can be overridden via env var in future
- Use structured, concise log messages

## 7. Security
- Never commit secrets; `.streamlit/secrets.toml` is ignored

## 8. Testing Strategy (minimal for this scope)
- Manual validation: app renders "Hello World"

## 9. Deployment Considerations
- Local run via Streamlit CLI
- Future: containerization/net deploy as needed

## 10. Acceptance Tests
- `streamlit run app.py` shows "Hello World" in the browser
