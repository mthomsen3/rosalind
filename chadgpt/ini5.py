def extract_even_lines(input_file, output_file):
    with open(input_file, 'r') as in_file, open(output_file, 'w') as out_file:
        lines = in_file.readlines()
        for i, line in enumerate(lines):
            if (i + 1) % 2 == 0:
                out_file.write(line)

input_file = "input.txt"
output_file = "output.txt"
extract_even_lines(input_file, output_file)