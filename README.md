# VLM-Qwen2.5-VL

# Qwen2.5-VL Gradio 인터페이스

Qwen2.5-VL 비전-언어 모델을 위한 현대적이고 사용자 친화적인 웹 인터페이스입니다. Gradio를 기반으로 제작되었습니다.

## 🚀 주요 기능

- 🖼️ **이미지 업로드**: 드래그 앤 드롭으로 손쉽게 이미지 업로드
- 💬 **대화형 챗**: 업로드한 이미지에 대해 질문 가능
- 🎨 **모던 UI**: 깔끔하고 직관적인 인터페이스
- ⚙️ **설정 가능**: 다양한 환경 설정 지원
- 🔧 **모듈형 설계**: 체계적으로 구성된 코드 구조

## 📁 프로젝트 구조

```
gradio/
├── run_app.py          # 메인 앱 실행 파일
├── app.py              # Gradio 인터페이스 구현
├── model.py            # Qwen2.5-VL 모델 래퍼
├── config.py           # 환경설정 파일
├── requirements.txt    # 파이썬 의존성 목록
├── run.sh              # 셸 스크립트 실행 파일
├── original_main.py    # 원본 추론 스크립트(참고용)
└── README.md           # 이 파일
```

## 🛠️ 설치 방법

### 사전 준비
- Python 3.8 이상
- CUDA 지원 GPU (권장)
- 8GB 이상 GPU 메모리

### 빠른 시작

1. **레포지토리 클론**
   ```bash
   git clone <your-repo-url>
   cd gradio
   ```

2. **의존성 설치**
   ```bash
   pip install -r requirements.txt
   ```

3. **앱 실행**
   
   **방법 1: Python으로 직접 실행**
   ```bash
   python run_app.py
   ```
   
   **방법 2: 셸 스크립트로 실행**
   ```bash
   ./run.sh
   ```

4. **브라우저에서 접속**
   - 로컬: http://localhost:7860
   - 네트워크: http://[서버-IP]:7860

## 🎯 사용법

1. **이미지 업로드**: 업로드 영역에 이미지를 클릭하거나 드래그
2. **질문 입력**: 이미지에 대해 궁금한 점을 입력
3. **답변 받기**: "답변 생성" 버튼 클릭 또는 Enter
4. **결과 확인**: 모델의 분석 결과를 출력 패널에서 확인

### 예시 질문
  - "이 이미지를 자세히 설명해줘"
  - "어떤 객체들이 보이나요?"
  - "주요 피사체는 무엇인가요?"
  - "두드러진 색상은 무엇인가요?"
  - "이 장면에서 무슨 일이 일어나고 있나요?"
  - "사람이 있나요? 무엇을 하고 있나요?"

## ⚙️ 환경설정

`config.py` 파일을 수정하여 원하는 설정을 적용할 수 있습니다:

```python
# 모델 설정
MODEL_NAME = "Qwen/Qwen2.5-VL-7B-Instruct"
MAX_NEW_TOKENS = 128

# 서버 설정
SERVER_PORT = 7860
SHARE = False  # 공개 링크 사용 시 True

# UI 설정
THEME = "soft"
IMAGE_HEIGHT = 400
```

## 🔧 문제 해결

### 자주 발생하는 문제

**CUDA 메모리 부족**
- `config.py`에서 `MAX_NEW_TOKENS` 값을 줄이세요
- 다른 GPU 프로그램을 종료하세요

**모델 로딩 실패**
- 인터넷 연결 확인
- Hugging Face 접근 권한 확인

**포트 사용 중**
- `config.py`에서 `SERVER_PORT` 변경
- 기존 프로세스 종료: `lsof -ti:7860 | xargs kill -9`

**의존성 문제**
- pip 업데이트: `pip install --upgrade pip`
- 가상환경 사용: `python -m venv venv && source venv/bin/activate`

## 📝 개발 안내

### 프로젝트 구조 설명

- **`run_app.py`**: Gradio 앱 실행 진입점
- **`app.py`**: Gradio UI 레이아웃 및 이벤트 핸들러
- **`model.py`**: Qwen2.5-VL 모델 래퍼
- **`config.py`**: 환경설정 관리
- **`original_main.py`**: 원본 프로젝트의 참고 구현

### 기능 추가 방법

1. **커스텀 테마**: `config.py`에서 테마 변경
2. **새 UI 요소**: `app.py`에 컴포넌트 추가
3. **모델 설정**: `model.py`에서 파라미터 조정
4. **예시 질문**: `config.py`의 `EXAMPLE_QUESTIONS` 수정

## 📜 라이선스

본 프로젝트는 Qwen2.5-VL 모델의 라이선스를 따릅니다.

## 🤝 기여 방법

1. 레포지토리 포크
2. 기능 브랜치 생성
3. 변경사항 반영
4. 풀 리퀘스트 제출

## 📞 문의 및 지원

문제 및 질문은 아래 방법을 이용하세요:
- 위 문제 해결 섹션 참고
- Qwen2.5-VL 공식 문서 확인
- 이 레포지토리에 이슈 등록

---

**즐거운 코딩 되세요! 🎉**
