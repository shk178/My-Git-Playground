from PIL import Image

# 변환할 WEBP 파일 경로
webp_file = "logo.webp"

# PNG 파일로 저장할 경로
png_file = "logo.png"

# 이미지 열기
with Image.open(webp_file) as img:
    img.save(png_file, "PNG")

print("변환 완료: PNG 파일이 저장되었습니다.")

