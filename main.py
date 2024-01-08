import os
import importlib.util

current_dir = os.path.dirname(__file__)
files_in_dir = os.listdir(current_dir)

for file in files_in_dir:
        if file.startswith("Prog_") and file.endswith(".py"):
            module_name = file[:-3]  # Remove the '.py' extension
            module_path = os.path.join(current_dir, file)
            spec = importlib.util.spec_from_file_location(module_name, module_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)

            # Check if the DajGlos function exists in the module and run it
            if hasattr(module, 'DajGlos') and callable(module.DajGlos):
                print("-----------------------------------------------------")
                print(f"Running DajGlos from {module_name}.py")
                module.DajGlos()
            else:
                 print(f"Did not found DajGlos definition in {module_name}.py")