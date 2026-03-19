course_map = {
    "python": ["Python Basics", "OOP", "Projects"],
    "machine learning": ["ML Basics", "Regression", "Model Evaluation"],
    "deep learning": ["Neural Networks", "CNN"],
    "aws": ["Cloud Basics", "EC2", "S3"],
    "react": ["React Basics", "Hooks"]
}

dependencies = {
    "deep learning": ["machine learning"],
    "machine learning": ["python"]
}


def resolve_dependencies(skill, visited, order):
    if skill in visited:
        return

    visited.add(skill)

    for dep in dependencies.get(skill, []):
        resolve_dependencies(dep, visited, order)

    order.append(skill)


def generate_path(gap):
    visited = set()
    order = []

    for skill in gap:
        resolve_dependencies(skill, visited, order)

    path = {}

    for skill in order:
        path[skill] = course_map.get(skill, ["Learn basics"])

    return path