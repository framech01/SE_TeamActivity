# Matrix Multiplication Benchmark

순수 Python 행렬곱과 NumPy 벡터화 연산의 실행 시간을 비교하고 프로파일링하는 교육용 벤치마크입니다.

## 사용 기술

- **Python 3.10+**: 3중 반복문 기반 알고리즘과 벤치마크 실행 흐름을 구현합니다.
- **NumPy**: `np.matmul`을 통해 BLAS 수준으로 최적화된 행렬곱을 수행하고 순수 Python 결과와 비교합니다.
- **전치 행렬 최적화**: 순수 Python 구현은 두 번째 행렬을 미리 전치해 열 접근을 연속적인 행 접근으로 바꾸고 indexing 비용을 줄입니다.
- **Generator Expression**: 각 셀의 dot product를 `sum(a * b ...)`로 계산해 명확한 수학 구조를 유지합니다.
- **time.perf_counter**: 짧은 실행 구간에 적합한 고해상도 단조 시계로 두 구현의 실행 시간을 측정합니다.
- **np.allclose**: 부동소수점 허용 오차를 고려해 두 구현의 계산 결과가 일치하는지 검증합니다.
- **cProfile**: 함수별 호출 횟수, 누적 실행 시간과 병목을 표준 라이브러리만으로 분석합니다.
- **line_profiler**: `@profile`이 적용된 행렬곱 함수의 줄별 실행 시간을 선택적으로 측정합니다.
- **argparse**: 행렬 크기와 random seed를 명령행에서 지정해 반복 가능한 실험을 구성합니다.

## 알고리즘 복잡도

두 방식의 이론적 시간 복잡도는 일반적인 정사각 행렬 기준 `O(n³)`입니다. 순수 Python은 각 산술 연산과 반복을 인터프리터에서 수행하지만 NumPy는 연속 메모리와 최적화된 네이티브 선형대수 루틴을 활용하므로 실제 실행 시간에는 큰 차이가 납니다. 입력과 결과 행렬의 공간 복잡도는 `O(n²)`입니다.

## 설치 및 실행

```bash
pip install -r requirements.txt
python benchmark_profile.py --size 200 --seed 42
```

함수 단위 프로파일링:

```bash
python -m cProfile -s cumulative benchmark_profile.py --size 200
```

줄 단위 프로파일링:

```bash
kernprof -l -v benchmark_profile.py --size 200
```

## 출력

- 순수 Python 실행 시간
- NumPy 실행 시간
- NumPy 대비 속도 향상 배수
- 두 구현의 결과 일치 여부

`--size`를 크게 설정하면 순수 Python의 `O(n³)` 연산으로 실행 시간이 급격히 증가하므로 작은 값부터 테스트하세요.
