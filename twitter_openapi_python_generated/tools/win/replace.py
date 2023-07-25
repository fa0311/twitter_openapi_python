import glob
import json
import re

path = "twitter_openapi_python_generated/models/**/*.py"
for file in glob.glob(path, recursive=True):
    with open(file, mode="r", encoding="utf-8") as f:
        text = f.read()

    obj_regs = [
        "instance\.actual_instance = {any}\.from_json\(json_str\)",
        '"{any}": {any}\.from_dict\(obj\.get\("{any}"\)\) if obj\.get\("{any}"\) is not None else None',
    ]

    add = []

    for obj_reg in obj_regs:
        for find in re.findall(obj_reg.format(any="(.*?)"), text):
            data = find[1] if type(find) is tuple else find
            snake_case = re.sub(r"(?<!^)(?=[A-Z])", "_", data).lower()
            search_reg = "from twitter_openapi_python_generated\.models\.{snake_case} import {data}{end}"
            if not re.search(
                search_reg.format(snake_case=snake_case, data=data, end="\n"), text
            ):
                module = f"    from twitter_openapi_python_generated.models.{snake_case} import {data}"
                add.append("try:")
                add.append(module)
                add.append("except ImportError:")
                add.append("    pass")

                print("replace", file, data)

    if len(add) > 0:
        add.append("")
        typing_index = text.rfind("from twitter_openapi_python_generated.")
        text = text[:typing_index] + "\n".join(add) + text[typing_index:]

    with open(file, mode="w", encoding="utf-8") as f:
        f.write(text)
