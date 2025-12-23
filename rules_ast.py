import ast
RISKY_FUNCTIONS = {"eval", "exec"}
class SecurityVisitor(ast.NodeVisitor):
    def __init__(self, filename):
        self.filename = filename
        self.issues = []
    def visit_Call(self, node):
        if isinstance(node.func, ast.Name):
            if node.func.id in RISKY_FUNCTIONS:
                self.issues.append({
                    "file": self.filename,
                    "line": node.lineno,
                    "severity": "ALTA",
                    "type": "Execução dinâmica perigosa",
                    "message": f"Uso de {node.func.id} detectado"
                })
        self.generic_visit(node)

def analyze_ast(code, filename):
    tree = ast.parse(code)
    visitor = SecurityVisitor(filename)
    visitor.visit(tree)
    return visitor.issues
