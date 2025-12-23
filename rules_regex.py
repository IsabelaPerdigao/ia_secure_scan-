import re

PATTERNS = [
    {
        "regex": r"(password|token|secret)\s*=\s*['\"](.+?)['\"]",
        "severity": "ALTA",
        "type": "Credencial hardcoded",
        "message": "Possível credencial exposta no código"
    },
    {
        "regex": r"cursor\.execute\(.+%\s*\w+",
        "severity": "MÉDIA",
        "type": "SQL sem parâmetros",
        "message": "Uso de SQL sem prepared statements" }]
def analyze_regex(code, filename):
    findings = []
    lines = code.splitlines()
    for idx, line in enumerate(lines, start=1):
        for pattern in PATTERNS:
            if re.search(pattern["regex"], line, re.IGNORECASE):
                findings.append({
                    "file": filename,
                    "line": idx,
                    "severity": pattern["severity"],
                    "type": pattern["type"],
                    "message": pattern["message"]
                })
    return findings

Report:
def print_report(findings):
    if not findings:
        print("✅ Nenhum problema crítico encontrado.")
        return
    print("\n🔍 RELATÓRIO DE SEGURANÇA\n")
    for f in findings:
        print(f"[{f['severity']}] {f['file']}:{f['line']}")
        print(f"  Tipo: {f['type']}")
        print(f"  Detalhe: {f['message']}\n")
    print(f"Total de alertas: {len(findings)}")
