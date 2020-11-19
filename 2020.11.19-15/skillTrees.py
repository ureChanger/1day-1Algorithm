def solution(skill, skill_trees):
    #문제이해
    #추상화: 남은 skill 중 맨 앞과 같은지 확인
    #계획: 1. skill_trees로 for문(skills) 2. skills로 for문(i) - skill에 없으면 패스, 있으면 맨 앞과 같은지 비교(다르면 break)
    answer = 0
    skillA = skill
    for skills in skill_trees:
        skillA = skill
        for i in skills:
            if i in skillA:
                if i != skillA[0]:
                    break
                else:
                    skillA = skillA[1:]
            
            if i == skills[-1]:
                print(skills)
                answer += 1
    
    return answer
