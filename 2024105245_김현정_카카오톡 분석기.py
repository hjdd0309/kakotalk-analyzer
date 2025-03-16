#파일 들여오는 코드
filename = 'abcd.txt' 
kt_file = open(filename,'r', encoding = 'utf8') 
kt_file_content = kt_file.readlines() 
kt_file.close()
#앞에 쓸데 없는 코드 지우기
del kt_file_content[0:3]

dic1 = {}#카톡 내용 중에서 이름과 카톡내용으로 키랑 벨류를 나누기 위해 딕셔너리를 설정하였습니다.
#print(kt_file_content)
for str1 in kt_file_content:
    if '님을 초대하였습니다.' in str1:
        pass# 밑에 3개 문구는 분석할 때 쓸데없는 요소들이여서 패스를 선언해줬습니다.
    elif '삭제된 메시지입니다.' in str1:
        pass
    elif '님이 나갔습니다.' in str1:
        pass
    elif str1.count('---------------') == 2:# 이거 두개 있으면 날짜가 떠서 이것도 쓸데 없기 때문에 패스처리를 해줬습니다.
        pass
    elif str1.startswith('['):#왼쪽 파라미터로 시작을 하면 밑 코드로 가게끔했고요
        temp = str1.split(']')#오른쪽 대괄호를 기준으로 스플릿을 넣어줬고요
        name = temp[0].strip('[')#temp라는 리스트의 0번째(이름)에서 '['를 지우고 name에 저장
        content = temp[2].strip('\n').strip(' ')#이 셀은 temp라는 리시트의 2번째 값(내용)에서 불필요한 부분('\n'과 공백)을 제거하기위해 넣었습니다. 제거 후 content에 저장
        if name in dic1:#이전에 말해서 딕셔너리에 이름이 key 값으로 존재하는 경우에는, 그 value인 리스트의 끝에 append로 content를 추가.
            dic1[name].append(content)
        else:#밑에 코드는 이전에 말한 적 없는 사람들한테 키랑 벨류를 선언해줌.
            dic1[name] = [content]
    else:
        content = str1.strip('\n')#줄바꿈을 한 대화에 \n을 없애주기 위해 넣었습니다
        dic1[name][-1] = dic1[name][-1] +' '+ content #줄 바꿈인 경우에 이전에 나온 채팅과 같은 채팅이므로 합쳐서 개수를 1개로 유지하기 위함.

laugh_list = ['ㅎ','ㅋㅋ']#웃음 리스트에 요소들을 입력해줌
cry_list=['ㅜ','ㅠ','ㅜㅜ']
swear_list=['ㅗ','ㅗㅗ','ㅗㅗㅗ']
#ㅎㅎㅎㅎㅎㅎㅎㅎㅋㅋ  예시들

laugh_dic = {}  #이름과 웃은 횟수를 저장하는 딕셔너리를 만들어 줌          
for name in dic1:#딕셔너리에서 key(이름)를 하나하나 반복하기 위해 for문을 선언해줌.
    count = 0    # 새롭게 시작한 사람은 셌던 횟수가 0으로 시작해야함. count를 0으로 초기화.
    for text in dic1[name]:#벨류에 있는 리스트 요소들을 하나씩 text로 받아주는 for문/ key값이 변경될 때마다 value 리스트도 변경
        for laugh in laugh_list:#웃음 리스트에 있는 웃음 요소들을 하나씩 받아주는 for문
            if laugh in text:#텍스트에 웃음 요소가 있다면#
                count += 1#카운트에 +1을 해주는 형식으로 진행이 됩니다
                break#예를 들어 ㅋㅋㅋㅎㅎㅎ으로 웃었어도 ㅎ으로 한번 웃은 걸로 치고 ㅋㅋ으로 카운트에 포함되지 않게 하기 위해서 break를 넣어줬습니다.
    laugh_dic[name] = count    #레프 딕셔너리에 이제 키를 name으로 count를 벨류로 갖게 딕셔너리를 만들어줬습니다.

cry_dic = {}#위와 같은 방식으로 리스트랑 딕셔너리 이름만 조금씩 바꿔서 코드를 입력해줌
for name in dic1:
    count = 0
    for text in dic1[name]:
        for cry in cry_list:
            if cry in text:
                count += 1
                #ㅠㅠㅜㅜㅠㅜㅠㅜㅠㅜㅜ  요소들
                break
    cry_dic[name] = count    

swear_dic = {}#여기도 똑같은 방식
for name in dic1:
    count = 0
    for text in dic1[name]:
        for swear in swear_list:
            if swear in text:
                count += 1
                break
    swear_dic[name] = count  


while True:# 종료하기 전까지 입력을 계속 받기 위해 while문을 넣어줬습니다.
    order = input("명령어를 입력하세요 : ")

    if order == '\stop':
        print("종료합니다.")
        break#종료합니다를 선언하면 while문을 벗어나야 하니까 break를 해줌.
    elif order == '\laugh':
        #웃음 횟수 세는 과정
        for name in laugh_dic:#레프 딕셔너리에 키를 반복해주고
            if(laugh_dic[name]>0):#해당 벨류가 0이상이라면
                print(name,":", laugh_dic[name])#이름과 : 해당 벨류를 출력합니다
    elif order == '\cry':#밑에는 다 똑같은 방식
        for name in cry_dic:
            if(cry_dic[name]>0):
                print(name,":", cry_dic[name])
    elif order == '\swear':
        for name in swear_dic:
            if(swear_dic[name]>0):
                print(name,":", swear_dic[name])
    
    elif order == '\\talk':
        for name in dic1:#모든 사람에 대한 대화 횟수를 구하기 위해 for문을 넣어줌.
            print(name, len(dic1[name]))#출력은 이름,횟수로 넣었습니다. 렌 함수로 받은 이유는 벨류 리스트에 있는 요소들의 개수를 세기 위해서 만들었습니다.

    else:
        for name in dic1: #나머지 단어에 대한 카운트를 하기 위해서
            count =0# 사람마다 카운트를 0으로 시작하고
            for text in dic1[name]:#대화내용을 요소들로 반복하여 for문을 만들어줍니다.#
                if order in text:#인풋으로 받은 단어가 내용에 있으면 +1을 해줍니다.
                    count +=1
            print(name, count) #출력은 이름,카운트 횟수로 나옵니다.
            