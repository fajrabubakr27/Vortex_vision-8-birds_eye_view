import cv2
import numpy as np

# 1. Setup paths and global variables
img = cv2.imread(r'C:\Users\fajra\PycharmProjects\Task8\assets\input_images\jhonsmith.jpg')
points = []


# 2. Mouse Callback Function
def get_mouse_points(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        if len(points) < 4:
            points.append([x, y])
            cv2.circle(img, (x, y), 5, (0, 255, 0), -1)
            cv2.imshow("Select 4 Corners", img)


# 3. Main Window Logic
cv2.namedWindow("Select 4 Corners")
cv2.setMouseCallback("Select 4 Corners", get_mouse_points)

print("Click 4 corners in order: Top-Left, Top-Right, Bottom-Left, Bottom-Right")
cv2.imshow("Select 4 Corners", img)
cv2.waitKey(0)  # Wait until any key is pressed after selecting 4 points

# 4. Perspective Transform
if len(points) == 4:
    width, height = 500, 300
    pts1 = np.float32(points)
    pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])

    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    output = cv2.warpPerspective(img, matrix, (width, height))

    # 5. Show and Save results
    cv2.imshow("Bird's Eye View", output)
    cv2.imwrite(r'C:\Users\fajra\PycharmProjects\Task8\assets\output_results/jhonsmith_result.jpg', output)
    cv2.waitKey(0)

cv2.destroyAllWindows()