CANVAS_LENGTH = 5000

def no_matter_how_you_slice_it_part1(input_list):
    result = 0

    canvas = []
    for i in range(0,5000):
        row = [0] * 5000
        canvas.append(row)

    # Canvas is ready
    counter = 0
    for claim in input_list:
        counter += 1
        col = int(claim.split(",")[0].split("@ ")[1])
        row = int(claim.split(",")[1].split(":")[0])

        length = int(claim.split(",")[1].split("x")[0].split(": ")[1])
        height = int(claim.split("x")[1])

        # print("claim: {}, col:{}, row:{}, l:{}, h:{}".format(claim,col,row,length,height))
        for i in range(0,length):
            for j in range(0,height):
                if canvas[row +j][col +i] == 0:
                    canvas[row + j][col + i] = 1 # fresh cloth

                elif canvas[row + j][col + i] != -1: # if equality - cloth is already used by someone - already included in result
                    result += 1
                    canvas[row + j][col + i] = -1

    # print("counter: {}".format(counter))
    return result


def no_matter_how_you_slice_it_part2(input_list):
    result = 0

    canvas = []
    claim_canvas = []
    all_claim_id = set()
    perfect_claim_id = set()

    for i in range(0, CANVAS_LENGTH):
        row = [0] * CANVAS_LENGTH
        claim_row = [[0] for x in range(0,CANVAS_LENGTH)]
        claim_canvas.append(claim_row)
        canvas.append(row)

    # Canvas is ready
    counter = 0
    for claim in input_list:
        counter += 1
        col = int(claim.split(",")[0].split("@ ")[1])
        row = int(claim.split(",")[1].split(":")[0])

        length = int(claim.split(",")[1].split("x")[0].split(": ")[1])
        height = int(claim.split("x")[1])

        claim_id = int(claim.split(" @")[0].split("#")[1])
        # print(claim_id)
        all_claim_id.add(claim_id)

        perfect_claim_id.add(claim_id)

        for i in range(0, length):
            for j in range(0, height):
                # print("claim: {}, col:{}, row:{}, l:{}, h:{}".format(claim, col, row, length, height))
                claim_canvas[row + j][col + i].append(claim_id)
                # print(claim_canvas)

                if canvas[row + j][col + i] == 0:
                    canvas[row + j][col + i] = 1  # fresh cloth

                elif canvas[row + j][col + i] != -1:  # if equality - cloth is already used by someone - already included in result
                    result += 1
                    canvas[row + j][col + i] = -1

                    perfect_claim_id.discard(claim_id)
                    for cid in claim_canvas[row + j][col + i]:
                        perfect_claim_id.discard(cid)

                else:
                    perfect_claim_id.discard(claim_id)
                    for cid in claim_canvas[row + j][col+i]:
                        perfect_claim_id.discard(cid)


    # print("claim canvas")
    # print(claim_canvas)
    # print("part 2 counter: {}".format(counter))
    print(perfect_claim_id)

    return perfect_claim_id.pop()
