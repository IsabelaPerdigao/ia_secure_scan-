import sys
from rules_ast import analyze_ast
from rules_regex import analyze_regex
from report import print_report
def scan_file(path):
    with open(path, "r", encoding="utf-8") as f:
        code = f.read()
    findings = []
    findings.extend(analyze_ast(code, path))
    findings.extend(analyze_regex(code, path))
    print_report(findings)
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python scanner.py <arquivo.py>")
        sys.exit(1)
    scan_file(sys.argv[1])

