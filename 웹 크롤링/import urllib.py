import urllib.request as req
img_url = "https://search.pstatic.net/sunny/?src=https%3A%2F%2Fi.pinimg.com%2Foriginals%2F21%2Ff9%2F83%2F21f98377d0d9f9efc27dfc19323d2c95.jpg&type=sc960_832"
html_url = "http://google.com"
save_path1 = "/Users/haneul/Desktop/웹 크롤링/test1.jpg"
save_path2 = "/Users/haneul/Desktop/웹 크롤링/index.html"
try:
    file1, header1 = req.urlretrieve(img_url, save_path1)
    file2, header2 = req.urlretrieve(html_url, save_path2)
except Exception as e:
    print("Download failed.")
    print(e)
else:
     print(header1)
     print(header2)

     print("download succeed") 
     