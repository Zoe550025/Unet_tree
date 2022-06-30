import cv2
import numpy as np

#https://cxybb.com/article/weixin_45875105/110871217
g_hls_h = []  # 图片分量 hls
g_hls_l = []
g_hls_s = []
g_diff_h, g_diff_l, g_diff_s = 0,0,0

# 修改图片各分量 组合成新图片
def change_hls(fname):
    global g_hls_h, g_hls_l, g_hls_s, g_diff_h, g_diff_l, g_diff_s

    # h分量
    hls_hf = g_hls_h.astype(np.float)
    hls_hf += g_diff_h
    hls_hf[hls_hf > 180] -= 180  # 超过180
    hls_hf[hls_hf < 0] += 180  # 小于0
    new_hls_h = hls_hf.astype("uint8")

    # l分量
    hls_lf = g_hls_l.astype(np.float)
    hls_lf += g_diff_l
    hls_lf[hls_lf < 0] = 0
    hls_lf[hls_lf > 255] = 255
    new_hls_l = hls_lf.astype("uint8")

    # s分量
    hls_ls = g_hls_s.astype(np.float)
    hls_ls += g_diff_s
    hls_ls[hls_ls < 0] = 0
    hls_ls[hls_ls > 255] = 255
    new_hls_s = hls_ls.astype("uint8")

    # 重新组合新图片 并转换成BGR图片
    new_bgr = cv2.cvtColor(cv2.merge([new_hls_h, new_hls_l, new_hls_s]), cv2.COLOR_HLS2BGR)
    cv2.imwrite(fname,new_bgr)
    #cv2.imshow("image", new_bgr)

# hsv分量值修改
def on_value(h,l,s,fname):
    global g_diff_h
    value_h = (h - 180)
    g_diff_h = value_h

    global g_diff_l
    value_l = l * 2
    value_l -= 255
    g_diff_l = value_l

    global g_diff_s
    value_s = s * 2
    value_s -= 255
    g_diff_s = value_s

    change_hls(fname)

def main():
    global g_hls_h, g_hls_l, g_hls_s
    fpath = "E:\\tzuwen\\tree_segmentation2\\Unet_tree_2\\2022-03-23_1031.png"
    new_name = "2022-03-23_1031_HA.png"
    H = 100
    L = 127
    S = 127

    # 加载图片
    img_org = cv2.imread(fpath)

    # hls分量拆分
    hls = cv2.cvtColor(img_org, cv2.COLOR_BGR2HLS)
    g_hls_h = hls[:, :, 0]
    g_hls_l = hls[:, :, 1]
    g_hls_s = hls[:, :, 2]

    on_value(H,L,S,new_name)

    cv2.waitKey(0)


if __name__ == '__main__':
    main()