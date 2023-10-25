<p align="center"><img width="100%" src="Images/2.png" /></p>

**순천향대학교 학사 공지사항 알리미 입니다.**

개발 기간 : 2023.10.26 ~ 2023.10.26 (1시간)

## 프로젝트 소개
기존 대학교 공지 사항을 확인하기 위해 주기적으로 접속해야 하는 단점이 존재했습니다. 이 단점을 보완하고자 공지 사항을 주기적으로 크롤링하여 Slack 메시지로 알림을 울리게 하여 공지 사항을 더욱 편하게 확인하고자 제작하였습니다. 또한 주기적으로 실행하기 위해 서버리스 아키텍쳐를 이용하여 구동하였습니다.

현재 프로젝트는 주기적으로 크롤링을 진행하지만, 기회가 된다면 실시간으로 알림을 전송할 수 있도록 수정하고싶습니다.

## 실사용 사진
![Running Image](Images/1.png)

## 개발환경
* 운영체제 : Windows 11 x64 (22H2, 22621.2428)
* 사용 언어 : Python 3.12.0
* 사용 라이브러리 : [BeautifulSoup4(4.12.2)](https://pypi.org/project/beautifulsoup4/), [slack_sdk(3.23.0)](https://pypi.org/project/slack-sdk/)
* 사용 서버리스 호스팅 : [Naver Cloud Functions](https://www.ncloud.com/product/compute/cloudFunctions)

## 설치하기

### 라이브러리 설치
```bash
pip install beautifulsoup4==4.12.2
pip install slack-sdk==3.23.0
```

### 프로젝트 설치
```bash
git clone https://github.com/mokminsu/SCH-Notify.git
cd SCH-Notify
```

## 실행하기

```py3
args = {
    'slack_token': 'token',
    'slack_channel_id': 'id'
}

main(args)
```

## 함수 설명
* **fetch_current_notices** : 해당 페이지의 공지사항들의 제목, 작성자, 작성일을 스크랩
* **post_to_slack** : 슬랙으로 메시지를 전송함

## 사용 스택

### 개발 환경
![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-007ACC?style=for-the-badge&logo=Visual%20Studio%20Code&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=Git&logoColor=white)
![Github](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=GitHub&logoColor=white)             

### 개발 언어
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffffff)

## 유의사항
이 프로젝트는 해당 웹사이트의 웹 크롤러 같은 로봇들의 접근을 제어하기 위한 규약을 준수하였습니다.

그러나 해당 프로젝트의 사용으로 인해 발생하는 모든 피해를 책임지지 않습니다.


## 라이센스
이 프로젝트는 [MIT License](LICENSE)로 배포됩니다.