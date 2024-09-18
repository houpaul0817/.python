#標準寫法
import matplotlib.pyplot as plt

# 1.製作figure
fig = plt.figure()

# 2.在1.的figure上製作一個axes
ax_1 = fig.add_subplot(1, 1, 1)

# 3.將圖的數據儲存在axes中
X = [0, 1, 2]
Y = [3, 4, 5]
ax_1.plot(X, Y, 'bo-.')

# 4.顯示圖
plt.show()

