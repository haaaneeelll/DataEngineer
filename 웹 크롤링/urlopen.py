import urllib.request as req
from urllib.error import URLError, HTTPError

path_list = ["/Users/haneul/Desktop/웹 크롤링/test1.jpg", "/Users/haneul/Desktop/웹 크롤링/index.html"]

target_url = ["https://search.pstatic.net/sunny/?src=https%3A%2F%2Fi.pinimg.com%2Foriginals%2F21%2Ff9%2F83%2F21f98377d0d9f9efc27dfc19323d2c95.jpg&type=sc960_832"
,"http://google.com"]

for i, url in enumerate(target_url):
    try:
        # 웹 수신 정보 읽기
        response = req.urlopen(url)
        
        # 수신 내용
        contents = response.read()
        
        print('---------------------------')
        # 상태 정보 중간 출력
        print('Header Info-{} {}'.format(i, response.info()))
        print('HTTP Status Code: {}'.format(response.getcode()))
        print()
        print('---------------------------')
        

        # 파일 쓰기
        with open(path_list[i], 'wb') as c:
            c.write(contents)

    except HTTPError as e:
        print("Download failed.")
        print('HTTPError Code:', e.code)

    except URLError as e:
        print("Download failed.")
        print('URL Error Reason:', e.reason)

    else:
        print("Download Succeeded.")


