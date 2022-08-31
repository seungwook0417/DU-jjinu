# DU-jjinu

주의❗ 이것은 스파게티와 짬뽕을 넘어선 찐 부대찌개 입니다❗

1. config.json 의 first_run 을 true 로 세팅한 뒤 스크립트를 1회 동작시키십시오.
2. config.json 의 first_run 을 false 로 세팅하고 계정 정보를 입력하십시오.
3. 서버에 스크립트를 계속 켜 두면 됩니다. 60초마다 자동으로 데이터를 가져옵니다.

## config.json
```json
{
  "account": {
    "chatID": "챗 아이디 작성",
    "token": "봇 API 기입"
  },
  "store_cnt": 100,
  "no_get_page": 5,
  "first_run": false
}
```