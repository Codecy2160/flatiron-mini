import sys

def quicksort(data, key_index):
    if len(data) <= 1:
        return data
    pivot = data[len(data) // 2]
    pivot_key = pivot.split(',')[key_index]
    left = [x for x in data if x.split(',')[key_index] < pivot_key]
    middle = [x for x in data if x.split(',')[key_index] == pivot_key]
    right = [x for x in data if x.split(',')[key_index] > pivot_key]
    return quicksort(left, key_index) + middle + quicksort(right, key_index)

def sort_data(input_file, sort_field, sort_options):
    if sort_field not in sort_options:
        print(f"Invalid sort field: {sort_field}")
        sys.exit(1)
    with open(input_file, mode='r') as data_file:
        data = data_file.readlines()
        data = [line for line in data if len(line) > 1]
        data = quicksort(data, sort_options.index(sort_field))
    for line in data:
        print(line, end='')
    print(f"Sorted data by {sort_field}")

if __name__ == "__main__":
    sort_options = ['patient_id', 'first_name', 'last_name', 'age', 'diagnosis', 'severity', 'birth_date', 'created_at', 'updated_at']
    if len(sys.argv) != 3:
        print("Usage: python sort_data.py <input_file> <sort_field>")
        sys.exit(1)
    input_file = sys.argv[1]
    sort_field = sys.argv[2]
    sort_data(input_file, sort_field, sort_options)

    