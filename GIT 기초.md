# GIT



## GIT 이란?

- Git은 분산버전관리시스템으로 코드의 버전을 관리하는 도구
- 2005년 리눅스 커널을 위한 도구로 리누스 토르발스가 개발
- 컴퓨터 파일의 변경사항을 추적하고 여러명의 사용자들 같의 해당 파일들의 작업을 조율



## 기본흐름

- modified : 파일이 수정된 상태
- stagef: : 수정한 파일을 곧 커밋할 것이라고 표시한 상태
- committed : 커밋이 된 상태



### 기초 명령어

|            명령어            |              내용              |
| :--------------------------: | :----------------------------: |
|           git init           |        로컬 저장소 생성        |
|      git add < 파일명 >      | 특정 파일/폴더의 변경사항 추가 |
| git commit -m '<커밋메시지>' |        커밋 (버전 기록)        |
|          git status          |           상태 확인            |
|           git log            |           버전 확인            |

## Git 설정 파일 (config)

- 사용자 정보 (commit author) : 커밋을 하기 위해 반드시 필요
  - git config —global user.name “username”
    - (Github에서 설정한 username으로 설정)
  - git config —global user.email “my@email.com"
    -  Github에서 설정한 email로 설정



## 원격저장소 만들기

1. 경로 설정
   - 원격 저장소 정보를 로컬 저장소에 추가
   - 로컬 저장소에는 한번만 설정 해주면 된다.
   - git remote add origin https://github.com/woocheolll/저장소 이름
2. 정보 확인
   - $ git remote -v
3. 활용 명령어
   - git push <원격저장소 이름> <브랜치이름>
   - 원격 저장소로 로컬 저장소 변경 사항(커밋)을 올림(push)
   -  로컬 폴더의 파일/폴더가 아닌 저장소의 버전(커밋)이 올라감
     1. push 주의 사항
        -  로컬 폴더의 파일/폴더가 아닌 저장소의 버전(커밋)이 올라감
        - 윈도우는 아래의 화면에서 인증을 하여야 합니다. (크롬 브라우저 활용)

