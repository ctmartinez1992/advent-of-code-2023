def do_func_for_each_line_in_file(filepath, process_func, final_func):
    try:
        results = []
        with open(filepath, "r") as file:
            for line in file:
                results.append(process_func(line.strip()))

        return final_func(results)
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
