""" 

#darknet批量测试并生成坐标命令
例：
./darknet detector valid data/obj.data yolo.cfg backup/best.weights

本代码用于解析darknet.exe批量输出预测坐标后的txt文本并将预测框以及置信度并呈现在待测试图片上

"""
import cv2

img_file = "D:\\xx\\images"    # 原图地址 图片为png格式
detect_txt = "detect.txt"            # darknet解析坐标的文本 形如图片名 置信度 框的左上x 左上y 右下x 右下y的坐标
file = "C:\\xxx\\xxx"                # 输出文件夹

font=cv2.FONT_HERSHEY_SIMPLEX

def pics_draw(detect_txt):
    with open (detect_txt,'r') as f:
        lines = f.readlines()
        splitlines = [w.strip().split(' ')  for w in lines]
        name = "no_name"
        cnt = 0
        n = 0.3     # 置信度 

        for splitline in splitlines:
            cnt += 1
            if name == "no_name":
                name = str(splitline[0])
                img_data = cv2.imread(img_file + "\\" + str(splitline[0]) + ".png")
                if float(splitline[1]) >= n:
                    draw_img(img_data,splitline)

            elif splitline[0] != name:
                cv2.imwrite(file + "\\" + name + "_draw.png",img_data)
                name = str(splitline[0])
                img_data = cv2.imread(img_file + "\\" + str(splitline[0]) + ".png")
                if float(splitline[1]) >= n:
                    draw_img(img_data,splitline)

            elif splitline[0] == name:
                if float(splitline[1]) >= n:
                    draw_img(img_data,splitline)

            if cnt == len(splitlines):
                cv2.imwrite(file + "\\" + name + "_draw.png",img_data)

def draw_img(imgdata,recdata):                          # 画框
    rectangle_x = int(float(recdata[2]))
    rectangle_y = int(float(recdata[3]))
    rectangle_x1 = int(float(recdata[4]))
    rectangle_y1 = int(float(recdata[5]))
    draw = cv2.rectangle(imgdata,(rectangle_x,rectangle_y),(rectangle_x1,rectangle_y1),(0,0,255),1)
    cv2.putText(draw, str(recdata[1]), (rectangle_x,rectangle_y - 5), font, 0.5, (0,0,255), 1)
    return imgdata

def main():
    pics_draw(detect_txt)

                                    
if __name__ == "__main__":
    main()        
        