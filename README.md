# 개요

[백준](https://www.acmicpc.net) 이나 [코드포스](https://codeforces.com) 문제를
풀 때 여러 케이스를 실행하여 결과를 보여줍니다.

# 설치

```sh
$ pip install problem_solving_offline_judge
```

문제풀이의 상단 디렉토리에 CLI 용 파일을 생성하여 다음과 같은 내용을 입력합니다.
파일명은 관계없지만 이 설명서에서는 `judge.py` 를 사용하겠습니다.

```py
# judge.py
from problem_solving_offline_judge import judge

judge.cli()
```

# 사용법

```sh
$ python3 ./judge.py <문제 디렉토리 이름>
```

파이썬에서는 패키지로 사용할 디렉토리 이름은 문자 나 `_` 로 시작해야 합니다.
하지만 디렉토리 이름을 전부 입력할 필요는 없습니다.

```sh
$ python3 ./judge.py b_1000
$ python3 ./judge.py 1000
```

성공할 경우 다음과 같이 출력됩니다.

```bash
$ python3 ./judge.py 1000
SUCCESS! 1.in (48 ms)
```

실패할 경우 다음과 같이 출력됩니다.

```bash
$ python3 ./judge.py 1000
FAIL! 1.in (47 ms)
Result:
2
Expected:
3
```

# 디렉토리 구조

```bash
├── b_1000
│   ├── 1.input.txt
│   ├── 1.output.txt
│   ├── 2.input.txt
│   ├── 2.output.txt
│   └── problem.py
├── b_1001
│   ├── ...
│   ├── ...
└── judge.sh
```

```py
# problem.py
# solve, solution, main 함수 중 하나는 반드시 있어야 합니다.
def solve():
    # 풀이 (아래는 백준 1000번 문제 샘플입니다)
    a, b = map(int, input().split())
    print(a+b)

# 백준이나 코드포스에 그대로 복사해서 붙여넣기 위해 필요합니다.
if __name__ == "__main__":
    solve()
```

- judge.py: CLI 스크립트
- \b_1000: 문제 디렉토리
- \b_1000/1.input.txt: 입력값. `1.in` 과 같은 형식도 가능합니다.
- \b_1000/1.output.txt: 솔루션이 출력해야하는 값. 입력값 파일명에서 `in` 을 `out` 으로 바꾸시면 됩니다.
- problem.py: 문제 모듈 파일. 이름은 `problem.py` 이 아니어도 됩니다. 자세한 구조는 위 파일내용을 참조해주세요.
