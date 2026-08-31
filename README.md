# NeetCode 150 — local practice environment

Solve problems in **Python** and **TypeScript**, run and debug them locally before submitting to LeetCode.

The solutions intentionally start incomplete. A failing test is your feedback loop, not a broken setup: choose one exercise, make its tests pass, then move to the next.

## Quick start

```bash
./practice list --todo
./practice test py arrays-hashing/two-sum
./practice run ts arrays-hashing/two-sum
```

`./practice list` shows the available exercises and marks files you have started. Problem names can be abbreviated when they are unique, for example `./practice test py two-sum`.

## Web app

```bash
cd web
npm install
npm run dev
```

Open `http://localhost:3000`. Choose a problem, edit its Python or TypeScript solution, and click **Run tests**. The editor saves directly to the existing exercise file before running its focused local test suite.

### AI Roast Mode

Keep the Anthropic key local—do not paste it into the browser or commit it:

```bash
cd web
cp .env.example .env
```

Open `web/.env`, replace the placeholder with your key, and restart `npm run dev`. Turn on **🔥 AI** above the editor. After you pause typing, the coach reviews the code line by line with technical praise, playful roasts, and hints. Identical code reviews are cached to reduce API usage.

## Layout

```
neetcode-150/
├── new.sh                  # scaffold a new problem in both languages
├── python/
│   ├── .venv/              # virtualenv with pytest
│   └── arrays_hashing/
│       └── two_sum.py      # solution + tests in one file
└── typescript/
    └── src/
        └── arrays-hashing/
            ├── two-sum.ts       # solution + runnable main block
            └── two-sum.test.ts  # vitest tests
```

Topics follow the NeetCode 150 roadmap: `arrays-hashing`, `two-pointers`, `sliding-window`, `stack`, `binary-search`, `linked-list`, `trees`, `tries`, `heap`, `backtracking`, `graphs`, `advanced-graphs`, `1d-dp`, `2d-dp`, `greedy`, `intervals`, `math-geometry`, `bit-manipulation`.

## Start a new problem

```bash
./new.sh two-pointers valid-palindrome
```

Creates skeleton files in both languages with the right names. Paste the problem's examples in as test cases, then implement.

## Python

```bash
cd python
source .venv/bin/activate      # or use .venv/bin/python directly
python arrays_hashing/two_sum.py            # run the file's main block
pytest arrays_hashing/two_sum.py -v         # run one problem's tests
pytest                                      # run all tests
```

If the virtual environment ever needs rebuilding:

```bash
python3 -m venv python/.venv
python/.venv/bin/pip install -r python/requirements-dev.txt
```

Each file keeps the LeetCode `class Solution` shape, so you can copy-paste the class straight into LeetCode.

## TypeScript

```bash
cd typescript
npx tsx src/arrays-hashing/two-sum.ts             # run the file's main block
npx vitest run src/arrays-hashing/two-sum.test.ts # run one problem's tests
npm test                                          # run all tests
npm run test:watch                                # re-run tests on save
npm run typecheck                                 # check TypeScript types
```

Run `npm install` inside `typescript/` if dependencies are missing.

Copy just the function body into LeetCode (drop the `export`).

## Debugging (VS Code / Cursor)

Open **this folder** as the workspace. Set a breakpoint, then Run and Debug (⇧⌘D) with:

- **Python: debug current file** — runs the `__main__` block of the open file
- **Python: debug tests in current file** — runs its pytest tests under the debugger
- **TypeScript: debug current file (tsx)** — runs the file's main block
- **TypeScript: debug tests in current file (vitest)** — runs its tests under the debugger

The main block in each file is a scratch area — call your function with whatever input you're trying to debug, set breakpoints, and step through.
