#!/bin/bash
# Scaffold a new NeetCode problem in both languages.
#
# Usage:   ./new.sh <topic> <problem-name>
# Example: ./new.sh two-pointers valid-palindrome
#
# Creates:
#   python/<topic_snake>/<problem_snake>.py
#   typescript/src/<topic>/<problem-name>.ts
#   typescript/src/<topic>/<problem-name>.test.ts

set -euo pipefail
cd "$(dirname "$0")"

if [ $# -ne 2 ]; then
  echo "Usage: ./new.sh <topic> <problem-name>   (kebab-case, e.g. ./new.sh two-pointers valid-palindrome)"
  exit 1
fi

TOPIC="$1"                                 # kebab-case, e.g. two-pointers
NAME="$2"                                  # kebab-case, e.g. valid-palindrome
TOPIC_SNAKE="${TOPIC//-/_}"
NAME_SNAKE="${NAME//-/_}"
# camelCase function name, e.g. validPalindrome
FUNC="$(echo "$NAME" | awk -F- '{ printf "%s", $1; for (i=2; i<=NF; i++) printf "%s%s", toupper(substr($i,1,1)), substr($i,2) }')"
# Title Case, e.g. Valid Palindrome
TITLE="$(echo "$NAME" | awk -F- '{ for (i=1; i<=NF; i++) printf "%s%s%s", toupper(substr($i,1,1)), substr($i,2), (i<NF ? " " : "") }')"

PY_FILE="python/$TOPIC_SNAKE/$NAME_SNAKE.py"
TS_FILE="typescript/src/$TOPIC/$NAME.ts"
TS_TEST="typescript/src/$TOPIC/$NAME.test.ts"

for f in "$PY_FILE" "$TS_FILE" "$TS_TEST"; do
  if [ -e "$f" ]; then
    echo "Refusing to overwrite existing file: $f"
    exit 1
  fi
done

mkdir -p "python/$TOPIC_SNAKE" "typescript/src/$TOPIC"

cat > "$PY_FILE" <<EOF
"""
LeetCode ?. $TITLE
https://leetcode.com/problems/$NAME/

Run just this file:   python $TOPIC_SNAKE/$NAME_SNAKE.py
Run its tests:        pytest $TOPIC_SNAKE/$NAME_SNAKE.py -v
"""


class Solution:
    def $FUNC(self):
        pass


# ---------------------------- tests ----------------------------

def test_example_1():
    assert Solution().$FUNC() == ...


if __name__ == "__main__":
    s = Solution()
    print(s.$FUNC())
EOF

cat > "$TS_FILE" <<EOF
/**
 * LeetCode ?. $TITLE
 * https://leetcode.com/problems/$NAME/
 *
 * Run just this file:   npx tsx src/$TOPIC/$NAME.ts
 * Run its tests:        npx vitest run src/$TOPIC/$NAME.test.ts
 */

export function $FUNC(): void {
  // TODO
}

// Quick manual run / debugging playground — runs only when executed directly.
if (import.meta.url === \`file://\${process.argv[1]}\`) {
  console.log($FUNC());
}
EOF

cat > "$TS_TEST" <<EOF
import { describe, expect, it } from "vitest";
import { $FUNC } from "./$NAME.ts";

describe("$FUNC", () => {
  it("example 1", () => {
    expect($FUNC()).toEqual(undefined);
  });
});
EOF

echo "Created:"
echo "  $PY_FILE"
echo "  $TS_FILE"
echo "  $TS_TEST"
