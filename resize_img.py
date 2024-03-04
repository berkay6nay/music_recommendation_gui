from PIL import Image

image = Image.open('img/54a9766fc75926c2adcd3181afe26db1.jpg')
image2 = Image.open("img/png-transparent-computer-icons-font-awesome-stop-button-building-text-united-states.png")
play_resized = image.resize((50, 50))
stop_resized = image2.resize((50, 50))
play_resized.save('play50.png')
stop_resized.save("stop50.png")