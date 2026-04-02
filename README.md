AWS EC2 환경에서 Nginx 리버스 프록시와 Flask를 결합하여 구축한 로그인 웹 서비스입니다.

## 서비스 주소
- URL: https://jizero.xyz

## Tech Stack & reason
-**Backend**: Python 3.12, Flask

원래는 Python과 잘 어울린다 Django로 하려고 했는데 로그인 서비스가 이미 다 구현이 되어있는 프레임워크이고
사용한 서버가 AWS EC2 프리티어라서 가볍고 빠르다는 Flask를 이용
  
-**Frontend**: HTML5, CSS3 (Glassmorphism Design)

HTML5를 이용한 이유는 Flask의 기능 중 하나가 서버에서 HTML에 데이터를 직접 주는 것이라고 해서
응답 속도를 조금 더 빠르게 하고 백엔드와 프론트엔드가 직접 연결되게 함. 개인적으로 그라데이션을 좋아하고 로그인 화면이 가운데에 오게 만들기 위해서 CSS3 사용함.
  
-**Web Server**: Nginx (Reverse Proxy)

Ngnix를 사용하는 이유는 보안을 위해서임. 서버의 실제 내부 IP를 숨길 수 있고 해킹 공격을 일차적으로나마 차단 가능
또한 Flask 대신 암호화 처리 해주어서 업무 분담해줄 수 있음.
 
 -**Security**: Let's Encrypt (HTTPS/SSL인증서), Flask Session Management
 
 무료 인증서 발급기관에서 Cerbot을 이용해 인증서 받음. https는 데이터 암호화하기 때문에 사용함. 또한 사용자가 로그인하면 Flask에 정보를 저장함.
 

## Directory Structure

- `app.py`: 메인 백엔드 서버 로직
  
- `templates/`: HTML 디자인 파일 모음
  
- `requirements.txt`: 프로젝트 의존성 라이브러리 목록
