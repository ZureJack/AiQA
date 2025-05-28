from clang.cindex import Config, Index, CursorKind


# class Cparse:
#     def __init__(self, path:str):
#         Config.set_library_path(path)
#         self.ats = {}

def get_functions(filename):
    index = Index.create()
    tu = index.parse(filename)
    functions = []
    
    for node in tu.cursor.walk_preorder():
        if node.kind == CursorKind.FUNCTION_DECL:
            # 过滤掉编译器内置函数和无效位置
            if node.location.file and node.location.file.name == filename:
                functions.append(node)
    
    return functions

# 使用示例
functions = get_functions("./test.c")
for func in functions:
    print(f"函数名: {func.spelling}")