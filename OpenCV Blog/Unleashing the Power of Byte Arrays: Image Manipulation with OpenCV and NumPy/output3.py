import cv2

destination_folder = f"./outputs/"
if not os.path.exists(destination_folder):
  os.makedirs(destination_folder)

# reading the earth and astronaut images
earth_space = cv2.imread("earth-ga837aa373_1280.jpg")
astronaut = cv2.imread("science-g999b43884_1920.png", cv2.IMREAD_REDUCED_COLOR_2)

# now I want to paste the astronaut to the earth image
'''let's first view the topleft pixel and see if it's blank'''
# print(astronaut.item(0,0,3))
'''
so yeah it's blank
Now let us see the dimensions of the image
'''

# print(earth_space.shape) -> (1280, 1197, 3)
# print(astronaut.shape) -> (960, 721, 3)

# Now let's stick the astronaut onto the earth

# calculating gaps
gap_x = 1197 - 721 - 50 # this shifts to the right with a padding of 50
gap_y = (1280 - 960) // 2 # this centers

for i in range(gap_y, gap_y + 960):
    for j in range(gap_x, gap_x+721):
        earth_space[i,j] = astronaut[i - gap_y, j - gap_x] if (astronaut[i - gap_y, j - gap_x] != (0,0,0)).all() else earth_space[i,j]

cv2.imwrite("outputs\output3.png", earth_space)
