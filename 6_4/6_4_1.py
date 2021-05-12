def merge(massive):
    while len(massive) > 1:
        data.append(merge_list(massive[0], massive[1]))
        del massive[0]
        del massive[0]
    return massive[0]


def merge_list(first_massive, second_massive):
    # label Dz
    result_massive = []
    i = 0
    j = 0
    result_number = 0
    for number in range(len(first_massive) + len(second_massive)):
        if i < len(first_massive) and j < len(second_massive) and first_massive[i] <= second_massive[j]:
            result_massive.append(first_massive[i])
            i += 1
        elif j < len(second_massive) and i < len(first_massive) and first_massive[i] > second_massive[j]:
            result_massive.append(second_massive[j])
            j += 1
            result_number += 1

    special_list.append(result_number)
    return result_massive


if __name__ == "__main__":
    special_list = []
    value = int(input())
    data = list(map(lambda x: [int(x)], input().split()))
    merge(data)
    print(sum(special_list))
