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
