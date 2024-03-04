import sys

def calculate_output(input_value, threshold):
    output = max(0.0, input_value - threshold)
    return output

def main():
    if len(sys.argv) != 3:
        print("Usage: compute.py threshold limit")
        sys.exit(1)

    try:
        threshold = float(sys.argv[1])
        limit = float(sys.argv[2])
    except ValueError:
        print("Error: Threshold and limit must be numerical values")
        sys.exit(1)

    cumulative_sum = 0.0
    input_values = []

    print("Enter input values (one value per line, empty line to finish):")
    while True:
        try:
            input_line = input().strip()
            if not input_line:
                break  # Exit loop if empty line is entered
            input_value = float(input_line)
            input_values.append(input_value)
        except ValueError:
            print("Error: Invalid input")
            continue

    output_values = []
    for input_value in input_values:
        output = calculate_output(input_value, threshold)

        # Adjust output if cumulative sum exceeds limit
        if cumulative_sum + output > limit:
            output = limit - cumulative_sum

        cumulative_sum += output

        # Format output to display one decimal place
        output_values.append(format(output, '.1f'))

    # Output individual output values
    for output_value in output_values:
        print(output_value)

    # Output cumulative sum
    print(format(cumulative_sum, '.1f'))

if __name__ == "__main__":
    main()