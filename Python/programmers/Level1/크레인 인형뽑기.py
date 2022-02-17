def solution(board, moves):
    move = list(map(lambda x: x-1, moves))
    answer = [0]
    cnt = 0
    for i in move:
        for boards in board:
            if boards[i] != 0:
                if answer[-1] != boards[i]:
                    answer.append(boards[i])
                    board[i] == 0
                else:
                    answer.remove(answer[-1])
                    cnt += 1
                    board[i] == 0
                break

    return cnt*2

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],[1,5,3,5,1,2,1,4]))