# Wojciech Lidwin

def elephants():
    try:
        result = 0
        minimum = 65000
        weights = []
        original = []
        final = []
        permutation = []
        visited = []

        file_name = input()
        f = open(file_name, "r")
        number_of_elephants = int(f.readline())
        weights_from_file = f.readline()
        original_setup_from_file = f.readline()
        final_setup_from_file = f.readline()

        for index in weights_from_file.split(" "):
            weights.append(int(index))
        for index in original_setup_from_file.split(" "):
            original.append(int(index))
        for index in final_setup_from_file.split(" "):
            final.append(int(index))

        for index in weights:
            minimum = min(minimum, index)
        for index in range(number_of_elephants):
            permutation.append(0)
            visited.append(False)
        for index in range(number_of_elephants):
            permutation[final[index] - 1] = original[index]

        for number, element in enumerate(weights):
            if not visited[number]:
                sum = 0
                length = 0
                weight = 65000
                current_number = number
                for value in weights:
                    length += 1
                    weight = min(weight, weights[current_number])
                    sum += weights[current_number]
                    current_number = permutation[current_number] - 1
                    visited[current_number] = True
                    if (current_number == number):
                        break
                result += min(sum + (length - 2) * weight, sum + weight + (length + 1) * minimum)
        print(result)

    except Exception:
        pass


if __name__ == "__main__":
    elephants()
